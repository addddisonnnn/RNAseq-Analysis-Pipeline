#!/usr/bin/env nextflow

process MULTIQC {
    label 'process_low'
    container 'ghcr.io/bf528/multiqc:latest'
    
    // The publishDir is set to output the final report to the main results folder
    publishDir "${params.outdir}/results/multiqc", mode: 'copy', overwrite: true

    input:
    // Takes a list of all output files/logs from previous processes
    path multiqc_files

    output:
    path "multiqc_report.html", emit: report

    shell:
    """
    # -f is required to force MultiQC to run even if it finds issues with file names/structure
    multiqc -f . 
    """
}
