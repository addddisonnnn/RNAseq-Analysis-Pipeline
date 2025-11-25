#!/usr/bin/env nextflow

process FASTQC {
   label 'process_low'
   container 'ghcr.io/bf528/fastqc:latest'
   publishDir "${params.outdir}/fastqc", mode: 'copy'

   input:
   tuple val(name), path(reads)

   output:
   tuple val(name), path('*.zip'), emit: zip
   tuple val(name), path('*.html'), emit: html

   script:
   """
   fastqc -t $task.cpus $reads
   """
}
