
import csv
import pandas as pd
import mysql.connector as mc

# """ 配置数据库 """
# HOST='localhost'
# PORT='3306'
# USERNAME='root'
# PASSWORD='xblshxg'
# DATABASE='program'


def get_longest_value_from_col(filename, column_name):
       with open(filename, 'r') as csvfile:
              reader = csv.DictReader(csvfile)
              longest_name = max([row[column_name] for row in reader], key=len)
       return len(longest_name) + 7

class global_value():
       table_name = []

class csv2Mysql(object):
       # 定义一个init方法，用于读取数据库
       def __init__(self):
              # 读取数据库和建立游标对象
              self.connect = mc.connect(host="localhost",
                                             port=3306, 
                                             user="root", 
                                             password="xblshxg", 
                                             database="program"# ,
                                             # charset="utf8"
                                             )
              self.cursor = self.connect.cursor()
              print("initialized!")
       
       # 定义一个del类，用于运行完所有程序的时候关闭数据库和游标对象
       def __del__(self):
              self.connect.close()
              self.cursor.close()
              print("deleted!")

       # 定义一个确认事务运行
       def commit(self):
              self.connect.commit()

       # 定义一个创建表的方法
       def create_table(self, df, address):
              # 若已有数据表weather_year_db，则删除
              global_value.table_name = input("How would you like to name your table? :)")
              query = "DROP TABLE IF EXISTS `{}`;".format(global_value.table_name)
              self.cursor.execute(query)
              # 构造语句创建表
              sql = "CREATE TABLE `{}` ( ".format(global_value.table_name)
              for i in range (len(list(df.columns))):
                     dtype = "init"
                     if list(df.dtypes)[i] == "int64": dtype = dtype.replace("init", "INT")
                     if list(df.dtypes)[i] == "O": 
                            dtype = dtype.replace("init", "VARCHAR({})".format(get_longest_value_from_col(address, list(df.columns)[i])))
                     if list(df.dtypes)[i] == "float64": dtype = dtype.replace("init", "FLOAT")
                     part = "`{}` {}, ".format(list(df.columns)[i], dtype)
                     sql = "".join([sql, part])
              sql = " ".join([sql,"PRIMARY KEY (`{}`));".format(list(df.columns)[0])])
              self.cursor.execute(sql)
              self.commit()
              print("create_table succeed!")
       
       def write_mysql(self, df):
              for i in range(len(df)):
                     sql = "INSERT INTO `" + global_value.table_name + "` VALUES{};".format(tuple(df.iloc[i]))
                     self.cursor.execute(sql)
                     self.commit()
              print("write_mysql succeed!")

