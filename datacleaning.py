import pandas as pd

train = "D:\\Programing\\VSCodeCprojects\\git_workspace\\Titanic\\train.csv"
test = "D:\\Programing\\VSCodeCprojects\\git_workspace\\Titanic\\test.csv"
df = pd.read_csv(train)
df_t = pd.read_csv(test)

df.describe(include=['O']).transpose()

# Drop unnecessary columns
cols = ['column_name','column_name','column_name']
df.drop(cols, inplace=True, axis=1)

# Show first five rows of it
# df.head()

# Check for missing values
df.isnull().sum()
without_NULL = df.fillna('NULL')

# Check data types
df.dtypes
df['column_name'] = pd.to_datetime(df['column_name'])
df = df.astype({'column_name':'datatype','column_name':'datatype','column_name':'datatype'})

# Show csv header
list(df.columns)
list(df.dtypes)

# Convert all rows into a list of tuples
y = []
for i in range(len(df)):
       x = tuple(df.iloc[i])
       y.append(x)


