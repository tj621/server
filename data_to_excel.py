
import xlrd
import xlwt

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

def close_excel(file='file.xls'):
    return 'd'
def excel_table_byindex(sheet_index=0,row_number=1):
    file = ''
    data = open_excel(file)
    table = data.sheets()[sheet_index,]
    nrows = table.nrows
    ncols = table.ncols
    title_names=table.row_values(0)
    print nrows
    print ncols
    print title_names

def match_table_title(property):
    return 'a'