from tkinter import *

class Section:
    def __init__(self, name="", duration=0.0, frame=None):
        if (len(name) == 0): name="noName"
         
        self.name = name
        self.duration = duration
        self.frame = frame
        
        
        self.nameLabel = Label(self.frame, text="Name:")
        self.durationLabel = Label(self.frame, text="Duration:")
        
        self.nameEntry=Entry(
            self.frame, width=5
        )
        
        self.durationEntry=Entry(
            self.frame, width=5
        )
      
        
        # self.frame.grid_columnconfigure((1,3), weight=0.5)

        
        self.nameLabel.grid(row=0, column=0)
        self.nameEntry.grid(row=0, column=1)
        self.durationLabel.grid(row=0, column=2)
        self.durationEntry.grid(row=0, column=3)
        
        
    
    def setName(name):
        self.name = name
        
    def setDuration():
        self.duration = duration