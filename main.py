import tkinter
from tkinter import *
from tkinter import filedialog
import json
import subprocess
from analizadores import analizador_lexico as AL
from analizadores import analizador_sintactico as AS

def generar_tabla_html(data):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tabla de datos</title>
        <style>
            table {
                width: 80%;
                margin: 0 auto; /* Centrar la tabla en la página */
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #000; /* Líneas de separación */
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <table>
            <tr>
                <th>Tipo</th>
                <th>Lexema</th>
                <th>Fila</th>
                <th>Columna</th>
            </tr>
    """

    for row in data:
        html_content += f"""
            <tr>
                <td>{row['tipo']}</td>
                <td>{row['lexema']}</td>
                <td>{row['fila']}</td>
                <td>{row['columna']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """
    
    return html_content

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
    
def guardar(cuadro_texto):
    if ruta_archivo.get() == "":
        texto = cuadro_texto.get("1.0", END)
        archivo_guardado = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo_guardado:
            with open(archivo_guardado, "w") as archivo:
                archivo.write(texto)
    else:
        try:
            texto = cuadro_texto.get("1.0", END)
            with open(ruta_archivo.get(), "w") as archivo:
                archivo.write(texto)
        except Exception:
            print("No se pudo guardar el archivo")

def guardar_como(cuadro_texto):
    try:
        texto = cuadro_texto.get("1.0", END)
        archivo_guardado = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if archivo_guardado:
            with open(archivo_guardado, "w") as archivo:
                archivo.write(texto)
            ruta_archivo.set(archivo)
    except Exception:
        return
    
def salir():
    menu.destroy()

def analizar_texto(texto):
    cuadro_resultados.config(state="normal")
    resultados = AL.analizar(texto)
    cuadro_resultados.delete(1.0, END)
    for resultado in reversed(resultados):
        cuadro_resultados.insert(1.0, str("\n"+">>>>"+resultado))
    cuadro_resultados.config(state="disabled")


def reporte_tokens(data):
    contenido_html = generar_tabla_html(data)
    with open('tokens.html', 'w') as resultados:
        resultados.write(contenido_html)


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
reportes_boton.add_command(label="Reporte de Tokens", command=lambda: reporte_tokens(AS.tokens_leidos))
reportes_boton.add_command(label="Reporte de Errores", command=lambda: reporte_errores())
reportes_boton.add_command(label="Arbol de derivación", command=lambda: arbol())
botones_archivo.add_command(label="Abrir", command=lambda: abrir_archivo())
botones_archivo.add_command(label="Guardar", command=lambda: guardar(cuadro_texto))
botones_archivo.add_command(label="Guardar Como", command=lambda: guardar_como(cuadro_texto))
botones_archivo.add_command(label="Salir", command=lambda: salir())
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
