from tkinter import *
from tkinter import filedialog
import os, shutil
from subprocess import call

filename = str()

def select_file():
    global filename
    root.filename = filedialog.askopenfilename(initialdir = "./", title = "Select Krunker Map File", filetypes = (("txt","*.txt"),("all files","*.*")))
    print(root.filename)

    root.currfile.config(text = "Current File Selected:" + root.filename)
    root.filestatus.config(text = "File Status: Has Been Converted")

def save_location():
    root.savelocation = filedialog.askdirectory(initialdir = "./", title = "Select Save Location")
    root.savelocationtext.config(text = "Save Location Selected:" + root.savelocation)

def convert():

    try:
        with open(root.savelocation + os.path.basename(root.filename)) as f:
            print(f.readlines())
            # Do something with the file
    except IOError:
        root.filestatus.config(text = "ERR. Duplicate File In Save Location")
        root.mainloop()

    programdir = os.path.dirname(os.path.abspath(__file__))
    print(programdir)

    if root.filename == str(""):
        root.filestatus.config(text = "File Converted: ERR, No File Selected")    
    else:
        shutil.copyfile(root.filename, programdir + "/repo/" + os.path.basename(root.filename))
        os.chdir(programdir + "/repo")
        print(os.getcwd())
        os.system("node" " krunkerToWavefront.js " + os.path.basename(root.filename))
        root.filestatus.config(text = "File Status: File Has Not Been Converted")

        filecontent = []
        filecontent = os.listdir("./wavefront")

        for i in filecontent:
            if i == ("textures"):
                pass
            else: 
                os.rename("./wavefront/" + i , root.savelocation + "/" + i)
    os.remove(programdir + "/repo/" + os.path.basename(root.filename))

if __name__ == "__main__":
    root = Tk()
    root.title("Krunker file converter GUI")
    root.geometry("525x275")
    root.resizable(0,0)
    #root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='Data/Images/favicon.png'))

    root.fileselectandconvert = Frame(root)
    root.fileselectandconvert.pack(side = BOTTOM)

    root.otherinfo = Frame(root)
    root.otherinfo.pack(side = LEFT)

    #file select and convert buttons

    root.Convertfile = Button(root.fileselectandconvert, text = "CONVERT", command = convert, width = 525, height = 5)
    root.Convertfile.pack(side = BOTTOM)

    root.Selectfilebutton  = Button(root.fileselectandconvert, text = "Select File", command = select_file, width = 525, height = 2)
    root.Selectfilebutton.pack(side = BOTTOM)

    root.Savefilelocation = Button(root.fileselectandconvert, text = "Save Location", command = save_location, width = 525, height = 2)
    root.Savefilelocation.pack(side = BOTTOM)

    #other info that people might want
    root.currfile = Label(root.otherinfo, text = "Current File Selected:")
    root.currfile.pack(anchor = W)

    root.savelocationtext = Label(root.otherinfo, text = "Save Location Selected:")
    root.savelocationtext.pack(anchor = W)

    root.filestatus = Label(root.otherinfo, text = "File Status:")
    root.filestatus.pack(anchor = W)

    root.mainloop()
        