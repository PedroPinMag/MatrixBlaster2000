from tkinter import *

def determinante():

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

        label1 = Label(doisdois, text="Insira os números:")

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
        

        label1 = Label(trestres, text="Insira os números:")

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
    
    determinante = Tk()
    determinante.geometry("400x600")
    determinante.resizable(width=False, height= False)
    determinante.title("Determinante")

    label1 = Label(determinante, text="\nSelecione o tipo de matriz\n",font=("Segoe_Ui, 20"))
    geospace = Label(determinante, text="\n")
    matriz2x2 = Button(determinante, text="2X2", command=matrizdoisdois, padx=150,pady=80)
    matriz3x3 = Button(determinante, text="3X3", command=matriztrestres, padx=150,pady=80)

    label1.pack()
    matriz2x2.pack()
    geospace.pack()
    matriz3x3.pack()
def multiplicar():

    def matrizdoisdois():
        def run():

            e111 = entry111.get()
            e112 = entry112.get()
            e121 = entry121.get()
            e122 = entry122.get()
            e211 = entry211.get()
            e212 = entry212.get()
            e221 = entry221.get()
            e222 = entry222.get()

            e111 = int(e111)
            e112 = int(e112)
            e121 = int(e121)
            e122 = int(e122)
            e211 = int(e211)
            e212 = int(e212)
            e221 = int(e221)
            e222 = int(e222)

            a = e111 * e211
            b = e112 * e212
            c = e121 * e221
            d = e122 * e222

            e = [a,b]
            f = [c,d]
        
            
            labelresposta = Label(doisdois,text=("Respota: " + str(e) + "\n" + "               " + str(f)))
            labelresposta.grid(column=4, row=4)

        doisdois = Tk()
        
        doisdois.geometry("650x150")
        doisdois.title("2X2")
        doisdois.resizable(width=False, height=False)

        label1 = Label(doisdois, text="Insira os números:")


        entry111 = Entry(doisdois,)
        entry112 = Entry(doisdois,)
        entry121 = Entry(doisdois,)
        entry122 = Entry(doisdois,)

        entry211 = Entry(doisdois,)
        entry212 = Entry(doisdois,)
        entry221 = Entry(doisdois,)
        entry222 = Entry(doisdois,)

        button1 = Button(doisdois, text="Run", command=run)

        label1.grid(column=1, row=1)

        entry111.grid(column=1, row=2)
        entry112.grid(column=1, row=3)
        entry121.grid(column=2, row=2)
        entry122.grid(column=2, row=3)

        entry211.grid(column=3, row=2)
        entry212.grid(column=3, row=3)
        entry221.grid(column=4, row=2)
        entry222.grid(column=4, row=3)

        button1.grid(column=1, row=4)  

    def matriztrestres():
        pass


    multiplicar = Tk()
    multiplicar.geometry("400x600")
    multiplicar.resizable(width=False, height= False)
    multiplicar.title("Multiplicar")

    label1 = Label(multiplicar, text="\nSelecione o tipo de matriz\n",font=("Segoe_Ui, 20"))
    geospace = Label(multiplicar, text="\n")
    matriz2x2 = Button(multiplicar, text="2X2", command=matrizdoisdois, padx=150,pady=80)
    matriz3x3 = Button(multiplicar, text="3X3", command=matriztrestres, padx=150,pady=80)

    label1.pack()
    matriz2x2.pack()
    geospace.pack()
    matriz3x3.pack()
    



def window():

    window = Tk()
    window.geometry("1000x800")
    window.resizable(width=False, height=False)
    window.title("MatrixBlaster2000")
    
    label1 = Label(window, text="Selecione o Método:", font=("Segoe_UI", 30))
    label2 = Label(window, text="Autor: PedroPinMag:", font=("Segoe_UI", 20))
    

    button1 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button2 = Button(window, text="Multiplicar", command=multiplicar , padx=110, pady=100)
    button3 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button4 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button5 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button6 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button7 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button8 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)
    button9 = Button(window, text="Determinante", command=determinante, padx=100, pady=100)

    label1.grid(column=2, row=1)
    label2.grid(column=1, row=5)

    button1.grid(column=1, row=2)
    button2.grid(column=2, row=2)
    button3.grid(column=3, row=2)
    button4.grid(column=1, row=3)
    button5.grid(column=2, row=3)
    button6.grid(column=3, row=3)
    button7.grid(column=1, row=4)
    button8.grid(column=2, row=4)
    button9.grid(column=3, row=4)



    window.mainloop()
window()
