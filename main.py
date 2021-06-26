from tkinter import *

def matrizdoisdois():

    def run():

        e11 = entry11.get()
        e12 = entry12.get()
        e21 = entry21.get()
        e22 = entry22.get()

        e11 = int(e11)
        e12 = int(e12)
        e21 = int(e21)
        e22 = int(e22)

        a = e11 * e22
        b = e12 * e21
        c = a - b

        labelresposta = Label(doisdois,text=("Respota: " + str(c)))
        labelresposta.grid(column=2, row=4)

    doisdois = Tk()
    
    doisdois.geometry("325x150")
    doisdois.title("2X2")
    doisdois.resizable(width=False, height=False)

    label1 = Label(doisdois, text="Insira os números")

    entry11 = Entry(doisdois,)
    entry12 = Entry(doisdois,)
    entry21 = Entry(doisdois,)
    entry22 = Entry(doisdois,)

    button1 = Button(doisdois, text="Run", command=run)

    label1.grid(column=1, row=1)
    entry11.grid(column=1, row=2)
    entry12.grid(column=1, row=3)
    entry21.grid(column=2, row=2)
    entry22.grid(column=2, row=3)
    button1.grid(column=1, row=4)    

def matriztrestres():

    def run():

            e11 = entry11.get()
            e12 = entry12.get()
            e13 = entry13.get()

            e21 = entry21.get()
            e22 = entry22.get()
            e23 = entry23.get()

            e31 = entry31.get()
            e32 = entry32.get()
            e33 = entry33.get()

            e11 = int(e11)
            e12 = int(e12)
            e13 = int(e13)

            e21 = int(e21)
            e22 = int(e22)
            e23 = int(e23)

            e31 = int(e31)
            e32 = int(e32)
            e33 = int(e33)

            a = (e11 * e22 * e33) 
            b = (e12 * e23 * e31) 
            c = (e13 * e21 * e32)
            d = (e13 * e22 * e31)
            e = (e11 * e23 * e32) 
            f = (e33 * e21 * e12)

            g = a + b + c
            h = d + e + f
            i = g - h

            labelresposta = Label(trestres, text=("Resposta: "+ str(i)))
            labelresposta.grid(column=2, row=5)
    trestres = Tk()
    
    trestres.geometry("500x150")
    trestres.title("3X3")
    trestres.resizable(width=False, height=False)
    

    label1 = Label(trestres, text="Insira os números")

    entry11 = Entry(trestres,)
    entry12 = Entry(trestres,)
    entry13 = Entry(trestres,)
    entry21 = Entry(trestres,)
    entry22 = Entry(trestres,)
    entry23 = Entry(trestres,)  
    entry31 = Entry(trestres,)
    entry32 = Entry(trestres,)
    entry33 = Entry(trestres,)  

    button1 = Button(trestres, text="Run", command=run)

    label1.grid(column=1, row=1)

    entry11.grid(column=1, row=2)
    entry12.grid(column=2, row=2)
    entry13.grid(column=3, row=2)

    entry21.grid(column=1, row=3)
    entry22.grid(column=2, row=3)
    entry23.grid(column=3, row=3)

    entry31.grid(column=1, row=4)
    entry32.grid(column=2, row=4)
    entry33.grid(column=3, row=4)

    button1.grid(column=1, row=5)    

def window():
    window = Tk()
    window.geometry("400x600")
    window.resizable(width=False, height= False)
    window.title("MatrizBlaster 2000")

    label1 = Label(window, text="\nSelecione o tipo de matriz\n",font=("Segoe_Ui, 20"))
    geospace = Label(window, text="\n")
    matriz2x2 = Button(window, text="2X2", command=matrizdoisdois, padx=150,pady=80)
    matriz3x3 = Button(window, text="3X3", command=matriztrestres, padx=150,pady=80)

    label1.pack()
    matriz2x2.pack()
    geospace.pack()
    matriz3x3.pack()

    window.mainloop()

window()
