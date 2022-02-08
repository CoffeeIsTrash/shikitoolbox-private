'''
import os,csv


def barcsvgen(x,y,barcode):
    with open(barcode + '.csv', mode='w+', newline='') as barcode_file:
        barcode_writer = csv.writer(barcode_file, quoting=csv.QUOTE_NONE)
        for i in range(x,y+1):
            barcode_writer.writerow([i])
            print(i)
barcode = input("Naziv file-a: ")
x = int(input("Pocetni broj: "))
y = int(input("Krajnji broj: "))
barcsvgen(x,y, barcode)

'''
import pandas as pd
import csv
splitData = [1, 
            2, 
            3, 
            4, 
            5, 
            [6, 'DOPI d.o.o. za poslovno savjet', 'ovanje'], 
            [7, 'S.K.A.B. TRANSPORT TRGOVINA I ', 'UGOSTITELJSTVO'], 
            8, 
            [9, 'Baltic-Adriatic društvo s ogra', 'ničenom odgovornošću za usluge'], 
            10, 
            11, 
            12, 
            13, 
            14, 
            15, 
            16, 
            17, 
            18, 
            19]

maxSplit = 2 # biggest number of split items

for i in range (2,maxSplit):
    fileName = column+'_'+i+'_'+writeFile
    with open(fileName, mode='w+', newline='') as csv_files:
        for sublist in splitData:
            if isinstance(sublist, list):
                print(sublist[i]+',')
            else:
                print(",")


with open(writeFile,'w', encoding="utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)



'''
def populateFiles(numOF, writeFile, splitData):
    for i in range(0,len(splitData):
        if isinstance(splitData[i], list):
            for j in range(2,numOF+1):
            with open(i+j+writeFile + '.csv', mode='w+', newline='') as csv_files:
                csv_writer = csv.writer(csv_files, quoting=csv.QUOTE_NONE)
                csv_writer.writerow([splitData[i][j]])
        else:
            csv_writer.writerow([''])
'''  
'''      
def populateFiles(numOF, writeFile, splitData, column):
    for i in range(2,numOF+1):
        fileName = column+'_'+i+'_'+writeFile
        with open(fileName, mode='w+', newline='') as csv_files:
            csv_writer = csv.writer(csv_files)
            for j in range(0,len(splitData)):
                if isinstance(splitData[i], list):
                    csv_writer.writerow([splitData[i][j]])
                else:
                    csv_writer.writerow([''])

populateFiles(2, 'final.csv', splitData, 1)
'''
''' 

splitData = [1, 
            2, 
            3, 
            4, 
            5, 
            [6, 'DOPI d.o.o. za poslovno savjet', 'ovanje'], 
            [7, 'S.K.A.B. TRANSPORT TRGOVINA I ', 'UGOSTITELJSTVO'], 
            8, 
            [9, 'Baltic-Adriatic društvo s ogra', 'ničenom odgovornošću za usluge'], 
            10, 
            11, 
            12, 
            13, 
            14, 
            15, 
            16, 
            17, 
            18, 
            19]

column = 1
writeFile = 'name.csv'
numOF = 3

populateFiles(numOF, writeFile, splitData, column):

za svaki i od 2 do 3+1:
    i = 2:
        writeFile = 1_2_name.csv
        with open file writeFile:






i loop:



1.   open file 

for every 
    [6, 'DOPI d.o.o. za poslovno savjet', 'ovanje'],
    [7, 'S.K.A.B. TRANSPORT TRGOVINA I ', 'UGOSTITELJSTVO']
    





    j loop:

    for every
        stepStart = 0
        stepEnd = splitData[i][j-1]
        6, 
        'DOPI d.o.o. za poslovno savjet',  
        'ovanje'
        
        create file with row+column+fileName+csv  
        while stepStart != stepEnd:

        writerow[j]
'''
