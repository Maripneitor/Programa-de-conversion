import tkinter as tk
from tkinter import ttk

def convertir():
    try:
        temp = float(textbox.get())
        print(f"Temperatura ingresada: {temp}")
        conversion = var.get()
        print(f"Conversion seleccionada: {conversion}")
        if conversion == 1:
            resultado = (temp - 32) * 5/9
            resultado_label.config(text=f"{temp} Fahrenheit son {resultado:.2f} Celsius")
        elif conversion == 2:
            resultado = (temp * 9/5) + 32
            resultado_label.config(text=f"{temp} Celsius son {resultado:.2f} Fahrenheit")
        else:
            resultado_label.config(text="Seleccione una conversion.")
        print(f"Resultado: {resultado}")
    except ValueError:
        resultado_label.config(text="Por favor, ingrese un numero valido.")
        print("Error: Entrada no valida")

def limpiar():
    textbox.delete(0, tk.END)
    resultado_label.config(text="")
    var.set(0)

ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.minsize(500, 400)

etiqueta = ttk.Label(ventana, text="Conversor de temperatura")
etiqueta.place(x=200, y=20)
etiqueta.config(foreground="red")

etiqueta = ttk.Label(ventana, text="Ingrese la temperatura:")
etiqueta.place(x=50, y=50)

var = tk.IntVar()

radio1 = ttk.Radiobutton(ventana, text="Fahrenheit a Celsius", variable=var, value=1)
radio1.place(x=50, y=110)

radio2 = ttk.Radiobutton(ventana, text="Celsius a Fahrenheit", variable=var, value=2)
radio2.place(x=50, y=140)

textbox = tk.Entry(ventana)
textbox.place(x=50, y=80)

resultado_label = ttk.Label(ventana, text="")
resultado_label.place(x=180, y=80)

boton_convertir = ttk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.place(x=50, y=170)

boton_limpiar = ttk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.place(x=120, y=170)

boton_salir = ttk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.place(x=50, y=250)

ventana.mainloop()

