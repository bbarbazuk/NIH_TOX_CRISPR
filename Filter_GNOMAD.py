import argparse
import pandas as pd

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Filter rows in a CSV based on a list of gene names.\n\n"
                    "Example usage:\n"
                    "  python filter_genes.py data/large.csv genes.txt filtered.csv",
        formatter_class=argparse.RawTextHelpFormatter  # Enables multi-line help text
    )
    parser.add_argument("large_csv_path", help="Path to the large CSV file.")
    parser.add_argument("genes_list_path", help="Path to the file containing gene names (one per line).")
    parser.add_argument("output_csv_path", help="Path to save the filtered CSV.")

    args = parser.parse_args()

    # Read gene list
    with open(args.genes_list_path, "r") as f:
        target_genes = set(line.strip() for line in f if line.strip())

    # Filter matching rows
    matching_rows = []
    with open(args.large_csv_path, "r") as f:
        header = f.readline().strip().split(",")  # Read header
        gene_column_index = 0  # Adjust if gene column is not the first

        for line in f:
            row = line.strip().split(",")
            if len(row) <= gene_column_index:
                continue  # Skip malformed lines
            gene_name = row[gene_column_index]
            if gene_name in target_genes:
                matching_rows.append(row)

    # Convert to DataFrame and save
    df = pd.DataFrame(matching_rows, columns=header)
    df.to_csv(args.output_csv_path, index=False)

    print(f"✅ Extracted {len(df)} matching rows to '{args.output_csv_path}'.")

if __name__ == "__main__":
    main()

