#!/usr/bin/env python
'''This script takes n number of input files generated by
ribotish and creates a gff3 file.
'''

import pandas as pd
import re
import argparse
import numpy as np
import os

# function to read in ribosome profiling output files ORFs_max_filt
def create_table(name):
    df = pd.read_table(name)
    return df

# function to keep only certain columns
def filter_cols(df_ORFs):
    df_kept = df_ORFs[["GenomePos", "AALen", "Gid", "Symbol", "Tid", "StartCodon", "TisType", "TISPvalue", "RiboPvalue", "FisherPvalue"]]
    df_kept.columns = ["ORF_id_gen", "ORF_length", "gene_id", "gene_symbol", "transcript_id", "start_codon", "tis_type", "tis_pvalue", "ribo_pvalue", "fisher_pvalue"]
    return df_kept

#Tid	Symbol	GenomePos	StartCodon	Start	Stop	TisType	TISGroup	TISCounts

# function to get chromosome name
def chrom_name(column):
    chrom = []
    for i in column:
        match = re.findall("^[0-9A-Za-z]+", i)
        for a in match:
            chrom.append(a)
    return chrom


# function to get start position
def start(column):
    start = []
    for i in column:
        match = re.findall(":([0-9]+)-", i)
        for a in match:
            startstring = str(int(a)+1)
            start.append(startstring)
    return start


# function to get stop position
def stop(column):
    stop = []
    for i in column:
        match = re.findall("-([0-9]+):", i)
        for a in match:
            stopstring = str(int(a))
            stop.append(stopstring)
    return stop

def strand(column):
    strand = []
    for i in column:
        match = re.findall(":([+-])$", i)
        for a in match:
            strand.append(a)
    return strand


# function to create final data frame
def create_output(args):
    #rearrange column

    df_final = pd.DataFrame(columns=["ORF_id_gen","chromosome","start","stop","gene_id","gene_symbol","start_codon","tis_type","tis_pvalue","ribo_pvalue","fisher_pvalue","strand","ORF_length","transcript_id"])
    # Create data frame from all input files
    for name in args.ribotish_files:
        #for nonempty files
        if os.stat(name).st_size != 0:
            print(name)
            #read file into dataframe and drop columns not of interest
            df_sub = filter_cols(name)
            # rename columns to chromosome, start, and stop
            df_sub["strand"] = strand(df_sub["ORF_id_gen"])
            df_sub["chromosome"] = chrom_name(df_sub["ORF_id_gen"])
            df_sub["start"] = start(df_sub["ORF_id_gen"])
            df_sub["stop"] = stop(df_sub["ORF_id_gen"])
            
            df_kept = df_sub[["ORF_id_gen","chromosome","start","stop","gene_id","gene_symbol","start_codon","tis_type","tis_pvalue","ribo_pvalue","fisher_pvalue","strand","ORF_length","transcript_id"]]
            for new_index, new_row in df_kept.iterrows():
                 #check if entry with overlapping coordinates already exists
                 orf_range = range((int(new_row.start)), (int(new_row.stop)))
                 orf_set = set(orf_range)
                 orf_length = int(new_row.stop) - int(new_row.start)
                 intersection_switch = False
                 if len(df_final) != 0:
                     current_index = len(df_final)
                     df_final.loc[current_index] = new_row
                 else:
                     current_index = 0
                     df_final.loc[current_index] = new_row

            # Cleaning up data frame
            df_final.drop_duplicates(subset="ORF_id_gen", inplace=True)
            df_final.reset_index(inplace=True)
            df_final.drop(["index"], axis=1, inplace=True)


            # Filter min and max uORF lengths
            if args.min_length is not None:
                print("Length filterset to min: " + args.min_length)
                df_final = df_final[df_final['ORF_length'] >= int(args.min_length)]

            if args.max_length is not None:
                print("Length filterset to max: " + args.max_length)
                df_final = df_final[df_final['ORF_length'] <= int(args.max_length)]
    return df_final


def make_ORFs_gff3(args):
    ORFsString = ""
    for index, row in args.iterrows():
        ORFString=row.chromosome + "\t" + "ribotish" + "\t" + "CDS" + "\t" + row.start + "\t" + row.stop + "\t" + "." + "\t" + row.strand + "\t" + "." + "\t" + "transcript_id ribotish" + index + ";" + "start_codon " + row.start_codon + ";" +  "tis_type " + row.tis_type + ";" +  "tis_pvalue " + row.tis_pvalue  + ";" +  "ribo_pvalue " + row.ribo_pvalue + ";" +  "fisher_pvalue " + row.fisher_pvalue + "\n"
        ORFsString= ORFsString + ORFString
    return(ORFsString)

def main():
    # store commandline args
    parser = argparse.ArgumentParser(description='Converts ribotish output to gff3.')
    parser.add_argument('ribotish_files', nargs='*', metavar='ribotish', help='Path to ribotish ORF file')
    parser.add_argument("--output_gff3_filepath", help='Path to write \
                        gff3 output')
    parser.add_argument("--min_length", default=None, help='Minimal uORF \
                        length')
    parser.add_argument("--max_length", default=None, help='Maximal uORF \
                        length')
    args = parser.parse_args()
    # make sure that min_length and max_length are given
    orfsframe = create_output(args)
    #print(output.describe(include='all'))
    # write output to gff3 file
    ORFsgff=make_ORFs_gff3(orfsframe)
    f = open(args.output_gff3_filepath, 'wt', encoding='utf-8')
    f.write(ORFsgff)

if __name__ == '__main__':
main()
