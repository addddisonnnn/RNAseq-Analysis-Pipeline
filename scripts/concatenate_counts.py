#!/usr/bin/env python
"""
A script to concatenate multiple VERSE .exon.txt count files 
into a single gene-by-sample matrix using pandas.
"""
import argparse
import pandas as pd
import os
import sys

def concatenate_counts(input_files, output_file):
    """
    Concatenates gene count files into a single, combined TSV file.
    
    It automatically skips any files that appear to be summary reports
    (i.e., files ending in '.summary.txt').
    """
    print(f"Concatenating {len(input_files)} potential count files...")
    
    all_data = []
    
    # List to store file names that are actually processed
    processed_files = []

    for file_path in input_files:
        # Check to skip summary files which cause parsing errors
        if file_path.endswith('.summary.txt'):
            print(f"Skipping summary report: {file_path}")
            continue

        try:
            # Gene count files are typically tab-separated (TSV) 
            # and may have a header line. We read them in, making 
            # the gene identifier the index.
            df = pd.read_csv(
                file_path,
                sep='\t',
                index_col=0,  # Use the first column (Gene ID) as the index
                header=None,  # Treat the file as having no header line
                names=['Gene_ID', 'Count'],
                usecols=[0, 1] # Only read the first two columns (index 0 and 1)
            )

            # Extract the sample name from the file path for the column header
            # Example: 'control_rep1.counts.gene.txt' -> 'control_rep1'
            sample_name = os.path.basename(file_path).split('.')[0]
            
            # The counts are in the second column (index 1) which we rename 
            # to the sample name
            counts_series = df['Count']
            counts_series.name = sample_name
            
            all_data.append(counts_series)
            processed_files.append(file_path)
            
        except Exception as e:
            # Print the error and exit gracefully if a critical count file fails
            print(f"Error processing file {file_path}: {e}", file=sys.stderr)
            sys.exit(1)

    if not all_data:
        print("No valid count files found to concatenate. Exiting.", file=sys.stderr)
        sys.exit(1)

    # Combine all series into a single DataFrame
    combined_df = pd.concat(all_data, axis=1)

    # Write the final combined table to the specified output file
    combined_df.to_csv(output_file, sep='\t')
    print(f"Successfully concatenated {len(processed_files)} files into {output_file}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Concatenate multiple single-column gene count TSV files into one large table."
    )
    # The input files are passed as positional arguments
    parser.add_argument(
        'input_files', 
        nargs='+', 
        help='List of gene count files to concatenate.'
    )
    parser.add_argument(
        '--output', 
        required=True, 
        help='Name of the final concatenated output file (TSV).'
    )
    
    args = parser.parse_args()
    concatenate_counts(args.input_files, args.output)