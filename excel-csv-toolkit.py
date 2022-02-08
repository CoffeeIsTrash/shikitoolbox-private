import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Entry
import pandas as pd
import csv

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 700, height = 500, relief = 'raised')
canvas1.pack()

titleFrame = tk.Frame(root)
titleFrame.pack()
generatorFrame = tk.Frame(root)
generatorFrame.pack()
conversionFrame = tk.Frame(root)
conversionFrame.pack(side='BOTTOM')



label1 = tk.Label(root, text='File Conversion and BC Generator Tool')
label1.config(font=('helvetica', 20))
canvas1.create_window(300, 50, window=label1)
startNumberEntry = tk.Entry(canvas1)
canvas1.create_window(100,100,window=startNumberEntry)
genLabel = tk.Label(root, text='Barcode generator' )
genLabel.config(font=('helvetica',15))
canvas1.create_window(100,80, window=genLabel)

def barcsvgen ():
    barcode = input("Naziv file-a: ")
    x = int(input("Pocetni broj: "))
    y = int(input("Krajnji broj: "))
    with open(barcode + '.txt', mode='w+', newline='') as barcode_file:
        barcode_writer = csv.writer(barcode_file, quoting=csv.QUOTE_NONE)
        barcode_writer.writerow(['NUM1','NUM2'])
        for i in range(x,y+1):
            barcode_writer.writerow([i,i])
            print(i)



def getExcel ():
    global read_file
    
    import_file_path = filedialog.askopenfilename()
    read_file = pd.read_excel (import_file_path)
    
browseButton_Excel = tk.Button(text="      Import Excel File     ", command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 130, window=browseButton_Excel)

'''def checklines (efile):

'''



def convertToCSV ():
    global read_file
    
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    read_file.to_csv (export_file_path, index = None, header=True)

saveAsButton_CSV = tk.Button(text='Convert Excel to CSV', command=convertToCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_CSV)

def exitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
     
exitButton = tk.Button (root, text='       Exit Application     ',command=exitApplication, bg='brown', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 230, window=exitButton)

root.mainloop()