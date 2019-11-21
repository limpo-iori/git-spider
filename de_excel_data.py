import openpyxl


def read_data(file_name):
    test_xlsx = openpyxl.load_workbook(file_name)
    test_data = test_xlsx.active
    name_list = []
    val_list = []
    for row in test_data.rows:
        name_list.append(row[0].value)
        val_list.append(row[1].value)
    return name_list, val_list


def de_name_list(name_list):
    de_name = []
    for l in name_list:
        if l not in de_name:
            de_name.append(l)
    return de_name


def de_val_sum(name_list, val_list, set_name_list):
    val = 0
    de_val = []
    for s in set_name_list:
        for i in range(len(name_list)):
            if name_list[i] == s:
                val += val_list[i]
        de_val.append(val)
        val = 0
    return de_val


name_list, val_list = read_data('test.xlsx')
de_name = de_name_list(name_list)
de_val = de_val_sum(name_list, val_list, de_name)
print(de_name)
print(de_val)
