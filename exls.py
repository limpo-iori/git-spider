import xlrd
import xlwt
# 打开数据表
def rd_wt_one_table(table,sheet_name,file_name):
    nrows = table.nrows
    ncols = table.ncols
    workbook = xlwt.Workbook(encoding = 'utf-8')
    worksheet = workbook.add_sheet(sheet_name)
    for row in range(nrows):
        for col in range(ncols):
            worksheet.write(row,col,table.cell(row,col).value)
    gat_workbook.save(file_name)
    print(file_name+'写入成功')

def rd_wt_two_table(header_table,body_table,header_sheet_name,body_sheet_name,file_name):
    header_nrows = header_table.nrows
    header_ncols = header_table.ncols

    body_nrows = body_table.nrows
    body_ncols = body_table.ncols

    workbook = xlwt.Workbook(encoding = 'utf-8')
    header_worksheet = order_workbook.add_sheet('header_sheet_name')
    body_worksheet = order_workbook.add_sheet('body_sheet_name')

    # 订单表头读写
    for row in range(header_nrows):
        for col in range(header_ncols):
            header_worksheet.write(row,col,header_table.cell(row,col).value)
    print(header_sheet_name+'写入成功')

    # 订单表体读写
    for row in range(body_nrows):
        for col in range(body_ncols):
            body_worksheet.write(row,col,body_table.cell(row,col).value)
    print(body_sheet_name+'写入成功')

    workbook.save(file_name)
    print(file_name+'写入成功')

if __name__ == '__main__':
    data = xlrd.open_workbook('出口总模板.xlsx')
    # 读取收款单
    gathering_table = data.sheet_by_name('收款单')
    # 读取出口运单
    exprot_table = data.sheet_by_name('出口运单')
    # 读取订单表头
    order_header_table = data.sheet_by_name('订单表头')
    # 读取订单表体
    order_body_table = data.sheet_by_name('订单表体')
    # 读取清单表头
    list_header_table = data.sheet_by_name('出口清单表头')
    # 读取清单表体
    list_body_table = data.sheet_by_name('出口清单表体')
    # 读取清单总分单表头
    list_sum_header_table = data.sheet_by_name('清单总分单表头')
    # 读取订单总分单表体
    list_sum_body_table = data.sheet_by_name('清单总分单表体')

    rd_wt_one_table(gathering_table,'收款单','收款单.xls')
    rd_wt_one_table(exprot_table,'出口运单','出口运单.xls')
    rd_wt_two_table(order_header_table,order_body_table,'订单表头','订单表体','订单.xls')
    rd_wt_two_table(list_header_table,list_body_table,'出口清单表头','出口清单表头','清单.xls')
    rd_wt_two_table(order_header_table,order_body_table,'清单总分单表头','清单总分单表头','清单总分单.xls')


# # 收款单读取写入
# gat_nrows = gathering_table.nrows
# gat_ncols = gathering_table.ncols
# gat_workbook = xlwt.Workbook(encoding = 'utf-8')
# gat_worksheet = gat_workbook.add_sheet('收款单')
# for row in range(gat_nrows):
#     for col in range(gat_ncols):
#         gat_worksheet.write(row,col,gathering_table.cell(row,col).value)
# gat_workbook.save('收款单.xls')
# print('收款单写入成功')


# # 出口运单读取写入
# exp_nrows = exprot_table.nrows
# exp_ncols = exprot_table.ncols
# exp_workbook = xlwt.Workbook(encoding = 'utf-8')
# exp_worksheet = exp_workbook.add_sheet('出口运单')
# for row in range(exp_nrows):
#     for col in range(exp_ncols):
#         exp_worksheet.write(row,col,exprot_table.cell(row,col).value)
# exp_workbook.save('出口运单.xls')
# print('出口运单写入成功')


# # 订单读取写入
# order_header_nrows = order_header_table.nrows
# order_header_ncols = order_header_table.ncols

# order_body_nrows = order_body_table.nrows
# order_body_ncols = order_body_table.ncols

# order_workbook = xlwt.Workbook(encoding = 'utf-8')
# order_header_worksheet = order_workbook.add_sheet('订单表头')
# order_body_worksheet = order_workbook.add_sheet('订单表体')

# # 订单表头读写
# for row in range(order_header_nrows):
#     for col in range(order_header_ncols):
#         order_header_worksheet.write(row,col,order_header_table.cell(row,col).value)
# print('订单表头写入成功')

# # 订单表体读写
# for row in range(order_body_nrows):
#     for col in range(order_body_ncols):
#         order_body_worksheet.write(row,col,order_body_table.cell(row,col).value)
# print('订单表体写入成功')

# order_workbook.save('订单.xls')
# print('订单写入成功')


# # 清单读取写入
# list_header_nrows = list_header_table.nrows
# list_header_ncols = list_header_table.ncols

# list_body_nrows = list_body_table.nrows
# list_body_ncols = list_body_table.ncols

# list_workbook = xlwt.Workbook(encoding = 'utf-8')
# list_header_worksheet = list_workbook.add_sheet('清单表头')
# list_body_worksheet = list_workbook.add_sheet('清单表体')

# # 清单表头读写
# for row in range(list_header_nrows):
#     for col in range(list_header_ncols):
#         list_header_worksheet.write(row,col,list_header_table.cell(row,col).value)
# print('清单表头写入成功')

# # 清单表体读写
# for row in range(list_body_nrows):
#     for col in range(list_body_ncols):
#         list_body_worksheet.write(row,col,list_body_table.cell(row,col).value)
# print('清单表体写入成功')

# list_workbook.save('清单.xls')
# print('清单写入成功')


# # 清单总分单读取写入
# list_sum_header_nrows = list_sum_header_table.nrows
# list_sum_header_ncols = list_sum_header_table.ncols

# list_sum_body_nrows = list_sum_body_table.nrows
# list_sum_body_ncols = list_sum_body_table.ncols

# list_sum_workbook = xlwt.Workbook(encoding = 'utf-8')
# list_sum_header_worksheet = list_sum_workbook.add_sheet('清单总分单表头')
# list_sum_body_worksheet = list_sum_workbook.add_sheet('清单总分单表体')

# # 清单总分单表头读写
# for row in range(list_sum_header_nrows):
#     for col in range(list_sum_header_ncols):
#         list_sum_header_worksheet.write(row,col,list_sum_header_table.cell(row,col).value)
# print('清单总分单表头写入成功')

# # 清单总分单表体读写
# for row in range(list_sum_body_nrows):
#     for col in range(list_sum_body_ncols):
#         list_sum_body_worksheet.write(row,col,list_sum_body_table.cell(row,col).value)
# print('清单总分单表体写入成功')

# list_sum_workbook.save('清单总分单.xls')
# print('清单总分单写入成功')