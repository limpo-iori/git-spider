import xlrd
import xlwt

#单表格读写
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

#双表格读写
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
    # 打开数据表
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
