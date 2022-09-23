from msilib.schema import ComboBox
import sqlite3
from tkinter import *
from tkinter import ttk

class Patrimonio(Frame):
    db_name = 'database.db'

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # container selector de empresas
        contenedorSelectorEmpresa = LabelFrame(
            self, text='Propiedades a su nobre', padx=80, pady=50)
        # contenedorSelectorEmpresa.pack_configure(width=900,height=900)
        contenedorSelectorEmpresa.grid(row=0, column=0, columnspan=3, pady=20)



        # Name select empresa
        Label(contenedorSelectorEmpresa, text='Name: ').grid(row=1, column=0)
        #ComboBox empresas
        self.comboEmpresas = ttk.Combobox(contenedorSelectorEmpresa, state="readonly",
        values=["Python", "C", "C++", "Java"])
        self.comboEmpresas.grid(row=1, column=1)


