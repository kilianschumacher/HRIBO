#!/usr/bin/env python
'''This script takes input files generated by
reparationGFF and merges all replicates into one file, for each condition.
'''

import os
import argparse
import pandas as pd

def concatGff(args):
    # create dataframes of all non-empty files
    dataFrames = []
    for file in args.reparation_files:
        if os.stat(file).st_size != 0:
            dataFrames.append(pd.read_csv(file, sep='\t', header=None))

    prefix = os.path.basename(args.reparation_files[0]).split("-")[0]
    # check if dataframe exist for concatination
    if len(dataFrames) != 0:
        mergedGff = pd.concat(dataFrames)

        ### Handling output
        # write to file
        outputFile = os.path.join(args.output_folder,"%s.reparation.gff" %prefix)
        with open(outputFile, 'w') as f:
            mergedGff.to_csv(f, sep="\t", header=False, index=False)


def main():
    # store commandline args
    parser = argparse.ArgumentParser(description='Converts reperation output to new data frame\
                                     containing specified information and saves it in gff3 format.')
    parser.add_argument("reparation_files", nargs="*", metavar="reparation", help= "Path to reparation gff files.")
    parser.add_argument("output_folder", help= "output folder for concatenated files.")
    args = parser.parse_args()

    concatGff(args)

if __name__ == '__main__':
    main()