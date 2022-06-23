import tkinter as tk
from tkinter import ttk

'''
En este ejercicio tenéis que crear una lista de RadioButton 
que muestre la opción que se ha seleccionado y que contenga 
un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
'''

def selection():
    select_txt = "Eligió la opción nº " + str(seleccion.get())
    label.config(text = select_txt)

def reset():
    seleccion.set(0)
    label.config(text = "")

window = tk.Tk()
window.title("Elija...")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

seleccion = tk.StringVar()
seleccion.set(0)
r1 = ttk.Radiobutton(window, text="Elegir la Opción nº 1", variable=seleccion, value="1", command=selection) 
r2 = ttk.Radiobutton(window, text="Elegir la Opción nº 2", variable=seleccion, value="2", command=selection)
r3 = ttk.Radiobutton(window, text="Elegir la Opción nº 3", variable=seleccion, value="3", command=selection)
r1.grid(row=0, column=0, sticky="w")
r2.grid(row=1, column=0, sticky="w")
r3.grid(row=2, column=0, sticky="w")

label = ttk.Label(window, text="")
label.grid(row=3, column=0, sticky="w")

reset_button = ttk.Button(window, text="Reset" , command=reset)
reset_button.grid(row=3, column=3, sticky='W', padx=10, pady=10)

window.mainloop()
