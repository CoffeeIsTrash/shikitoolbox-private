
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os, csv
import pandas as pd


print('--------------------------------------------------------')
#Init TkinterGui
root = Tk()

final, idxSplitItems = [], []
newSplits = 0

#Title
titleLabel = Label(root, text="Shiki toolbox", bg="red", fg="white")
titleLabel.pack(fill=X)



#-----------------------------------DEFS---------------------------------
################################### SPLITTING PART OF THE CODE FUNCTIONS ##########################

def checkLength():

    counter = 0
    i = 0
    global idxSplitItems
    global final
    global newSplits
    
    column = columnNum.get()
    readFile = filedialog.askopenfilename()
    maxLen = lenNum.get()
    writeFile = filedialog.asksaveasfilename(defaultextension='.csv')

    with open(readFile,'r', encoding="utf8", newline='') as f:
        reader = csv.reader(f)
        your_list = list(reader)
        your_list = removeUnwanted(your_list, column)
        final = your_list
        #print(final)

        for sublist in your_list:
            #del sublist[-1]    -remove last invisible element
            i+=1

            if len(final[i-1][column]) > maxLen:
                counter += 1 # Number of large
                idxSplitItems.append(split_bylen(i,final[i-1][column],maxLen))
                final[i-1][column] = split_bylen(i,final[i-1][column],maxLen)[1]

            else:
                idxSplitItems.append(i)

            #print("After split final: "+ final[i-1][column])   

    print (idxSplitItems)
    writeSplitToCSV(readFile, final)
    writeSplitItems(idxSplitItems, writeFile)
    checkCols(final, 6)
    
    print (checkSplits(idxSplitItems))
    #return newSplits, final, idxSplitItems

def writeSplitItems(splitItems, writeFile):
    with open(writeFile,mode='w+',encoding='utf8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONE)
        writer.writerows(splitItems)

            


#----------------------Check how many splits/ how many csvs to make-----------
def checkSplits (data):
    global newSplits
    for sublist in data:
        if isinstance(sublist, list):
            if (len(sublist)-1 > newSplits) :
                newSplits = len(sublist)-1 
    return newSplits


#----------------------Remove unwanted commas inside CSV data column-----------
def removeUnwanted(data, column):
    i = 0

    for sublist in data:
        i+=1
        data[i-1][column] = sublist[column].replace(",","")
        print(data[i-1][column])

    return data


#----------------------Split strings by maximum length-------------------------
def split_bylen(index, item, maxLen):
    splitList = [item[ind:ind+maxLen] for ind in range(0, len(item), maxLen)]
    splitList.insert(0,index)
    return splitList


#-----------------------Rewrite split data into the original csv---------------
def writeSplitToCSV(writeFile,data):

    with open(writeFile,mode='w+',encoding='utf8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONE)
        writer.writerows(data)


#-----------------------Check if any row is fixed wrong and has different number of cols------------
def checkCols(data, columns):

    for sublist in data:

        if len(sublist)-1!=columns:
            print ("[X] This row doesnt have the same amount of columns as others: "+sublist)

        else:
            print("[OK] All okay")




#Entry
def click(event):
    # Get the number, debug
    print (startNum.get())
    print (endNum.get())
    print (columnNum.get())
#------------------------String Len check and create new-----------------------

lenCheckFrame = Frame(root)
lemCheckLabel = Label(lenCheckFrame, text="Length check and create new",font=('helvetica', 12, 'bold'))
lenCheckFrame.pack()
lemCheckLabel.grid(row=0, columnspan=2)


#Labels
columnLabel = Label(lenCheckFrame, text="Column to check and export: ")
columnLabel.grid(row=1)

lenLabel = Label(lenCheckFrame, text="Max length of string: ")
lenLabel.grid(row=2)

lenNum = IntVar()
lenNumEntry = Entry(lenCheckFrame, textvariable=lenNum)
lenNumEntry.bind("<Return>", click)

columnNum = IntVar()
columnNumEntry = Entry(lenCheckFrame, textvariable=columnNum)
columnNumEntry.bind("<Return>", click)


#Put entry in frame
lenNumEntry.grid(row=2, column=1)
columnNumEntry.grid(row=1, column=1) 
checkCSV = Button(lenCheckFrame, text='Start', command=lambda: checkLength(), bg='green', fg='white', font=('helvetica', 12, 'bold'))
checkCSV.grid(row=3, columnspan=2)





#_____MAIN LOOP_____
root.mainloop()
