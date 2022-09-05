"""  
Ejercicio 1: Dólar II
Hacer un programa que con un botón de consulta
muestre el precio de compra y venta del dólar.
"""

import tkinter as tk, requests, os, sys
from tkinter import ttk, messagebox

def llamadaRequest():
    try:
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        if r.status_code == 200:
            respuesta = r.json()
            return respuesta
    except Exception:
        messagebox.showerror(title="Error de conexion", message="No se puede obtener la cotizacion, intente mas tarde")
        caja_compra.insert(0,"NAN")
        caja_venta.insert(0,"NAN")

def borrar():
    caja_compra.delete(0,tk.END)
    caja_venta.delete(0,tk.END)

def cotizacionDolarOficial():
    borrar()
    respuesta = llamadaRequest()
    dolar_oficial_datos = respuesta[0]
    dolar_oficial_compra = dolar_oficial_datos['casa']['compra']
    caja_compra.insert(0,dolar_oficial_compra)
    dolar_oficial_venta = dolar_oficial_datos['casa']['venta']
    caja_venta.insert(0,dolar_oficial_venta)


def cotizacionDolarBlue():
    borrar()
    respuesta = llamadaRequest()
    dolar_blue_datos = respuesta[1]
    dolar_blue_compra = dolar_blue_datos['casa']['compra']
    caja_compra.insert(0,dolar_blue_compra)
    dolar_blue_venta = dolar_blue_datos['casa']['venta']
    caja_venta.insert(0,dolar_blue_venta)

def cotizacionDolarLiqui():
    borrar()
    respuesta = llamadaRequest()
    dolar_liqui_datos = respuesta[3]
    dolar_liqui_compra = dolar_liqui_datos['casa']['compra']
    caja_compra.insert(0,dolar_liqui_compra)
    dolar_liqui_venta = dolar_liqui_datos['casa']['venta']
    caja_venta.insert(0,dolar_liqui_venta)

def cotizacionDolarBolsa():
    borrar()
    respuesta = llamadaRequest()
    dolar_bolsa_datos = respuesta[4]
    dolar_bolsa_compra = dolar_bolsa_datos['casa']['compra']
    caja_compra.insert(0,dolar_bolsa_compra)
    dolar_bolsa_venta = dolar_bolsa_datos['casa']['venta']
    caja_venta.insert(0,dolar_bolsa_venta)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def apliacion():
    # Haciendo globales las variables
    global caja_compra
    global caja_venta
    
    # Ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title('Cotizaciones del dolar')
    ventana_principal.configure(width=640, height=260)
    ventana_principal.resizable(0,0)
    path = resource_path('logoDolares.ico')
    ventana_principal.iconbitmap(path)

    # Botones 

    btn_dolar_oficial = ttk.Button(text="Cotizacion dolar oficial",command=cotizacionDolarOficial)
    btn_dolar_oficial.place(x=10, y=50, width=140, height=40)
    btn_dolar_blue = ttk.Button(text='Cotizacion dolar blue',command=cotizacionDolarBlue)
    btn_dolar_blue.place(x=170, y=50, width=140, height=40)
    btn_dolar_liqui = ttk.Button(text='Cotizacion dolar liqui',command=cotizacionDolarLiqui)
    btn_dolar_liqui.place(x=330, y=50, width=140, height=40)
    btn_dolar_bolsa = ttk.Button(text='Cotizacion dolar bolsa',command=cotizacionDolarBolsa)
    btn_dolar_bolsa.place(x=490, y=50, width=140, height=40)

    # Caja

    caja_compra = ttk.Entry(font=('Arial Bold',15),foreground='red')
    caja_compra.place(x=100, y=170, width=100, height=40)
    caja_venta = ttk.Entry(font=('Arial Bold',15),foreground='green')
    caja_venta.place(x=430, y=170, width=100, height=40)

    # Label

    label_compra = ttk.Label(text='Compra:')
    label_compra.place(x=100, y=140)
    label_compra.config(font=("Arial Bold",15),foreground='red')
    label_venta = ttk.Label(text='Venta:')
    label_venta.place(x=430, y=140)
    label_venta.config(font=("Arial Bold",15),foreground='green')

    ventana_principal.mainloop()

#Ejercuto ventana
apliacion()