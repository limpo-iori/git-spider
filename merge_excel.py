import xlwt
import xlrd
import os
path = r'C:\Users\WZKJ\Desktop\file_list'
file_list = os.listdir(path)
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('merge',cell_overwrite_ok=True)
x_cursor = 0
for file in file_list:
	file_data = xlrd.open_workbook(os.path.join(path,file))
	file_sheet = file_data.sheet_by_index(0)
	nrow = file_sheet.nrows
	ncol = file_sheet.ncols
	for row in range(nrow-1):
		for col in range(ncol):
			worksheet.write(row+x_cursor,col,file_sheet.cell(row+1,col).value)
	x_cursor = x_cursor+row
workbook.save('merge.xls')