# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
from pandas import DataFrame, Series
import pandas as pd
import traceback
import os

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))
#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
def excel_table_byindex(file,colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):

         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i] 
             list.append(app)
    return list

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file,colnameindex=0,by_name=u'data'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

def main():
    totaldata =[]
    #AtableA=["All5.xls","All6.xls","All7.xls"]
    path="D:\\Python\\美剧天堂\\初次数据xls\\"
    #info="D:\Python\数据爬虫\800-1000" #input("请输入要列举文件的目录：(如D:\\temp)")
    listfile=os.listdir(path)
    print(listfile)
    for t in listfile:
        temp_tables = excel_table_byindex(path+t)
        for row in temp_tables:
            totaldata.append(row)
    print(len(totaldata))
    pdaa = pd.DataFrame(totaldata)
    #pdaa.columns = ["IDS","Link","Name", "Mobile", "Province", "City","Address","Tel","CreateDate"]
    pdaa.to_csv("all.csv")
    
if __name__=="__main__":
    main()
