import tkinter
from tkinter import *
from tkinter import filedialog
import json
import subprocess
from analizadores import analizador_lexico as AL


def abrir_archivo():
    try:
        archivo = filedialog.askopenfilename(title="Seleccionar un archivo")
        with open(archivo, "r") as archivo_cargado:
            texto = archivo_cargado.read()
        cuadro_texto.delete(1.0, END)
        cuadro_texto.insert(1.0, texto)
        ruta_archivo.set(archivo)
    except Exception:
        return


def analizar_texto(texto):
    AL.analizar(texto)


def reporte_tokens():
    print("tokens")


def reporte_errores():
    print("errores")


def arbol():
    print("arbolito")


menu = tkinter.Tk()
menu.geometry("1200x700")
menu.config(bg="#262732")
menu.title("Analizador Sintactico")
frame_botones = tkinter.Frame(menu, background="#3D3D3F")
frame_botones.pack(side="top", fill="x")
botones = tkinter.Menu(menu)
botones_archivo =tkinter.Menu(botones, tearoff=0)
reportes_boton = tkinter.Menu(botones, tearoff=0)
reportes_boton.add_command(label="Reporte de Tokens", command=lambda: reporte_tokens())
reportes_boton.add_command(label="Reporte de Errores", command=lambda: reporte_errores())
reportes_boton.add_command(label="Arbol de derivación", command=lambda: arbol())
botones_archivo.add_command(label="Abrir", command=lambda: abrir_archivo())
botones_archivo.add_command(label="Guardar", command=lambda: reporte_errores())
botones_archivo.add_command(label="Guardar Como", command=lambda: arbol())
botones_archivo.add_command(label="Salir", command=lambda: arbol())
boton = tkinter.Button(
    frame_botones, background="#0ECA19", height=2, width=2000, text="Proyecto 2 202100543")
scrollbar = Scrollbar(menu)
scrollbar.pack(side=RIGHT, fill=Y)
cuadro_texto = tkinter.Text(
    menu, height=35, width=75, yscrollcommand=scrollbar.set)
cuadro_texto.pack(side="left", padx=35)
scrollbar.config(command=cuadro_texto.yview)
cuadro_resultados = tkinter.Text(menu, height=35, width=60, state="disabled")
boton.pack(pady=15)
cuadro_resultados.pack(side="right", padx=35)
botones.add_cascade(label="Abrir", menu=botones_archivo)
botones.add_cascade(
    label="Analizar", command=lambda: analizar_texto(cuadro_texto.get("1.0", END)))
botones.add_cascade(label="Reportes", menu=reportes_boton)
ruta_archivo = tkinter.StringVar()
menu.config(menu=botones)
menu.resizable(False, False)
menu.mainloop()
