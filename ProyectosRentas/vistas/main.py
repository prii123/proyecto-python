from msilib.schema import ComboBox
import sqlite3
from tkinter import *
from tkinter import ttk

class FrSuma(Frame):
    db_name = 'database.db'

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # container selector de empresas
        contenedorSelectorEmpresa = LabelFrame(
            self, text='Selector de empresas', padx=50, pady=50)
        # contenedorSelectorEmpresa.pack_configure(width=900,height=900)
        contenedorSelectorEmpresa.grid(row=0, column=0, columnspan=3, pady=20)

        # Name select empresa
        Label(contenedorSelectorEmpresa, text='Name: ').grid(row=1, column=0)
        #ComboBox empresas
        self.comboEmpresas = ttk.Combobox(contenedorSelectorEmpresa, state="readonly",
        values=["Python", "C", "C++", "Java"])
        self.comboEmpresas.grid(row=1, column=1)


        # Button Add Product
        ttk.Button(contenedorSelectorEmpresa, text='Select').grid(
            row=3, columnspan=2, sticky=W + E)

        # out put messages
        self.message = Label(contenedorSelectorEmpresa, text='', fg='red')
        self.message.grid(row=4, column=0, sticky=W + E)

        # table
        # self.tree = ttk.Treeview(contenedor, height=10, columns=2)
        # self.tree.grid(row=5, column=0, columnspan=2)
        # self.tree.heading('#0', text='Name', anchor='center')
        # self.tree.heading('#1', text='Price', anchor='center')

        # container de los modulos de operacion
        contenedorModulos = LabelFrame(
            self, text='Seccion de procesos', padx=50, pady=50)
        contenedorModulos.grid(row=0, column=4, columnspan=3, pady=20)
        # contenedorModulos.config(width=480,height=320)

        ttk.Button(contenedorModulos, text='Select').grid(
            row=2, columnspan=2, sticky=W + E)
        ttk.Button(contenedorModulos, text='Select').grid(
            row=3, columnspan=2, sticky=W + E)
        ttk.Button(contenedorModulos, text='Select').grid(
            row=4, columnspan=2, sticky=W + E)


