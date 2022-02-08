import pandas as pd
import csv
import numpy
import os
'''
df= pd.read_csv('uskrs.csv', usecols=['ime'])
#for line in df:
 #   if len(line)>20:
  #      print (line)
df.head()

with open("uskrs.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for lines in csv_reader:
      print(lines[0])

with pd.read_csv('uskrs.csv', delimiter=',',usecols=[0]) as df:
    for line in df:
        print (line)
'''
print("-------------------------------------------------------")

'''Example csv containing

long string with some special characters , number, string, number
long string with some special characters , number, string, number
long string with some special characters , number, string, number
long string with some special characters , number, string, number

'''
'''
def newopenfile(fileName, maxCollumnLength, lineNum, splitString):
    with open(fileName, 'rw', encoding="utf8") as nf:
        writer = csv.writer(fileName, quoting=csv.QUOTE_NONE)
        for i in range(0, maxCollumnLength-1):
            #write whitespace until reaching lineNum of a string thats bigger then 20 then write that part of the string to a csv
'''

fileName = 'uskrs.csv'
firstColList=[]         #an empty list to store the second column
splitString=[]
i = 0
counter = 0
with open(fileName, 'r', encoding="utf8") as rf:
    reader = csv.reader(rf, delimiter=',')
    for row in reader:
        i+=1
        if len(row[1]) > 30:
            print(i)
            counter+= 1
            print(row[1])
            #split row and parse the other end of the row to newopenfile(fileName, len(reader), i, splitString )
            #print(row[0])
        #for debuging    
        
        firstColList.append(row[0])  
print (counter)

    
#print([x for x in noise_amp if len(x)>40])
#print(len(noise_amp))