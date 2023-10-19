from analizadores import analizador_sintactico as AS
abecedario = [";","#","_","'","(",")","{", "}", "[", "]", ":", ",", '"', " ", "\n", "=", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
              "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2",
              "3", "4", "5", "6", "7", "8", "9", ".", "-", "á", "é", "í", "ó", "ú"]
arreglo_errores = []

def analizar(datos):
    columna = 1
    fila = 0
    nuevo_texto = datos
    for token in datos:
        fila = fila+1
        if token == "\n":
            columna = columna+1
            fila = 0
        if token.lower() not in abecedario:
            nuevo_texto = nuevo_texto.replace(token, "")
            arreglo_errores.append(token)
    AS.analizar(nuevo_texto)