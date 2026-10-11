from tkinter import *
from Section import *


xs="asdasd\n"

def configWindow(window):
    
    width = 750
    height = 500
    
    window.geometry(
        f"{str(width)}x{str(height)}"
    )
    window.resizable(False, False)
    window.title("PAUSA")


def newItem():
    return Frame(
        sectionDisplay,
        bg="grey",
        bd=1, relief=SUNKEN,
        width=250, height=25
    )
    

def addSection():
    sections.append(Section("", 0.0, newItem()))
    sections[len(sections) - 1].frame.place(
        x=(300/2)-(250/2), 
        y=25 *len(sections)
    )
   
    
sections = []
mainWindow = Tk()
configWindow(mainWindow)

addSectionButton=Button(
    mainWindow, text="Añadir Seccion"
)
addSectionButton.config(command=addSection)

sectionDisplay=Frame(
    mainWindow, 
    bg="pink",
    bd=5, relief=SUNKEN, 
    width=300, height=400
)

sectionDisplay.place(x=(750/2)-(300/2), y=50)


addSectionButton.pack()

mainWindow.mainloop()


