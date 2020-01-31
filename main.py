from tkinter import *
from tkinter import filedialog
import os, shutil, time
from subprocess import call
from pathlib import Path
import shutil

filename = str()

def select_file():
    global filename
    root.filename = filedialog.askopenfilename(initialdir = "./", title = "Select Krunker Map File", filetypes = (("txt","*.txt"),("all files","*.*")))
    print(root.filename)

    root.currfile.config(text = "Current File Selected:" + root.filename)
    root.filestatus.config(text = "File Status: File Status: Has Not Been Converted")

def save_location():
    root.savelocation = filedialog.askdirectory(initialdir = "./", title = "Select Save Location")
    root.savelocationtext.config(text = "Save Location Selected:" + root.savelocation)

def convert():
    converted_file_name = (os.path.splitext(root.savelocation + '/' + os.path.basename(root.filename))[0])
    converted_file = Path(converted_file_name + '.obj')
    print('--File name--: ' + converted_file_name)
    print('--File getting used--:' + str(converted_file))

    root.filestatus.config(text = "File Status: Converting...")
    programdir = os.path.dirname(os.path.abspath(__file__))
    print(programdir)
    if root.filename == str(""):
        root.filestatus.config(text = "File Status: ERR, No File Selected") 
        root.mainloop()   
    else:
        shutil.copyfile(root.filename, programdir + "/repo/" + os.path.basename(root.filename))
        os.chdir(programdir + "/repo")
        print(os.getcwd())
        os.system("node" " krunkerToWavefront.js " + os.path.basename(root.filename))
        root.filestatus.config(text = "File Status: File Has Been Converted")
        filecontent = []
        filecontent = os.listdir("./wavefront")
        for i in filecontent:
            if i == ("textures"):
                pass
            else:
                try:
                    os.rename(("./wavefront/" + i ), (root.savelocation + "/" + i))
                    os.remove(programdir + "/repo/" + os.path.basename(root.filename))
                    shutil.copyfile(("./wavefront/textures"), (root.savelocation + "/" + i))
                except IOError:
                    root.filestatus.config(text = "File Status: ERR. Duplicate File In Save Location")
                    os.remove(programdir + "/repo/" + os.path.basename(root.filename))
                    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Krunker file converter GUI")
    root.geometry("525x275")
    root.resizable(0,0)
    root.configure(bg='#393952')
    #root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Data/Images/favicon.png'))

    root.fileselectandconvert = Frame(root, bg='#393952')
    root.fileselectandconvert.pack(side = BOTTOM)

    root.otherinfo = Frame(root, bg='#393952')
    root.otherinfo.pack(side = LEFT)

    #file select and convert buttons

    root.Convertfile = Button(root.fileselectandconvert, text = "CONVERT", command = convert, width = 525, height = 5, bg='#393952', fg='#fafafa', activebackground='#f06f51', activeforeground='#fafafa')
    root.Convertfile.pack(side = BOTTOM)

    root.Selectfilebutton  = Button(root.fileselectandconvert, text = "Select File", command = select_file, width = 525, height = 2, bg='#393952', fg='#fafafa', activebackground='#f06f51', activeforeground='#fafafa')
    root.Selectfilebutton.pack(side = BOTTOM)

    root.Savefilelocation = Button(root.fileselectandconvert, text = "Save Location", command = save_location, width = 525, height = 2, bg='#393952', fg='#fafafa', activebackground='#f06f51', activeforeground='#fafafa')
    root.Savefilelocation.pack(side = BOTTOM)

    #other info that people might want
    root.currfile = Label(root.otherinfo, text = "Current File Selected:", bg='#393952', fg='#fafafa')
    root.currfile.pack(anchor = W)

    root.savelocationtext = Label(root.otherinfo, text = "Save Location Selected:", bg='#393952', fg='#fafafa')
    root.savelocationtext.pack(anchor = W)

    root.filestatus = Label(root.otherinfo, text = "File Status:", bg='#393952', fg='#fafafa')
    root.filestatus.pack(anchor = W)

    root.mainloop()
        