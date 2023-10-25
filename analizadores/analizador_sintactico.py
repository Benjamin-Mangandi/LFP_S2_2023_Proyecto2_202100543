import tkinter
from tkinter import *
from tkinter import filedialog
from objetos import tokens
tk_cometario_multilinea = ["'",'"']
tk_comenario_normal = ["#"]
tk_abecedario = ["a", "b", "c", "d"]
tk_variables = ["claves", "registros", "="]
tk_funciones = ["imprimir"]
resultados = []
continuacion =""
indice = 0
columna = 0
fila = 0
comentario_junto = False
tokens_leidos = []
def analizar(datos):
    global fila
    global columna
    global indice
    global continuacion
    global comentario_junto
    resultados.clear()
    contador = 0
    lineas = datos.splitlines()
    comentario_multilinea = False
    for linea in lineas:
        columna = columna+1
        if linea.startswith('imprimir("'):
            if comentario_junto == False:
                aux_tk = tokens.token("instrucción",linea[:8],fila,columna)
                token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
                tokens_leidos.append(token_leido)
                continuacion = linea[10:-3]
                resultados.append(linea[10:-3])
                indice = resultados.index(continuacion)
                comentario_junto = True
                continue
            else:
                comentario_completo = str(continuacion+linea[10:-3])
                resultados.pop(indice)
                resultados.insert(indice,comentario_completo)
                continue
        if linea.startswith('imprimirln("'):
            comentario_junto=False
            resultados.append(linea[12:-3])
            print(resultados)
            continue
        for token in linea:
            if comentario_multilinea:
                if token in tk_cometario_multilinea:
                    contador = contador+1
                    if contador == 3:
                        comentario_multilinea = False
                        contador = 0
                        continue
                continue
            if token in tk_comenario_normal:
                print(linea)
                break
            if token in tk_cometario_multilinea:
                contador = contador+1
                if contador == 3:
                    comentario_multilinea = True
                    contador = 0
                    break
                continue
            else:
                contador=0
    return resultados