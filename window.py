from tkinter import *
import subprocess

def configWindow(window):

    x = 500
    y = 500

    icon =  PhotoImage(file="./image.png")

    frames = [None] * 9
    colors=["red", "black", "blue", "orange", "pink", "green", "red", "black", "blue"]
    j=0
    n=0
    for i in range(0, len(frames)):
        frames[i]= Frame(
            window, 
            bg=colors[i],
            width=x/3,
            height=y/3
        )
        frames[i].place(x=(n*(x/3)), y=(j*(y/3)))
        n+=1
        goDown=2==(i%3)
        j+= int(goDown)
        if goDown: n=0
        # print(j)

    window.geometry(f"{str(x)}x{str(y)}")
    window.title("Holaaaaaaaaaa")
    window.iconphoto(True, icon)

    window.config(
        background="#ffffff"
    )

brightCMD = "./brightness.ps1"

# process = subprocess.run(["powershell", brightCMD, str(25)], shell=True)



mainWindow = Tk()
configWindow(mainWindow)

# Button(mainWindow, text="create new window", command=print("xd")).pack()

mainWindow.mainloop()