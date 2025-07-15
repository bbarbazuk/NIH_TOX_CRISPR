import pandas as pd

# Config
filtered_csv_path = ""        
sample_names_path = ""        
output_filtered_csv = ""      

# Read sample names to target (e.g., liver samples)
with open(sample_names_path, "r") as f:
    target_samples = set(line.strip() for line in f if line.strip())

# Load the previously filtered gene dataframe
df = pd.read_csv(filtered_csv_path)

# Always keep the first column (gene names or IDs)
first_col = df.columns[0]

# Determine which columns to retain: first column + any that match target sample names
columns_to_keep = [col for col in df.columns if col == first_col or col in target_samples]

# Filter the DataFrame
filtered_df = df[columns_to_keep]

# Save to new CSV
filtered_df.to_csv(output_filtered_csv, index=False)

print(f"Filtered DataFrame with {len(columns_to_keep)-1} liver sample columns saved to '{output_filtered_csv}'.")

