from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import os, csv
import pandas as pd

class App1(ttk.Frame):
    def createWidgets(self):
        #labels
        self.label1 = ttk.Label(self, text="EXCEL TO CSV CONVERTER").pack(side = TOP, pady = 10)

        #buttons
        self.importExcel = Button(self, text='      Import Excel File     ', command=self.getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)
        self.exportCSV = Button(self, text='Export CSV file', command=self.convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)
        self.exitButton = Button(self, text='       Exit Application     ', command=self.quit, bg='brown', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)

    def getExcel (self):
        
        self.import_file_path = filedialog.askopenfilename()
        self.read_file = pd.read_excel (self.import_file_path)

    def convertToCSV (self):
        
        self.export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        self.read_file.to_csv (self.export_file_path, index=False, header=False)  

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

class App2(ttk.Frame):
    def createWidgets(self):
        #labels
        self.label1 = ttk.Label(self, text="BARCODE GENERATOR").pack(side = TOP, pady = 10)
        self.startNumLabel = Label(self, text="Starting num").pack(side=LEFT)
        self.endNumLabel = Label(self, text="Ending num").pack(side=LEFT)


        #buttons
        self.startNum = IntVar()
        self.endNum = IntVar()
        self.startNumEntry = Entry(self, textvariable=self.startNum)
        self.endNumEntry = Entry(self, textvariable=self.endNum)

        # Bind the entrybox to the Return key
        self.startNumEntry.bind("<Return>", self.click)
        self.endNumEntry.bind("<Return>", self.click)

        #Put entry in frame
        self.startNumEntry.pack(side = LEFT)
        self.endNumEntry.pack(side = LEFT)

        #Button
        self.genCSV = Button(self, text='Generate and save to csv', command=self.genBarcodeCSV, bg='green', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)
        self.exitButton = Button(self, text='       Exit Application     ', command=self.quit, bg='brown', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)

    def click(self,event):
        # Get the number, debug
        print (self.startNum.get())
        print (self.endNum.get())

    def genBarcodeCSV(self):
        #Open file to export to
        self.export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')

        with open(self.export_file_path, mode='w+',encoding='utf8', newline='') as self.barcode_file:
            self.barcode_writer = csv.writer(self.barcode_file, quoting=csv.QUOTE_NONE)

            for i in range(self.startNum.get(),self.endNum.get()+1):
                self.barcode_writer.writerow([i])
                print(i)

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

class App3(ttk.Frame):
    def createWidgets(self):
        #labels
        self.label1 = ttk.Label(self, text="CSV checker/splitter").pack(side = TOP, pady = 10)
        self.startNumLabel = Label(self, text="MAX string length").pack(side=LEFT)
        self.endNumLabel = Label(self, text="Column Number").pack(side=LEFT)


        #buttons
        self.startNum = IntVar()
        self.endNum = IntVar()
        self.startNumEntry = Entry(self, textvariable=self.startNum)
        self.endNumEntry = Entry(self, textvariable=self.endNum)


        #Put entry in frame
        self.startNumEntry.pack(side = LEFT)
        self.endNumEntry.pack(side = LEFT)

        #Button
        self.genCSV = Button(self, text='Generate and save to csv', command=self.genBarcodeCSV, bg='green', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)
        self.exitButton = Button(self, text='       Exit Application     ', command=self.quit, bg='brown', fg='white', font=('helvetica', 12, 'bold')).pack(side=LEFT)

   
    def checkLength(self):

        counter = 0
        i = 0
        
        self.column = self.columnNum.get()
        self.readFile = filedialog.askopenfilename()
        self.maxLen = self.lenNum.get()
        self.writeFile = filedialog.asksaveasfilename(defaultextension='.csv')

        with open(self.readFile,'r', encoding="utf8", newline='') as f:
            self.reader = csv.reader(f)
            self.your_list = list(reader)
            self.your_list = self.removeUnwanted(self.your_list, self.column)
            self.final = self.your_list
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



    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
######################################################################################################################

def main():
    #Setup Tk()
    window = Tk()

    #Setup the notebook (tabs)
    notebook = ttk.Notebook(window)
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)
    notebook.add(frame1, text="EXCEL TO CSV")
    notebook.add(frame2, text="BARCODE GEN")
    notebook.add(frame3, text="CSV Checker")
    notebook.grid()

    #Create tab frames
    app1 = App1(master=frame1)
    app1.grid()
    app2 = App2(master=frame2)
    app2.grid()
    app3 = App3(master=frame3)
    app3.grid()

    #Main loop
    window.mainloop()

if __name__ == '__main__':
    main()


