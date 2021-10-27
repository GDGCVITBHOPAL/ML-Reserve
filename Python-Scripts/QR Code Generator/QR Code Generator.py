import pyqrcode
import tkinter as tk 
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


#Defining Widgets() function to create tkinter widgets
def Widgets():
    label = Label(text='Enter Text: ',bg='deep sky blue')
    label.grid(row=0, column=1, padx=5, pady=5)

    root.entry = Entry(width=30, textvariable=InputQR)
    root.entry.grid(row=0, column=2, padx=5, pady=5)

    button = Button(width=10, text='Generate', command=GenerateQRCode)
    button.grid(row=0, column=3, padx=5, pady=5)

    label = Label(text='QR Code: ', bg='deep sky blue')
    label.grid(row=1, column=1, padx=5, pady=5)

    root.imageLabel = Label(root, background='deep sky blue')
    root.imageLabel.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

#Defining GenerateQRCode() 
def GenerateQRCode():
    # Storing User-Input Text 
    QRstring = InputQR.get()

    if QRstring!='':
        QRGenerate = pyqrcode.create(QRstring)

        QRCodePath = 'D:\Python\qrsaver'
        QRCodeName = QRCodePath + '\\'  + QRstring + '.png'
        QRGenerate.png(QRCodeName, scale=10)
        image = Image.open(QRCodeName)
        image = image.resize((400,400), Image.ANTIALIAS)

        image = ImageTk.PhotoImage(image)
        root.imageLabel.config(image=image)
        root.imageLabel.photo = image

    else: 
        messagebox.showerror("ERROR","Enter a valid input!!")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry('500x500')
root.resizable(False,False)
root.config(background='deep sky blue')

InputQR = StringVar()
Widgets()
root.mainloop()
