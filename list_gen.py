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
	price = file_sheet.cell(row,3).value
	for k in range(int(number)):
		worksheet.write(k+x,0,package)
		worksheet.write(k+x,1,name)
		worksheet.write(k+x,2,price)
	x = x+k+1
	print('包号：'+package+'，数据生成成功')
print('数据生成完毕，共计:'+str(x))
workbook.save('good_list.xls')