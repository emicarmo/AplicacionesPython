""" Etapa3
Para finalizar con nuestro proyecto integrador:
Migrar las tres funcionalidades del programa
(agregar alumno, ver la cantidad de cursos de un
alumno y ver la lista completa) a una aplicación
de escritorio. La información se seguirá
mostrando en la consola. 
El botón Ver lista de alumnos debe mostrar la
lista de los alumnos en la consola.
Agregar a la lista debe agregar un nuevo
alumno al diccionario con el nombre y la cantidad
de cursos ingresados en las cajas de texto
correspondientes.
Ver cantidad de cursos debe mostrar el número
de cursos asociados al nombre ingresado en la
primera caja de texto.
"""

import tkinter as tk

def convertir(valor):
    if valor.isdecimal():
        valor = int(valor)
    else:
        valor = 'error'
    return valor

def verificar(dato):
    if dato.strip() == '':
        dato = 'error'
    return dato

def agregar_lista():
    nombre = caja_nombre.get()
    nombre = verificar(nombre)
    cursos = caja_cursos.get()
    cursos = convertir(cursos)
    caja_nombre.delete(0, 'end')
    caja_cursos.delete(0, 'end')    
    if nombre == 'error':
        print('Error!! Nombre vacio')
    elif cursos == 'error':
        print('Error!! El ingreso de cursos debe ser solo numeros')
    else:
        lista_alumnos[nombre] = cursos
        print('Alumno ingresado correctamente')

def ver_lista():
    print('Lista de alumnos:')
    for nombre in lista_alumnos:
        cursos = lista_alumnos[nombre]
        print(nombre + ' - ' + str(cursos) + ' cursos')

def ver_cursos():
    nombre = caja_nombre.get()
    caja_nombre.delete(0, 'end')
    if nombre in lista_alumnos:
        print(nombre + ' tiene ' + str(lista_alumnos[nombre]) + ' cursos')
    else:
        print('Ese alumno no tiene cursos')


lista_alumnos = {}

ventana = tk.Tk()
ventana.config(width=400, height=300)
ventana.title('Proyecto integrador')

btn_lista_alumnos = tk.Button(text='Ver lista de alumnos', command=ver_lista)
btn_lista_alumnos.place(x=10, y=10)
btn_agregar_lista = tk.Button(text='Agregar a la lista', command=agregar_lista)
btn_agregar_lista.place(x=10, y=140)
btn_cantidad_cursos = tk.Button(text='Ver cantidad de cursos', command=ver_cursos)
btn_cantidad_cursos.place(x=120, y=140)
btn_finalizar_app = tk.Button(text='Finalizar programa', command=ventana.quit)
btn_finalizar_app.place(x=10, y=200)

label_nombre_alumno = tk.Label(text='Nombre alumno:')
label_nombre_alumno.place(x=10, y=55)
label_cursos_alumno = tk.Label(text='Cursos:')
label_cursos_alumno.place(x=10, y=90)

caja_nombre = tk.Entry()
caja_nombre.place(x=110, y=55)
caja_cursos = tk.Entry()
caja_cursos.place(x=110, y=90, width=50)

ventana.mainloop()