#!/usr/bin/python
import csv

def checkLength(column, readFile, writeFile, maxLen):
    counter = 0
    i = 0
    idxSplitItems = []
    final = []
    newSplits = 0
    with open(readFile,'r', encoding="utf8", newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        your_list = removeUnwanted(your_list, column)
        final = your_list
        print(final)

        for sublist in your_list:
            #del sublist[-1]    -remove last invisible element
            i+=1
            if len(final[i-1][column]) > maxLen:
                counter += 1 # Number of large
                idxSplitItems.append(split_bylen(i,final[i-1][column],maxLen))
                #if len(idxSplitItems) > newSplits: newSplits = len(idxSplitItems)
                final[i-1][column] = split_bylen(i,final[i-1][column],maxLen)[1]
            else:
                idxSplitItems.append(i)
            print("After split final: "+ final[i-1][column])   

    writeSplitToCSV(writeFile, final)
    checkCols(final, 6)
    return final, idxSplitItems

def removeUnwanted(data, column):
    i = 0
    print("----------------------------------------")
    for sublist in data:
        i+=1
        data[i-1][column] = sublist[column].replace(",","")
        print(data[i-1][column])
    return data



def split_bylen(index, item, maxLen):
    splitList = [item[ind:ind+maxLen] for ind in range(0, len(item), maxLen)]
    splitList.insert(0,index)
    print(item)
    return splitList

def writeSplitToCSV(writeFile,data):
    with open(writeFile,'w', encoding="utf8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def split_bylen (index, item, maxLen):
    splitList = [item[ind:ind+maxLen] for ind in range(0, len(item), maxLen)]
    splitList.insert(0,index)
    print(item)
    return splitList

def split_bylen(index, item, maxLen):
    splitList = [item[ind:ind+maxLen] for ind in range(0, len(item), maxLen)]
    splitList.insert(0,index)
    print(item)
    return splitList

def checkCols(data, columns):
    for sublist in data:
        if len(sublist)-1!=columns:
            print ("[X] This row doesnt have the same amount of columns as others: "+sublist)
        else:
            print("All okay")

#len(data) #how many split items
#print(your_list[0][0])
#print("Number of large: ", counter)

final, idxSplitItems = checkLength(0,'test.csv','final.csv', 30)
print("------------------------")
print(idxSplitItems)
print("-------------------------")
print(final)