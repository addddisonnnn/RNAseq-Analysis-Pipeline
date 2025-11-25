#!/usr/bin/env nextflow

process INDEX{
    label 'process_high'
    container 'ghcr.io/bf528/star:latest'

    input:
    path genome
    path gtf
    
    output:
    path "star_index", emit: index

    shell:
    """
    mkdir star_index
    STAR --runThreadN $task.cpus --runMode genomeGenerate --genomeDir star_index --genomeFastaFiles $genome --sjdbGTFfile $gtf
    """
}