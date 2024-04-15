
import pandas as pd
import csv2py_class as cc

train = "D:\\Programing\\VSCodeCprojects\\git_workspace\\Titanic\\train.csv"
df = pd.read_csv(train)

# We already know that column Age, Cabin and Embarked missing value
df['Age'] = df['Age'].fillna(0)
df['Cabin'] = df['Cabin'].fillna('Missing')
df['Embarked'] = df['Embarked'].fillna('Missing')

cc.csv2Mysql().create_table(df, train)
cc.csv2Mysql().write_mysql(df)