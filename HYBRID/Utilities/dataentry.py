import openpyxl
def read_details(file_path):

    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook["Sheet1"]

    rows = sheet.max_row
    data = []

    for r in range(2, rows + 1):

        street1 = sheet.cell(r, 3).value
        stree2 = sheet.cell(r, 4).value
        city = sheet.cell(r, 5).value

        data.append((street1, stree2,city))

    return data