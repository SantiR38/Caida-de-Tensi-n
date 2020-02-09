from tkinter import *
#------------------Raíz------------------------

root = Tk()
root.title("Caída de Tensión")
root.config()
root.iconbitmap("caida-tension.ico")

#-------------------Frame----------------------

miFrame = Frame()
miFrame.pack()
miFrame.config(bg="#C2C2C2", width=300, height=300, bd=35)

#-----------------Funciones--------------------
potencia = StringVar()
longitud = StringVar()
tension = IntVar()
seccion = StringVar()
rho = 1/56
intensidad = 0
resistividad = 0
caidaTension = 0


def funcionCalcular():
    global resultant
    intensidad = float(potencia.get()) / float(tension.get())
    resistividad = 2 * rho * float(longitud.get()) / float(seccion.get())
    caidaTension = intensidad * resistividad

    if caidaTension < 4:
        resultado.config(text="La sección de cable es correcta.")
    elif caidaTension >= 4 and caidaTension < 6.6:
        resultado.config(text="La sección es aceptable, pero es recomendable una sección mayor.")
    elif caidaTension >= 6.6:
        resultado.config(text="La sección de cable es muy pequeña. Haz el calculo con una sección mayor")

    resultados.config(text=f"\nRho: {rho}"
                           f"\nIntensidad: {intensidad}"
                           f"\nResistividad: {resistividad}"
                           f"\nCaída de Tensión: {caidaTension}")



#------------------Título----------------------
tituloLabel = Label(miFrame, text="Caída de Tensión")
tituloLabel.grid(row=0, column=0, pady=10, columnspan=4)
tituloLabel.config(font="Helvetica 15 bold")

#-----------------Formulario-------------------

#---Potencia---
DPMSLabel = Label(miFrame, text="DPMS: ")
DPMSLabel.grid(row=1, column=0, sticky="w", padx=5, pady=10)
DPMSLabel.config(font="Helvetica 10")
cuadroDPMS = Entry(miFrame, textvariable=potencia)
cuadroDPMS.grid(row=1, column=1, columnspan=2, pady=10)
cuadroDPMS.config(fg="blue", justify="center")
watts = Label(miFrame, text="W")
watts.grid(row=1, column=3, sticky="w", padx=5, pady=10)
watts.config(font="Helvetica 10")

#---Longitud---
longLabel = Label(miFrame, text="Longitud: ")
longLabel.grid(row=2, column=0, sticky="w", padx=5, pady=10)
longLabel.config(font="Helvetica 10")
cuadroLong = Entry(miFrame, textvariable=longitud)
cuadroLong.grid(row=2, column=1, columnspan=2, pady=10)
cuadroLong.config(fg="blue", justify="center")
metros = Label(miFrame, text="mts")
metros.grid(row=2, column=3, sticky="w", padx=5, pady=10)
metros.config(font="Helvetica 10")

#---Tensión---
tensionLabel = Label(miFrame, text="Tensión")
tensionLabel.grid(row=3, column=0, sticky="w", padx=5, pady=10)
tensionLabel.config(font="Helvetica 10")

Radiobutton(miFrame, text="220", variable=tension, value=220).grid(row=3, column=1, pady=10)
Radiobutton(miFrame, text="380", variable=tension, value=380).grid(row=3, column=2, pady=10)

volts = Label(miFrame, text="V")
volts.grid(row=3, column=3, sticky="w", padx=5, pady=10)
volts.config(font="Helvetica 10")


#---Sección---
seccLabel = Label(miFrame, text="Sección: ")
seccLabel.grid(row=4, column=0, sticky="w", padx=5, pady=10)
seccLabel.config(font="Helvetica 10")
cuadroSecc = Entry(miFrame, textvariable=seccion)
cuadroSecc.grid(row=4, column=1, columnspan=2, pady=10)
cuadroSecc.config(fg="blue", justify="center")
mmCuadrados = Label(miFrame, text="mm2")
mmCuadrados.grid(row=4, column=3, sticky="w", padx=5, pady=10)
mmCuadrados.config(font="Helvetica 10")

#---Botón---
calcularBoton = Button(miFrame, text="Calcular", command=funcionCalcular)
calcularBoton.grid(row=5, column=0, padx=5, pady=10, columnspan=4)

#---Resultados---
resultados = Label(miFrame)
resultados. grid(row=6, column=0, padx=5, pady=10, columnspan=4)
resultado = Label(miFrame)
resultado. grid(row=7, column=0, padx=5, pady=10, columnspan=4)

root.mainloop()