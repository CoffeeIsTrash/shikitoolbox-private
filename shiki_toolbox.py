from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

import os, csv
import pandas as pd

convert = Tk()
barcode = Tk()
csvedit = Tk()


#Title converter
titleLabel = Label(convert, text="Excel to CSV converter", bg="red", fg="white")
titleLabel.pack(fill=X)

#Title barcode generator
titleLabel = Label(barcode, text="Barcode generator", bg="red", fg="white")
titleLabel.pack(fill=X)

#Title CSV splitter/checker
titleLabel = Label(csvedit, text="CSV splitter/checker", bg="red", fg="white")
titleLabel.pack(fill=X)

def getExcel ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_excel (import_file_path)

def convertToCSV ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index=False, header=False)  

def exitApplication():

    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')

    if MsgBox == 'yes':
       convert.destroy()


convLabel = Label(convert, text="Excel to csv conversion",font=('helvetica', 12, 'bold'))
convLabel.pack(fill=X)
importExcel = Button(convert, text='      Import Excel File     ', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
importExcel.pack(fill=X)
exportCSV = Button(convert, text='Export CSV file', command=convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
exportCSV.pack(fill=X)
exitButton = Button(convert, text='       Exit Application     ', command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
exitButton.pack(fill=X)



#_____MAIN LOOP_____
convert.mainloop()
barcode.mainloop()