from math import floor
import os
import PyPDF2 as pdf
from googletrans import Translator
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import *
from tkinter.ttk import *
import time

def File_dialog():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("PDF files", ".pdf")])

    if(file_path!="" and file_path.endswith(".pdf")):
        
        ws.deiconify()
        return (file_path)
    else :
        ws.quit()
        exit()
        
        print("Error")



from_lang = 'en'
to_lang = 'te'
output_filename = 'output.pdf'
def text():
    global pb1
    global ws
   

    path=File_dialog()
    outputfile=os.path.basename(path).replace(".pdf",".txt")
    pdffile=open(path,"rb")
    pdfreader=pdf.PdfFileReader(pdffile)
    
    total_pages=pdfreader.getNumPages();
    #print("Total Pages:",total_pages)
    f=open(".//output_folder//"+outputfile,"w",encoding='utf-8')   
    for i in range(0,total_pages):
        str=pdfreader.getPage(i)
        
        text=str.extractText()
        #print("Page ",i,"/",total_pages)
        L['text']="Page ",i,"/",total_pages
        pb1['value']=floor((i/total_pages)*100)
        
        try:

            
            f.write(text_translator(text))
            
            
        except:
            L['text']="Error"
            
    f.close()
    ws.quit()
    messagebox.showinfo("Information","Finish...")
def text_translator(data):
    try:
        translator = Translator()
        text_to_translate = translator.translate(data,src= from_lang,dest= to_lang)
        
        return text_to_translate.text
    except :
        L['text']="Error"
            
        #print("Error")
def prbar():
    global pb1   
    global ws 
    global L
    ws = Tk()
    ws.resizable(False,False)
    ws.title('Pdf_Convertor_Eng To _Telugu_ver1.0')
    ws.geometry('400x150')
    ws.eval('tk::PlaceWindow . center')
    L=Label(ws,text="Status...")
    L.place(relx=0.0, rely=1.0, anchor='sw')
    ws.update_idletasks()
    #pb1['value'] = value_/200
            
    def _ext():
        import sys
        sys.exit()

    pb1 = Progressbar(ws, orient=HORIZONTAL, length=200, mode='determinate')
    pb1.pack(expand=True)
    Button(ws,text="Cancel",command=_ext).pack(side=TOP, anchor=NE)
    ws.withdraw()
    ws.mainloop()
    
    
from threading import Thread
if __name__ == '__main__':
    try:
        
        Thread(target = prbar).start()    
        Thread(target = text).start()
        
    except :
        pass
#text()