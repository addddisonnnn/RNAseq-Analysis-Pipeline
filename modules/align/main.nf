#!/usr/bin/env nextflow

// This process aligns paired-end reads using the pre-built STAR index.

process ALIGN {
    label 'process_high'
    container 'ghcr.io/bf528/star:latest'

    // FIX: Define the input tuple to match the 3 elements coming from main.nf:
    // 1. val(name): Sample name (val)
    // 2. path(reads_list): The list of R1, R2 paths (path)
    // 3. path(genome_index_dir): The index directory (path)
    input:
    tuple val(name), path(reads_list), path(genome_index_dir)

    output:
    path "${name}.Aligned.sortedByCoord.out.bam", emit: bam
    path "${name}.Log.final.out", emit: log

    script:
    // FIX: Unpack the reads_list array into two separate variables for the STAR command.
    def read1 = reads_list[0]
    def read2 = reads_list[1]

    """
    STAR --runThreadN ${task.cpus} \\
         --genomeDir ${genome_index_dir} \\
         --readFilesIn ${read1} ${read2} \\
         --readFilesCommand zcat \\
         --outFileNamePrefix ${name}. \\
         --outSAMtype BAM SortedByCoordinate \\
         --outBAMcompression 10 \\
         2> ${name}.Log.final.out
    """
}