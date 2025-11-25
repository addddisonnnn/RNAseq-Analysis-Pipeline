#!/usr/bin/env nextflow

process CONCATENATE {
    label 'process_low'
    container 'ghcr.io/bf528/pandas:latest'
    publishDir "${params.outdir}/results", mode: 'copy'

    // The input is a channel containing all files output by the VERSE process
    input:
    path input_files // A list/array of all count and summary files

    output:
    path "final_counts.tsv", emit: final_counts

    script:
    """
    # Use the Groovy spread operator (the space after ${input_files}) 
    # to expand the list/array of files into space-separated arguments 
    # for the command line.
    concatenate_counts.py --output final_counts.tsv ${input_files.join(' ')}
    """
}