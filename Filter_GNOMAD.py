import pandas as pd
import regex as re

#TEST

#config
large_csv_path = ""           
genes_list_path = ""       
output_csv_path = ""     

# READ LIST OF GENES TO MATCH
with open(genes_list_path, "r") as f:
    target_genes = set(line.strip() for line in f if line.strip())

# filter
matching_rows = []
with open(large_csv_path, "r") as f:
    header = f.readline().strip().split(",")  # read header
    gene_column_index = 0  # Assuming gene list is col 1

    for line in f:
        row = line.strip().split(",")
        gene_name = row[gene_column_index]
        if gene_name in target_genes:
            matching_rows.append(row)

#conv 2 df and save
df = pd.DataFrame(matching_rows, columns=header)
df.to_csv(output_csv_path, index=False)

print(f"Extracted {len(df)} matching rows to '{output_csv_path}'.")
