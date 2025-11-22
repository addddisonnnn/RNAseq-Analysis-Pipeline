# Analysis and Methods Summary
Data Source: RNA-seq data from 6 samples (3 WT control + 3 TYK2 KO experimental) at S5 endocrine progenitor stage.

## Quality Control & Alignment:

FastQC for read quality assessment

MultiQC for aggregating QC reports

STAR for alignment to GRCh38 human genome

VERSE for gene-level read counting

## Data Processing:

Filtered lowly expressed genes using CPM ≥ 1 in ≥3 samples

Reduced from 63,241 to 13,197 genes

DESeq2 for normalization and differential expression

Significance threshold: padj < 0.05

Additional biological relevance filter: |log2FC| ≥ 1

## Pathway Analysis:

Enrichr/Reactome: Threshold-based analysis of significant DEGs

FGSEA: Gene Set Enrichment Analysis using all genes ranked by log2FC

Both methods used C2 canonical pathways from MSigDB

## Visualization
ggplot2 and pheatmap for all plots (PCA, heatmaps, volcano plots, pathway enrichment)

## Takeaway
The pipeline successfully identified 1,116 significant DEGs (48 upregulated, 100 downregulated) and revealed key biological pathways affected by TYK2 knockout.
