import tkinter as tk
from tkinter import ttk
from frames import AttendaceFrame, GenerateId
import customtkinter as ctk
class PayRoll(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payroll Management System")
        self.geometry("800x600")

        self.bind("<<Escape>>", lambda e: self.destroy())
   
        self.setup()
    
    def setup(self):
        create = ctk.CTkButton(self, text="Create ID", command=self.create_id)

        create.pack()

        # attendace = AttendaceFrame(self)
        # attendace.pack()
    def create_id(self):
        
        """
        Open the GenerateId frame for creating a new ID
        """
        id = GenerateId(self)
        id.pack()

if __name__ == "__main__":
    app = PayRoll()
    app.mainloop()