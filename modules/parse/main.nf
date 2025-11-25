#!/usr/bin/env nextflow

process PARSE {
    container 'ghcr.io/bf528/biopython:latest'
    publishDir "${params.outdir}/gene_map", mode: 'copy'

    input:
    path gtf

    output:
    path 'geneIDs.txt', emit: IDs

    shell:
    """
    parseGTF.py -i $gtf -o geneIDs.txt
    """
}