from tkinter import *
import subprocess

def configWindow(window):
    
    width = 750
    height = 500
    
    
    window.geometry(
    f"{str(width)}x{str(height)}"
    )
    window.resizable(False, False)
    window.title("PAUSA")

def screenBrightness(bLevel):
    brightCMD = "./brightness.ps1"
    
    process = subprocess.run(["powershell", brightCMD, str(bLevel)], shell=True)
    
def transformarFrame(frame, dimension):
    frame.config(width=dimension["x"], height=dimension["y"])
   
mainWindow = Tk()
configWindow(mainWindow)

modosEnfoque = Frame(
    mainWindow, 
    bg="pink",
    width=250,
    height=500
)
modosEnfoque.pack()
modosEnfoque.place(x=0, y=0)

areaGeneral = Frame(
    mainWindow, 
    bg="grey",
    width=500,
    height=500
)
areaGeneral.pack()
areaGeneral.place(x=250, y=0)

Button(
    areaGeneral, 
    text="B = 0", 
    command=lambda: transformarFrame(
        modosEnfoque, 
        {"x":50, "y":50}
    )
).pack()

# Button(areaGeneral, text="B = 100", command=lambda: screenBrightness(100)).pack()

mainWindow.mainloop()

#Sesiones de Trabajo, permite al usuario establecer sus periodos de descanso y trabajo para su sesion de trabajo

#Notificaciones sobre los cambios de periodos en la sesion de trabajo