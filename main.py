"""
Augustini generator

MT - 10665  MT - 11665   MT - 12665 MT - 13665   
MT - 10665  MT - 11665   MT - 12665 MT - 13665


* 117
konec, konec, konec, konec, konec
"""

import csv
from itertools import zip_longest

################################ Augustini generator ##########################################
def generateCSV (name,stup1,stup2,stup3,stup4):
    #Open file to export to
    export_file_path = str(name)+".csv"
    exceldata = [stup1, stup2, stup3, stup4]
    export_data = zip_longest(*exceldata, fillvalue='')

    with open(export_file_path, mode='w+',encoding='utf8', newline='') as barcode_file:
        barcode_writer = csv.writer(barcode_file, quoting=csv.QUOTE_NONE)
        barcode_writer.writerows(export_data)

def generateSeq (starting,maxnum,itter,name):
    #obj = [[] for i in range(4)]
    #obj[1].append('xx')
    stup1 = []
    stup2 = []
    stup3 = []
    stup4 = []
    #stup5 = []
    n1,n2,n3,n4 = starting+1,starting+maxnum+1,starting+maxnum*2+1,starting+maxnum*3+1

    for i in range (maxnum):
        for j in range (itter):
            stup1.append('SPM - {:05d}'.format(n1))

            stup2.append('SPM - {:05d}'.format(n2))

            stup3.append('SPM - {:05d}'.format(n3))

            #stup4.append('SPM - %d' % n4)
            stup4.append('')

        stup1.append("konec")
        stup2.append("konec")
        stup3.append("konec")
        stup4.append("konec")
        #stup5.append("konec")
        n1,n2,n3,n4 = n1+1,n2+1,n3+1,n4+1

    generateCSV(name,stup1,stup2,stup3,stup4)
    #return stup1,stup2,stup3,stup4,stup5

def startProgram():
    starting = int(input("Input number: "))
    for i in range(1):
        if i != 2:
            generateSeq(starting,120,2620,i)
            starting += 4000
            #generateCSV(x,stup1,stup2,stup3,stup4,stup5)
        else: 
            generateSeq(starting,500,117,i)
    
startProgram()

# import csv

# def generate_csv(name, data):
#     with open(f"{name}.csv", mode="w+", encoding="utf-8", newline="") as csv_file:
#         writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE)
#         writer.writerows(data)

# def generate_sequence(starting, maxnum, itter):
#     n1, n2, n3, n4 = starting+1, starting+maxnum+1, starting+maxnum*2+1, starting+maxnum*3+1
#     data = []
#     for i in range(maxnum):
#         row = [f"ST - {n1}"] * itter + ["konec"]
#         data.append(row)
#         row = [f"ST - {n2}"] * itter + ["konec"]
#         data.append(row)
#         row = [f"ST - {n3}"] * itter + ["konec"]
#         data.append(row)
#         row = [f"MT - {n4}"] * itter + ["konec"]
#         data.append(row)
#         row = [""] * (itter+1)
#         data.append(row)
#         n1 += 1
#         n2 += 1
#         n3 += 1
#         n4 += 1
#     return data

# def start_program():
#     starting = int(input("Input number: "))
#     data = []
#     for i in range(3):
#         if i != 2:
#             data += generate_sequence(starting, 1000, 500)
#             starting += 4000
#         else:
#             data += generate_sequence(starting, 500, 117)
#     generate_csv("output", data)

# start_program()
