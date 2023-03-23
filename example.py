import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Chicago', 'San Francisco']
})

with open("file.csv","w") as file1:
    file1.re
print(df)
# Iterate over the rows of the DataFrame using iterrows()
for index, row in df.iterrows():
    print('Index:', index)
    print('Row data:')
    print(row)
    print('Name:', row['Name'])
    print('Age:', row['Age'])
    print('City:', row['City'])
    print('---')