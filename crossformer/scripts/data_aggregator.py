import pandas as pd
import os

# Define the input file path
input_file = '/Users/md/Library/CloudStorage/OneDrive-Personal/Mohit/RIT/trading/codebases/stockPredict/time_series_benchmarking/crossformer/Data shared/15 May 2024/2023_selected_50/train/AKAM.csv'

# Define the output folder path
output_folder = '/Users/md/Library/CloudStorage/OneDrive-Personal/Mohit/RIT/trading/codebases/stockPredict/time_series_benchmarking/crossformer/OriginalPaperCode/datasets/My Data'

# Define the columns to be filtered
columns_to_filter = ['date', 'VOL_CHANGE','BA_SPREAD','ILLIQUIDITY','sprtrn','TURNOVER', 'RET']

# Read the data from the input file
data = pd.read_csv(input_file)

# Filter the desired columns
filtered_data = data[columns_to_filter]

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Generate a unique filename for the output file
output_file = os.path.join(output_folder, 'AKAM_filtered_data.csv')

# Save the filtered data to the output file
filtered_data.to_csv(output_file, index=False)

print('Filtered data saved successfully.')