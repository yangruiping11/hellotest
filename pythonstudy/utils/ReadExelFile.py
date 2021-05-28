import xlrd
import json
'''
主要是学习python读取Excel
'''
if __name__ == '__main__':

    file_name = 'C:\\Users\\17996\\Desktop\\test.xls'
    #读取指定文件
    file = xlrd.open_workbook(file_name)

    #打印出文件有多少个sheets
    count = len(file.sheets())
    print(count)

    table = file.sheets()[0]
    #有几行
    nrows = table.nrows
    #几列
    ncols = table.ncols

    print(format('表示数据的行列为 %d ,%d'%(nrows,ncols)))

    for i in range(1,nrows):
        rowValues = table.row_values(i)
        url = rowValues[1]
        print(url)
        param = rowValues[3]
        print(param)

        url = table
