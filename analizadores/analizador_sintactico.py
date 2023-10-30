import tkinter
from tkinter import *
from tkinter import filedialog
from objetos import tokens
import reportes as R
tk_cometario_multilinea = ["'",'"']
tk_comentario_normal = ["#"]
resultados = []
claves = []
registros = []
continuacion = ""
indice = 0
columna = 0
fila = 0
dentro_arreglo = False
comentario_junto = False
tokens_leidos = []
def analizar(datos):
    global registros
    global dentro_arreglo
    global claves
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
        fila = 0
        columna = columna+1
        if dentro_arreglo:
            if linea.startswith("]"):
                dentro_arreglo= False
                continue
            if linea.replace(" ", "").startswith("{"):
                if linea.endswith("}"):
                    aux = linea.replace(" ", "")
                    aux2 = aux[1:-1]
                    aux3 = aux2.split(",")
                    registros.append(aux3)
                    continue
        if linea.startswith("claves ="):
            if linea.endswith("]"):
                aux_tk = tokens.token("claves",linea[0:6],1,columna)
                token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
                tokens_leidos.append(token_leido)
                aux = linea[10:-1]
                aux_2 = aux.split(",")
                for dato in aux_2:
                    claves.append(dato.replace('"', ""))
            continue
        if linea.startswith("Registros ="):
            aux_tk = tokens.token("registros",linea[0:9],1,columna)
            token_leido = {
                "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            if linea.endswith("["):
                dentro_arreglo= True
                continue
            continue
        if linea.startswith('imprimir("'):
            if comentario_junto == False:
                aux_tk = tokens.token("imprimir",linea[:8],1,columna)
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
            aux_tk = tokens.token("imprimir_salto_linea",linea[0:10],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            comentario_junto=False
            resultados.append(linea[12:-3])
            continue
        if linea.startswith("datos"):
            aux_tk = tokens.token("datos",linea[0:5],1,columna)
            token_leido = {
                "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            texto_claves = ""
            texto_registros = ""
            for clave in claves:
                texto_claves=clave+texto_claves
            resultados.append(str(texto_claves))
            for sub_registro in registros:
                for registro in sub_registro:
                    texto_registros=registro+texto_registros
                resultados.append(texto_registros)
            continue
        if linea.startswith("conteo"):
            aux_tk = tokens.token("numero",linea[:6],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            resultados.append(str(len(registros)))
            continue
        if linea.startswith('exportarReporte("'):
            aux_tk = tokens.token("instrucción",linea[:15],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            try:
                nombre = linea[17:-3]
                contenido_html = R.generar_tabla_datos_html(claves, registros)
                with open(nombre+".html", 'w') as Tabla:
                    Tabla.write(contenido_html)
                    continue
            except Exception:
                return resultados
        if linea.startswith('promedio("'):
            aux_tk = tokens.token("numero",linea[:8],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            continue
        if linea.startswith('contarsi("'):
            aux_tk = tokens.token("numero",linea[:8],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            continue
        if linea.startswith('sumar("'):
            aux_tk = tokens.token("numero",linea[:5],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            continue
        if linea.startswith('max("'):
            aux_tk = tokens.token("numero",linea[:3],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            continue
        if linea.startswith('min("'):
            aux_tk = tokens.token("numero",linea[:3],1,columna)
            token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
            tokens_leidos.append(token_leido)
            continue
        for token in linea:
            fila=fila+1
            if comentario_multilinea:
                if token in tk_cometario_multilinea:
                    contador = contador+1
                    if contador == 3:
                        comentario_multilinea = False
                        contador = 0
                        continue
                continue
            if token in tk_comentario_normal:
                aux_tk = tokens.token("comentario", token,fila,columna)
                token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
                tokens_leidos.append(token_leido)
                break
            if token in tk_cometario_multilinea:
                aux_tk = tokens.token("comentario_multilinea",token,fila,columna)
                token_leido = {
                    "tipo": aux_tk.tipo, "lexema": aux_tk.lexema, "fila": aux_tk.fila, "columna": aux_tk.columna
                    }
                tokens_leidos.append(token_leido)
                contador = contador+1
                if contador == 3:
                    comentario_multilinea = True
                    contador = 0
                    break
                continue
            else:
                contador=0
    return resultados