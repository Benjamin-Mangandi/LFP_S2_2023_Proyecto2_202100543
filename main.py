import tkinter
from tkinter import *
from tkinter import filedialog
import json
import subprocess
menu = tkinter.Tk()
menu.geometry("1200x700")
menu.config(bg="#262732")
menu.title("Analizador Sintactico")
frame_botones = tkinter.Frame(menu, background="#3D3D3F")
frame_botones.pack(side="top", fill="x")
boton_abrir = tkinter.Menu(menu)
boton_analizar = tkinter.Menu(menu)
reporte_boton = tkinter.Button(
    frame_botones, background="#0ECA19", height=2, width=2000, text="Proyecto 2 202100543")
scrollbar = Scrollbar(menu)
scrollbar.pack(side=RIGHT, fill=Y)
cuadro_texto = tkinter.Text(
    menu, height=35, width=75, yscrollcommand=scrollbar.set)
cuadro_texto.pack(side="left", padx=35)
scrollbar.config(command=cuadro_texto.yview)
cuadro_resultados = tkinter.Text(menu, height=35, width=60)
reporte_boton.pack(pady=15)
cuadro_resultados.pack(side="right", padx=35)
boton_abrir.add_cascade(label="Abrir")
boton_abrir.add_cascade(label="Analizar")
ruta_archivo = tkinter.StringVar()
menu.config(menu=boton_abrir)
menu.resizable(False, False)
menu.mainloop()
