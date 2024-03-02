import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('./output.csv')

# Convert the percentage data to float and calculate row-wise average
df['Average'] = df.iloc[:, 1:-1].apply(lambda x: x.str.rstrip('%').astype(float).mean(), axis=1)

# Convert the average back to percentage format
df['Average'] = df['Average'].apply(lambda x: f"{x:.2f}%")

# Sort the DataFrame based on the average score in descending order
df_sorted = df.sort_values(by='Average', ascending=False, key=lambda x: x.str.rstrip('%').astype(float))

# Display the sorted DataFrame
print(df_sorted['model/task'].to_list())

print(df_sorted['Average'].apply(lambda x: float(x.rstrip('%'))).to_list())

print(df_sorted['type'].to_list())

# Display the DataFrame with the added average column
# df[['model/task', 'Average']]
df_sorted.to_csv("output_avg.csv", index=False)