# RNA-seq Analysis: TYK2 Role in Pancreatic Beta-Cell Development

## Project Overview

This project reproduces the bioinformatic analysis from the publication "The type 1 diabetes gene TYK2 regulates β-cell development and its responses to interferon-α" by Chandra et al. (Nature Communications, 2022). The analysis focuses on RNA-seq data from wild-type versus TYK2 knockout cells at the S5 endocrine progenitor stage to understand TYK2's role in pancreatic beta-cell development.

## Project Structure

  
  ```text
  rnaseq-project/
  │
  |-- data/ # Input data files
  │ ├── final_counts.tsv # Raw count matrix
  │ └── geneIDs.txt # Gene ID to symbol mapping
  │
  ├── envs/ # Conda environment files
  │ └── base_env.yml # Environment specification
  │
  ├── modules/ # Nextflow modules
  │ └── align/
  │ └── concatenate/
  │ └── fastqc/
  │ └── index/
  │ └── multiqc/
  │ └── parse/
  │ └── verse/
  │
  ├── results/ # Analysis outputs
  │ ├── significant_genenames_for_DAVID_*.txt # Gene lists for enrichment
  │ ├── FGSEA_C2_results.tsv # FGSEA pathway results
  │ ├── Reactome_Pathways_2024_table.txt # Reactome enrichment results
  │ └── *.png # Generated figures
  │
  ├── scripts/ # Analysis scripts
  │ └── MainAnalysis.Rmd # Main analysis R Markdown file
  │ └── concatenate_counts.py # Concatenate VERSE .exon.txt count files into a gene-by-sample matrix
  │ └── parseGTF.py # Parse GTF files for gene ID and name
  │
  ├── workflows/ # Nextflow workflows
  │ ├── main.nf # Main Nextflow pipeline
  │ └── nextflow.config # Nextflow configuration
  │
  ├── RNAseq_Project_Report.pdf # Compiled PDF report
  │
  └── README.md
```

## Key Findings

- **Differential Expression:** Identified 1,116 significant differentially expressed genes (48 upregulated, 100 downregulated with |log2FC| ≥ 1)
- **Pathway Enrichment:** TYK2 knockout affects extracellular matrix organization and beta-cell development pathways
- **Quality Control:** High-quality RNA-seq data with >92% alignment rates and clear separation in PCA
- **Comparison to Original Study:** Similar biological conclusions despite methodological differences in gene counts

## Analysis Pipeline

### 1. Quality Control & Preprocessing
- FastQC and MultiQC for read quality assessment
- STAR alignment to GRCh38 reference genome
- VERSE for gene-level quantification
- CPM filtering (≥1 CPM in ≥3 samples)

### 2. Differential Expression Analysis
- DESeq2 for normalization and statistical testing
- Thresholds: padj < 0.05, |log2FC| ≥ 1
- Volcano plot visualization

### 3. Functional Enrichment
- **Enrichr/Reactome:** Over-representation analysis of significant DEGs
- **FGSEA:** Gene set enrichment analysis using ranked genes
- Both methods using C2 canonical pathways from MSigDB

### 4. Quality Assessment
- PCA and sample distance heatmaps
- Biological replicate consistency evaluation

## Tools and Versions

- R 4.4.3 with Bioconductor packages
- DESeq2 1.50.0 (differential expression)
- FGSEA 1.32.4 (pathway enrichment)
- ggplot2 3.5.1 (visualization)
- FastQC 0.12.1 (quality control)
- STAR 2.7.11b (alignment)
- VERSE 0.1.5 (read counting)

## Usage

To reproduce the analysis:

1. Ensure all required R packages are installed
2. Run the `Project2Report.Rmd` script in RStudio
3. The analysis will generate all figures and results in the `results/` directory

## Results Interpretation

The analysis confirms TYK2's critical role in regulating:
- Extracellular matrix organization pathways
- Beta-cell developmental transcription factors (NEUROG3, NKX2-2, INSM1)
- Cell signaling and motility pathways

These findings provide mechanistic insights into how TYK2 genetic variants may contribute to Type 1 Diabetes risk by disrupting beta-cell development.

## Reference

Chandra, V., Ibrahim, H., Halliez, C. et al. The type 1 diabetes gene TYK2 regulates β-cell development and its responses to interferon-α. Nat Commun 13, 6363 (2022). https://doi.org/10.1038/s41467-022-34069-z
