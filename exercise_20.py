import tkinter as tk
from tkinter import ttk

'''
En este segundo ejercicio, tendréis que crear una interfaz 
sencilla la cual debe de contener una lista de elementos 
seleccionables, también debe de tener un label con el texto 
que queráis.
'''

def print_selection():
    
    select_txt = "Eligió la " + lista[listbox.curselection()[0]]
    label.config(text = select_txt)

window = tk.Tk()
window.title("Elija...")
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

label_titulo = ttk.Label(window, text="Escoja su preferencia:")
label_titulo.grid(row=0, column=0, sticky="w")

seleccion = tk.StringVar()
seleccion.set(0)
lista = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5"]
lista_items = tk.StringVar(value=lista)
listbox = tk.Listbox(window, height=10, listvariable=lista_items, selectmode="single")
listbox.grid(row=1, column=0, sticky="nsew")

label = ttk.Label(window, text="Sin selección...")
label.grid(row=3, column=0, sticky="w")

print_button = ttk.Button(window, text="Muestra eleccción" , command=print_selection)
print_button.grid(row=3, column=3, sticky='W', padx=10, pady=10)

window.mainloop()
