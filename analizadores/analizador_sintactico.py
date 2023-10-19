def analizar(datos):
    contador = 0
    lineas = datos.splitlines()
    comentario_multilinea = False
    for linea in lineas:
        for caracter in linea:
            if comentario_multilinea:
                if caracter == "'":
                    contador = contador+1
                    if contador == 3:
                        comentario_multilinea = False
                        contador = 0
                        continue
                if caracter == '"':
                    contador = contador+1
                    if contador == 3:
                        comentario_multilinea = False
                        contador = 0
                        continue
                continue
            if caracter == "#":
                print(linea)
                break
            if caracter == "'":
                contador = contador+1
                if contador == 3:
                    comentario_multilinea = True
                    contador = 0
                    break
                continue
            if caracter == '"':
                contador = contador+1
                if contador == 3:
                    comentario_multilinea = True
                    contador = 0
                    break
                continue
            else:
                contador=0
