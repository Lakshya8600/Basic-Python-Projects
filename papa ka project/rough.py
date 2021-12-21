import xlwt

sheet = xlwt.Workbook()
shet = sheet.add_sheet("pysheet")

style = xlwt.easyxf("font: bold 1")
shet.write(2,2,"world", a)
shet.write(1,1,"hello")
sheet.save("123.xls")

