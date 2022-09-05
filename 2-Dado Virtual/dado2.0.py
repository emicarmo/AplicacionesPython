import random 
import tkinter as tk

def tirar_dado():
    caja_numero_dado.delete(0, tk.END)
    valor = random.randint(1,6)
    caja_numero_dado.insert(0, valor)

ventana = tk.Tk()
ventana.config(width=250, height=200)
ventana.title('Dado 2.0')

btn_arrojar_dado = tk.Button(text='Arrojar el dado', command=tirar_dado)
btn_arrojar_dado.place(x=70, y=30, width=100, height=50)

label_valor_dado = tk.Label(text='Valor:')
label_valor_dado.place(x=70, y=100)

caja_numero_dado = tk.Entry()
caja_numero_dado.place(x=70, y=140, width=100)

ventana.mainloop()