import argparse
import pandas as pd

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Filter a gene expression CSV to retain only specified sample columns.\n\n"
                    "Example usage:\n"
                    "  python filter_samples.py filtered_genes.csv liver_samples.txt filtered_output.csv",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("filtered_csv_path", help="Path to the filtered gene expression CSV.")
    parser.add_argument("sample_names_path", help="Path to the file containing sample names to keep (one per line).")
    parser.add_argument("output_filtered_csv", help="Path to save the new filtered CSV.")

    args = parser.parse_args()

    # Read sample names to retain
    with open(args.sample_names_path, "r") as f:
        target_samples = set(line.strip() for line in f if line.strip())

    # Load the gene expression CSV
    df = pd.read_csv(args.filtered_csv_path)

    # Keep the first column (gene names or IDs) + any sample columns that match
    first_col = df.columns[0]
    columns_to_keep = [col for col in df.columns if col == first_col or col in target_samples]

    # Filter and save
    filtered_df = df[columns_to_keep]
    filtered_df.to_csv(args.output_filtered_csv, index=False)

    print(f"✅ Filtered DataFrame with {len(columns_to_keep)-1} matching sample columns saved to '{args.output_filtered_csv}'.")

if __name__ == "__main__":
    main()
