from tkinter import *
import vistas.main as vista
# import vistas.patrimonio as patrimonio

def main():
    root = Tk()
    root.wm_title("Declaracion de renta PN")
    app = vista.Patrimonio(root)
    app.config(bg="pink", width=900, height=900)
    app.mainloop()

if __name__ == '__main__':
    main()
