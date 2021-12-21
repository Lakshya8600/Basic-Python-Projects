import xlwt
import datetime

date = datetime.date.today()

if __name__ == "__main__":
    i = 3
    sheet = xlwt.Workbook()
    shet = sheet.add_sheet("pysheet")
    style = xlwt.easyxf("font: bold 1")

    shet.write(1, 1, "OPENING STOCK", style)
    shet.write(2, 1, "Quantity", style)
    shet.write(2, 2, "Rate", style)
    shet.write(2, 3, "Amount", style)

    shet.write(1, 5, "PURCHASE", style)
    shet.write(2, 5, "Quantity", style)
    shet.write(2, 6, "Rate", style)
    shet.write(2, 7, "Amount", style)

    shet.write(1, 9, "SALE", style)
    shet.write(2, 9, "Quantity", style)
    shet.write(2, 10, "Rate", style)
    shet.write(2, 11, "Amount", style)

    shet.write(1, 13, "CLOSING STOCK", style)
    shet.write(2, 13, "Quantity", style)
    shet.write(2, 14, "Rate", style)
    shet.write(2, 15, "Amount", style)
    while True:
        print("enter product name")
        input12 = input()
        shet.write(i,0,input12,style)

        print("Enter quantity and rate for Opening Stock of", input12, "respectively")
        input13 = int(input("Quantity - "))
        input23 = int(input("Rate - "))
        amo1 = input13 * input23
        shet.write(i,1,input13)
        shet.write(i,2,input23)
        shet.write(i,3,amo1)

        print("Enter quantity and rate for purchase of", input12, "respectively")
        input14 = int(input("Quantity - "))
        input24 = int(input("Rate - "))
        amo2 = input14 * input24
        shet.write(i, 5, input14)
        shet.write(i, 6, input24)
        shet.write(i, 7, amo2)

        print("Enter quantity and rate for sale of", input12, "respectively")
        input15 = int(input("Quantity - "))
        input25 = int(input("Rate - "))
        amo3 = input15 * input25
        shet.write(i, 9, input15)
        shet.write(i, 10, input25)
        shet.write(i, 11, amo3)

        CSA = (amo1 + amo2) - amo3
        CSQ = (input13 + input14) - input15
        CSR = (input23 + input24) - input25
        shet.write(i, 13, CSQ)
        shet.write(i, 14, CSR)
        shet.write(i, 15, CSA)
        print()

        i += 2
        sheet.save("123.xls")
