### version 1.5.1 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 28.07.2021
 * fixed issue which sometimes caused crashes in coverage file generation.
 * fixed versioning issues with snakemake and multiQC.
 * updated documentation + Manual
 
### version 1.5.0 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 09.06.2021
 * added improved meta gene profiling figures
 * added automatic detection of peak read lengths
 * added detection of best offset for individual readlengths
 * added pip packaging
 * functions organized in library
 * added old_locus_tag information to annotation excel files.
 * fixed a bug in the metagene-profiling that would cause a strange peak at the start/end for 5 or 3prime mappings.
 * improved the plot output for the metagene-profiling when checking many read lengths.
 * slightly changed the metagene-profiling read-counting to make it more comparable to the build in coverage files.
 * added metagene profiling for stop codons, this is automatically used on TTS and RNATTS libraries.

### version 1.4.4 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 18.09.2020
 * added overlap column to the overview table, to show whether an entry overlaps with an annotated gene. 
 * improved the handling of TE wildcards in excel scripts, allowing input combinations that were previously not possible.
 * minor fix for mapping script that ensures the header is set correctly for the "mil" mapping. 
 * minor fix that ensures the gene_name is set correctly and not sometimes replaced by the locus_tag.
 * fixed a bug where tranlation of nt_seqs were done only up to the first stop codon.
 * improved gtf2gff3 script to use gene_biotype to find RNA features.
 * improved start/stop gff files (including motifs and frames)
 * added 15nt upstream of the start codon to each .xlsx table.
 * updated reparation environment
 * some code clean-up
 
### version 1.4.3 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 15.05.2020
 * added genome-browser identifier to overview table
 * completely reworked gff2 support by transforming gff2 to gff3. This is unavoidable as some tools require gff3 format
 * added script to convert gff2 to gff3
 * improved overview table by adding and reordering columns
 * improved TE calculation to be less confusing, using NaN if read-counts are 0 and would lead to division by 0
 * improved excel file generation
 * resolved redundancies in excel files
 * updated manual + online documentation

### version 1.4.2 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 25.04.2020
 * fixed bug causing generate_overview_excel.py to crash for certain deepribo files
 * updated manual

### version 1.4.1 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 20.04.2020
 * added support for multi-condition results for differential expression in the overview table
 * updated manual

### version 1.4.0 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 17.04.2020
 * added overview table that aggregates all important information about ORFs
 * updated readcounting to consitently use the same method
 * updated makereport script
 * updated manual

### version 1.3.2 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 24.03.2020
 * updated sge.yaml
 * updated torque.yaml
 * bugfixed retrieveAnnotation
 * added xlsx output for xtail and riborex
 * added updated annotation containing reparation predictions and the orginal annotation
 * updated manual

### version 1.3.1 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 13.02.2020

 * added makereport script

### version 1.3.0 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 30.01.2020

 * integration of deepribo
 * added metagene profiling
 * added pseudogene read counting
 * refactoring of scripts folder
 * renamed summary.xlsx -> predictions_reparation.xlsx
 * removal of unneeded dependencies
 * Refactored Snakefiles

### version 1.2.0 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 22.01.2020

 * updated reparation to v1.0.9
 * added differential expression analysis with Riborex and Xtail
 * added TIS support to generate_excel.py
 * standardized output annotation to GFF3 format
 * updated HRIBO Manual

### version 1.1.0 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 22.08.2019

  * added paired-end support
  * paired-end mapping (currently no tools allowing this exist)
  * combined paired-end mapping
  * improved samples.xlsx (for paired end)
  * improved count_tables (rounding numbers to 2 floating points)
  * fix for annotation generation

### version 1.0.0 [Rick Gelhausen & Florian Eggenhofer](mailto:gelhausr@informatik.uni-freiburg.de) 08.08.2019

 + initial commit
