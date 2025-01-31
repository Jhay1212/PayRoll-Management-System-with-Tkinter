from tkinter import ttk
import tkinter as tk
import customtkinter as ck

from openpyxl import load_workbook, Workbook, styles
import os 

base_path = os.path.dirname(__file__)


try:
    with open(os.path.join(base_path, 'pay.xlsx'), 'rb') as f:
        wb = load_workbook(f)
except FileNotFoundError:
    wb = Workbook()
    wb.save(os.path.join(base_path, 'pay.xlsx'))
    wb = load_workbook(os.path.join(base_path, 'pay.xlsx'))

class AttendaceFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=100, height=400)
        self.pack(fill=tk.BOTH, expand=True)
        # self.pack()
        self.create_widgets()

        self.time = tk.StringVar()

        self.time_out_val = tk.StringVar()

        



    def create_widgets(self):
        self.employee = ttk.LabelFrame(self, text="Employee")
        self.employee.pack(fill=tk.BOTH)
        self.employee.columnconfigure(0, weight=1)

        self.employee_id = ck.CTkEntry(self)
        self.employee_id.pack()

        self.employee_id_label = ck.CTkLabel(self, text="Employee ID")
        self.employee_id_label.pack()

        self.employee_name = ck.CTkEntry(self)
        self.employee_name.pack()
        self.employee_name_label = ck.CTkLabel(self, text="Employee Name")
        self.employee_name_label.pack()


        self.time_in = ck.CTkEntry(self)
        self.time_in.pack()
        self.time_in_label = ck.CTkLabel(self, text="Time In")
        self.time_in_label.pack()

        self.log_out = ck.CTkEntry(self)
        self.log_out.pack()

        self.log_out_label = ck.CTkLabel(self, text="Log Out")
        self.log_out_label.pack()
    wb.save(os.path.join(base_path, 'pay.xlsx'))


        

class EmpployeeFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=400, height=400)
        self.pack(fill=tk.BOTH, expand=True)
        # self.pack()

    
    