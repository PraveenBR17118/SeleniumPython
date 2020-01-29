'''
Created on 22-Jan-2020

@author: praveen
'''


import openpyxl as opp

path = "/Users/praveen/Documents/Eclipse Project/PythonAutomation/SeleniumPython/DATA/DDT3.xlsx"

workbook = opp.load_workbook(path)

#sheet = workbook.active  

sheet = workbook.get_sheet_by_name("Sheet1")

for r in range(1,6):
    for c in range(1,4):
        sheet.cell(row=r,column=c).value = "Pogo"
        
        
workbook.save(path)