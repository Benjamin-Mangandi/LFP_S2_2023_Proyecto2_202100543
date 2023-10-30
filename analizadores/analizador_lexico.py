from analizadores import analizador_sintactico as AS
from objetos import errores
abecedario = [";","#","_","'","(",")","{", "}", "[", "]", ":", ",", '"', " ", "\n", "=", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2",
              "3", "4", "5", "6", "7", "8", "9", ".", "-", "á", "é", "í", "ó", "ú"]
errores_encontrados = []

def analizar(datos):
    global errores_encontrados
    columna = 1
    fila = 0
    nuevo_texto = datos
    for token in datos:
        fila = fila+1
        if token == "\n":
            columna = columna+1
            fila = 0
            continue
        if token.lower() not in abecedario:
            nuevo_texto = nuevo_texto.replace(token, "")
            aux_error = errores.error("Error Lexico", token, fila,columna)
            error_encontrado = {
                    "tipo": aux_error.tipo, "error": aux_error.lexema, "fila": aux_error.fila, "columna": aux_error.columna
                    }
            errores_encontrados.append(error_encontrado)
            continue
    return AS.analizar(nuevo_texto)