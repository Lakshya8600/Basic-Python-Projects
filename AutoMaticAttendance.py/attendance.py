import xlwt 
from xlwt import Workbook 

Total = open("Total.txt","rt")
Present = open("Present.txt","rt")
TotalList = []
PresentList = []

Counter = 0
Content = Total.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1

Total.close()
Total = open("Total.txt","rt")

for index in range(Counter):
    name = Total.readline()
    name = name.lower()
    TotalList.append(name)


Counter = 0
Content = Present.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1

Present.close()
Present = open("Present.txt","rt")
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
i = 0

for index in range(Counter):
    name = Present.readline()
    name = name.lower()
    PresentList.append(name)

for TotalST in TotalList:
    for PresentST in PresentList:
        if PresentST in TotalST:
            sheet1.write(i,0,'P')
            break
    i += 1


 
wb.save('Attendance.xls')
