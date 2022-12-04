import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="ingrese el primer valor: ")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry.grid(column=1, row =0)

        self.label2=tk.Label(self.ventana1, text="ingrese el segundo valor: ")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)

        self.seleccion=tk.IntVar()
        self.radio1=tk.Radiobutton(self.ventana1, text="Sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=1, row=2)
        self.radio2=tk.Radiobutton(self.ventana1, text="Restar", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=3)
        self.boton1=tk.Button(self.ventana1, text="Operar", command=self.operar)
        self.boton1.grid(column=1, row=4)
        self.radio3=tk.Radiobutton(self.ventana1, text="multiplicar", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=2)
        self.radio4=tk.Radiobutton(self.ventana1, text="dividir", variable=self.seleccion, value=4)
        self.radio4.grid(column=2, row=3)
        self.radio5=tk.Radiobutton(self.ventana1, text="porcentaje", variable=self.seleccion, value=5)
        self.radio5.grid(column=2, row=4)
        self.radio6=tk.Radiobutton(self.ventana1, text="potencia", variable=self.seleccion, value=6)
        self.radio6.grid(column=2, row=5)
        
        self.label3=tk.Label(self.ventana1,text="")
        self.label3.grid(column=1, row=5)
        self.ventana1.mainloop()

    def operar(self):

        if self.seleccion.get()==1:
            suma=int(self.dato1.get())+int(self.dato2.get())
            self.label3.configure(text=suma)
 
        if self.seleccion.get()==2:
            resta=int(self.dato1.get()) - int(self.dato2.get())
            self.label3.configure(text=resta)

        if self.seleccion.get()==3:
            multiplicar=int(self.dato1.get()) * int(self.dato2.get())
            self.label3.configure(text=multiplicar)

        if self.seleccion.get()==4:
            dividir=int(self.dato1.get()) / int(self.dato2.get())
            self.label3.configure(text=dividir)
            
        if self.seleccion.get()==5:
            porcentaje=int(self.dato1.get())  % int(self.dato2.get())
            self.label3.configure(text=porcentaje)

        if self.seleccion.get()==6:
            potencia=int(self.dato1.get()) ** int(self.dato2.get())
            self.label3.configure(text=potencia)           
                    

apliacion1=Aplicacion()
