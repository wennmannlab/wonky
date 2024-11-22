# wonky - Basic read statistics for Nanopore reads
Nanopore FASTQ Read Quality and Content Analysis Tool

This tool extracts unique identifiers from nanopore FASTQ files and calculates essential metrics for each read, including mean quality, read length, and GC content. The output is a tab-delimited file with the following structure:

Unique Identifier - Unique ID for each read
Mean Quality - Average quality score of each read
Read Length - Total base count per read
GC Content - GC percentage for each read

To gives an easy intergration, A Galaxy XML wrapper is provided for seamless integration into respective Galaxy.

