from tkinter import *
import main as v

def main():
    root = Tk()
    root.wm_title("Suma de numeros")
    app = v.FrSuma(root)
    app.config(bg="pink", width=900, height=900)
    app.mainloop()

if __name__ == '__main__':
    main()
