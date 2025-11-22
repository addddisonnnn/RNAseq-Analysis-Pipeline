#!/usr/bin/env python

import argparse
import re
import os
import sys

# argparse setup
parser = argparse.ArgumentParser(description='Parse a GTF file to extract Ensembl gene IDs and gene names.')

#input and output file arguments
parser.add_argument("-i", "--input", help='Path to the input GTF file', dest="input", required=True)
parser.add_argument("-o", "--output", help='Path for the output to the tab-delimited map file (ID and symbol)', dest="output", required=True)

#run the parser and input the data into an object
args = parser.parse_args()

gtf_path = args.input
output_path = args.output

if not os.path.exists(gtf_path):
    sys.stderr.write(f"Error: Input GTF file not found at {gtf_path}\n")
    sys.exit(1)

print(f"Starting GTF parsing for: {gtf_path}")

# Regular expressions for attribute extraction: looks for e.g., gene_id "ENSG...";
gene_id_re = re.compile(r'gene_id\s+"([^"]+)";')
gene_name_re = re.compile(r'gene_name\s+"([^"]+)";')

gene_map = {}
lines_processed = 0

try:
    with open(gtf_path, 'r') as infile:
        for line in infile:
            # Skip header/comments
            if line.startswith('#'):
                continue

            lines_processed += 1
            
            # Split the tab-delimited line
            parts = line.strip().split('\t')
            
            if len(parts) < 9:
                continue
            
            feature_type = parts[2]
            attributes = parts[8]
            
            # Only process lines defining a 'gene' feature
            if feature_type == 'gene':
                
                # 1. Extract Gene ID
                match_id = gene_id_re.search(attributes)
                if match_id:
                    # Remove version suffix (e.g., ENSG... .10 -> ENSG...)
                    gene_id = match_id.group(1).split('.')[0]
                else:
                    continue # Must have a gene_id to proceed

                # 2. Extract Gene Name (Symbol)
                match_name = gene_name_re.search(attributes)
                # If gene_name is missing, use the gene_id as a fallback
                gene_name = match_name.group(1) if match_name else gene_id
                
                # Store unique mappings
                if gene_id not in gene_map:
                    gene_map[gene_id] = gene_name

except Exception as e:
    sys.stderr.write(f"An error occurred during parsing GTF: {e}\n")
    sys.exit(1)

print(f"Extracted {len(gene_map)} unique gene IDs from {lines_processed} lines.")

# Write the output file
try:
    with open(output_path, 'w') as outfile:
        # Write header
        outfile.write("ensembl_gene_id\thuman_gene_symbol\n")
        
        # Write data
        for gene_id, gene_symbol in sorted(gene_map.items()):
            outfile.write(f"{gene_id}\t{gene_symbol}\n")
    
    print(f"Successfully wrote gene map to {output_path}")

except Exception as e:
    sys.stderr.write(f"An error occurred during writing output file: {e}\n")
    sys.exit(1)