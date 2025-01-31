import tkinter as tk
from tkinter import ttk
from frames import AttendaceFrame
class PayRoll(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Payroll Management System")
        self.geometry("800x600")
        attendace = AttendaceFrame(self)


if __name__ == "__main__":
    app = PayRoll()
    app.mainloop()