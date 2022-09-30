import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger
import time
import threading
#Set the geometry
root = tk.Tk()
root.geometry("750x250")
  
text = tk.Label(root, text="Please, select PDF's to merge",fg="Blue", font=("Helvetica", 18))
text.place(x=250,y=90)

def pdf_merge():
    ''' Merges all the pdf files in current directory '''
    merger = PdfFileMerger()
    allpdfs = select_files()
    if(len(allpdfs)<1):
        text.configure(text="Please, select PDF's to merge")
        return
    
    text.configure(text="Processing")
    
    f = tk.filedialog.asksaveasfile(initialfile = 'Merged.pdf',title='Pick Location to save', defaultextension=".txt",filetypes=[("All Files","*.*"),("PDF File","*.pdf")])
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        text.configure(text="Please, select PDF's to merge")
        return
    
    [merger.append(pdf) for pdf in allpdfs]
    
    with open(f.name, "wb") as new_file:
        merger.write(new_file)
    text.configure(text="Done")

def select_files():
    selected_files = filedialog.askopenfilenames(parent=root,
                                                title='Choose files', 
                                                filetypes=(("PDF's", "*.pdf"), 
                                                           ("All files", "*.*")))
    return selected_files

def startThread():
    # Call work function
    t1=threading.Thread(target=pdf_merge)
    t1.start()

button = tk.Button(root, text='Select files', height= 3, width=10, command=startThread).pack()


root.wm_title("Ali Asghar's PDF Merger")
root.mainloop()
