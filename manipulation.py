import pandas as pd


OG_PATH = "og.csv"
BETWEEN_CELLS_SPLIT = "      "
INNER_CELL_SPLIT = " "
df = pd.read_csv(OG_PATH, index_col=0)

# Access the first data cell
first_data_cell = df.iloc[1, 2].split(BETWEEN_CELLS_SPLIT)
print("First data cell:", first_data_cell)

# Print the column headers
print("Column headers:", df.columns.tolist())

# Print the row headers
print("Row headers:", df.index.tolist())

# loop through the data cells
for i in range(0, len(df.index)):
    for j in range(0, len(df.columns)):
        content = df.iloc[i, j].split(BETWEEN_CELLS_SPLIT)
        for subject in content:
            subject = subject.split(INNER_CELL_SPLIT)
            # remove empty strings
            subject = list(filter(None, subject))
            print("Row:", i, "Column:", j, "Subject:", subject)
            break
