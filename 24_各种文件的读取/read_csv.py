import csv

# 读取csv文件
myfile = "data_csv.csv"
data = csv.reader(open(myfile, "r"))

for user in data:
    print(user)

print("=======================")
# 读取txt
with open("data_txt.txt", "r") as f:
    # data = f.read()
    # print(data)
    # data1 = f.readline()
    # print(data1)
    # 把所有的数据都读取出来，放在一个列表中
    data2 = f.readlines()
    print(data2)

print("=======================")
# 读取xls文件
import xlrd
import xlwt

# 打开文件
file_data = xlrd.open_workbook('bbb.xlsx')
# 获取一个工作表
table_file = file_data.sheets()[0]
# print(table_file)
# print(table_file.name)
print(file_data.sheet_names())
# 行和列
rows = table_file.nrows
cols = table_file.ncols
print(rows)
print(cols)
# 第一行的描述内容
first_name = table_file.row_values(0)
print(first_name)
li = []
# 从第2行开始往后取数据
for row_num in range(1, rows):
    # 把每行的数据取出来
    row_contect = table_file.row_values(row_num)
    if row_contect:
        app = {}
        for i in range(len(first_name)):
            # 把每行的数据以键值对的方式存起来，放在字典中
            app[first_name[i]] = row_contect[i]
        print(app)
        # 把字典中的数据添加到一个列表中,列表中存放一个个的字典
        li.append(app)

print("-----------")
print(li)
print("-----------")
for con in li:
    print(con)
