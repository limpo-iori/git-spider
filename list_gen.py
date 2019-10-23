import xlrd
import xlwt

path = 'model.xlsx'
file_data = xlrd.open_workbook(path)
file_sheet = file_data.sheet_by_index(0)
nrows = file_sheet.nrows
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('good_list',cell_overwrite_ok=True)
x = 0
for row in range(nrows):
	package = file_sheet.cell(row,0).value
	number = file_sheet.cell(row,1).value
	name = file_sheet.cell(row,2).value
	print("生成第"+str(int(number))+"数据")
	for k in range(int(number)):
		worksheet.write(k+x,0,package)
		worksheet.write(k+x,1,name)
	x = x+k+1
workbook.save('good_list.xls')