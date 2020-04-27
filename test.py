import openpyxl

# читаем excel-файл
wb = openpyxl.load_workbook('klass.xlsx')

# печатаем список листов
sheets = wb.sheetnames
for sheet in sheets:
    print(sheet)

# получаем активный лист
sheet = wb.active

# печатаем значение ячейки A1
s=(sheet['A1'].value)
w=(sheet['A2'].value)
w=str(w)
s=str(s)
print(s ,"",w  )
# печатаем значение ячейки B1
