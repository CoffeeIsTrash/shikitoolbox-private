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




################################ BARCODE GENERATOR FUNCTIONS ##########################################
#Barcode gen def
def genBarcodeCSV ():

    #Open file to export to
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')

    with open(export_file_path, mode='w+',encoding='utf8', newline='') as barcode_file:
        barcode_writer = csv.writer(barcode_file, quoting=csv.QUOTE_NONE)

        for i in range(startNum.get(),endNum.get()+1):
            barcode_writer.writerow([i])
            print(i)


def getExcel ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_excel (import_file_path,encoding='utf-8')

def convertToCSV ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index=False, header=False,encoding='utf-8')  

def exitApplication():

    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')

    if MsgBox == 'yes':
       root.destroy()





######################################  TKINTER FRAMES  ##################################################

#----------------------Barcode generator frame------------------------
genFrame = Frame(root)
genLabel = Label(genFrame, text="Barcode sequence generator",font=('helvetica', 12, 'bold'))
genFrame.pack()
genLabel.grid(row=0, columnspan=2)


#Labels
startNumLabel = Label(genFrame, text="Starting num")
endNumLabel = Label(genFrame, text="Ending num")
startNumLabel.grid(row=1)
endNumLabel.grid(row=2)


#Entry
def click(event):
    # Get the number, debug
    print (startNum.get())
    print (endNum.get())
    print (columnNum.get())

startNum = IntVar()
endNum = IntVar()
startNumEntry = Entry(genFrame, textvariable=startNum)
endNumEntry = Entry(genFrame, textvariable=endNum)


# Bind the entrybox to the Return key
startNumEntry.bind("<Return>", click)
endNumEntry.bind("<Return>", click)


#Put entry in frame
startNumEntry.grid(row=1, column=1)
endNumEntry.grid(row=2,column=1)

#Button
genCSV = Button(genFrame, text='Generate and save to csv', command=genBarcodeCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
genCSV.grid(row=3, columnspan=2)



#-------------------------Escel to CSV conversion-----------------------------

convLabel = Label(root, text="Excel to csv conversion",font=('helvetica', 12, 'bold'))
convLabel.pack(fill=X)
importExcel = Button(root, text='      Import Excel File     ', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
importExcel.pack(fill=X)
exportCSV = Button(root, text='Export CSV file', command=convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
exportCSV.pack(fill=X)
exitButton = Button(root, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
exitButton.pack(fill=X)



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

'''

final, idxSplitItems = checkLength(0,'test.csv','final.csv', 30)
print("------------------------")
print(idxSplitItems)
print("-------------------------")
print(final)
'''



'''

'''



