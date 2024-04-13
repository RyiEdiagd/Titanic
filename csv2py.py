import pandas as pd

df = pd.read_csv('train.csv')

# Drop unnecessary columns
cols = ['column_name','column_name','column_name']
df.drop(cols, inplace=True, axis=1)

# Show first five rows of it
# df.head()

# Check for missing values
df.isnull().sum()
df.fillna('NULL')

# Check data types
df.types
df['column_name'] = pd.to_datetime(df['column_name'])
df = df.astype({'column_name':'datatype','column_name':'datatype','column_name':'datatype'})

# Convert all rows into a list of tuples
y = []
for i in range(len(df)):
       x = tuple(df.iloc[i])
       y.append(x)


