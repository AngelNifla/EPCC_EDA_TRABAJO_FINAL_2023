import pandas as pd

# Replace 'your_dataset.xlsx' with the actual path to your dataset
input_file_path = 'Files/covid_DB.xlsx'

# Read the dataset into a pandas DataFrame
df = pd.read_excel(input_file_path)

# Select the desired columns
selected_columns = ["Patient ID", "SARS-Cov-2 exam result", "Patient age quantile", 
                    "Hematocrit", "Platelets", "Mean platelet volume ", 
                    "Mean corpuscular hemoglobin concentration (MCHC)", 
                    "Leukocytes", "Basophils", "Eosinophils", "Monocytes", 
                    "Proteina C reativa mg/dL"]

df_selected = df[selected_columns]

# Rename columns for simplicity
column_mapping = {
    "Patient ID": "ID",
    "SARS-Cov-2 exam result": "SARS-Cov-2 test result",
    "Mean corpuscular hemoglobin concentration (MCHC)": "Mean corpuscular concentration (MCHC)",
    "Proteina C reativa mg/dL": "Proteina C reativa mg/dL"
}

df_selected = df_selected.rename(columns=column_mapping)

# Write the selected columns to a new CSV file
output_file_path = 'FetchedData.csv'
df_selected.to_csv(output_file_path, index=False)

print(f"Selected columns saved to {output_file_path}")
