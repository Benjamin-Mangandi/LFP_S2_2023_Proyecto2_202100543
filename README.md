# **Lenguajes Formales y de Programación**
## *Segundo Proyecto*
### **Segundo Semestre 2023**

```js
Universidad San Carlos De Guatemala
Programador: Harold Benjamin Oxlaj Mangandi
Carne: 202100543
Lenguaje: Python, HTML
Bibliotecas usadas: graphviz, tkinter, subprocess, math
```
---
### Descripción del Proyecto
El siguiente proyecto es un analizador lexico y sintactico, el cual tiene como objetivo reconocer las instrucciones ingresadas por el usuario y desplegarlas en la consola de la aplicación, asi mismo el usuario puede generar reportes de tokens, errores y datos en formato HTML.
![gramatica](https://i.ibb.co/BG0bqSF/gramatica.jpg)
## Partes del Proyecto
### **Archivos y Carpetas**
### Carpeta Principal
# main.py
**Importa**: *analizador_lexico, analizador_sintactico, reportes, filedialog, tkinter*
![menu](https://i.ibb.co/ZSbvR50/menu.png)
![menu2](https://i.ibb.co/71YMHrT/menu2.png)
## **Funciones**
### *abrir_archivo*
Esta función permite abrir un archivo de texto al usuario por medio de la función de tkinter 
*filedialog.askopenfilename()* inserta el texto en el cuadro de texto y asigna la ruta a la variable *ruta_archivo*
![archivo](https://i.ibb.co/pft3XWD/abrir.png)
### *guardar*
**Parametros**: nombre del cuadro de texto
Esta función permite o bien sobreescribir el archivo si es que existe o crear uno nuevo y guardarlo con el nombre que desee el usuario por medio de una validación de la variable *ruta_archivo*, si es que contiene la ruta de un archivo abierto.
![guardar](https://i.ibb.co/z7YkbPd/guardar.png)
### *guardar_como*
**Parametros**: nombre del cuadro de texto
Esta función permite guardar como un archivo aparte el texto que el usuario haya ingresado y le asigna la ruta a la variable *ruta_archivo*
### *salir*
Esta funcion simplemente cierra la ventana junto con el proceso con la funcion *destroy()*
![guardar_salir](https://i.ibb.co/TgQ2y6N/guardar-como.png)
### *analizar_texto*
**Parametros**: texto del cuadro de texto
Esta funcion recibe como parametro el texto del cuadro de texto para mandarlo al analizador lexico, y obtener los resultados para imprimirlos en la consola de la aplicación
![analizar_texto](https://i.ibb.co/kxrxSvr/analizar-texto.png)
### *reporte_tokens*
**Parametros**: arreglo de tokens
Esta Función recibe como parametro un arreglo en donde estén los tokens leidos, se le pasa como arreglo a la función *generar_tabla_tokens_html* del **archivo reportes.py** para obtener el contenido html y realizar el archivo correspondiente.
![reporte](https://i.ibb.co/n1YvwZG/reporte-tokens.png)
### *reporte_errores*
**Parametros**: arreglo de errores
Esta Función recibe como parametro un arreglo en donde estén los errores encontrados, se le pasa como arreglo a la función *generar_tabla_errores_html* del **archivo reportes.py** para obtener el contenido html y realizar el archivo correspondiente.
![reporte_errores](https://i.ibb.co/1r4B68t/reporte-errores.png)
# reportes.py
## **Funciones**
### *generar_tabla_tokens_html*
**Parametros**: arreglo con los tokens leidos
Esta función realiza en formato HTML la tabla de tokens generada por el usuario y utiliza el arreglo de tokens leidos para las filas y retorna el contenido html para realizar el archivo
![tabla_tokens](https://i.ibb.co/0Vdm65B/tabla-tokens1.png)
![tabla_token2](https://i.ibb.co/wSVYwwc/tabla-tokens2.png)
### *generar_tabla_errores_html*
**Parametros**: arreglo con los errores encontrados
Esta función realiza en formato HTML la tabla de errores generada por el usuario y utiliza el arreglo de errores para las filas y retorna el contenido html para realizar el archivo
![tabla_errores](https://i.ibb.co/GHpkbKp/tabla-errores1.png)
![tabla_errore2](https://i.ibb.co/BNZSmsP/tabla-errores2.png)
### *generar_tabla_datos_html*
**Parametros**: arreglo de claves y arreglo de registros
Esta función realiza en formato HTML la tabla con los registros y las claves ingresadas por el usuario el arreglo de claves para las columnas y el arreglo de registros para las filas y retorna el contenido html para realizar el archivo
![tabla_datos](https://i.ibb.co/HzLs4md/tabla-datos.png)
![tabla_datos2](https://i.ibb.co/xL3Qk2M/tabla-datos2.png)

### analizadores
# analizador_lexico.py
**Importa**: *analizador_sintactico, errores*
Este archivo contiene todos los abecedarios que usa el analizador para validar caracteres y palabras.
## **Funciones**
### *analizar*
**Parametros**: texto del cuadro de texto
Esta función analiza el texto del cuadro de texto en busca de errores caracter a caracter; si encuentra un caracter que no esté en abecedario lo incluye como un error, y se suma al contador de errores, la fila y la columna.
Al terminar el analisis, le pasa el texto al analizador sintactico.
![analizar2](https://i.ibb.co/xLSgyCm/analizador-lexico.png)
# analizador_sintactico.py
**Importa**: *tokens, reportes*
Este se encarga de leer las instrucciones ingresadas por el usuario y si alguna de ellas coincide realiza la instruccion deseada.
## **Funciones**
### *Analizar*
**Parametros**: texto mandado del analizador lexico
Esta función recibe como parametro el texto resultante del analizador lexico, este lee las palabras reservadas ingresadas por el usuario y si las palabras coinciden realiza la accion correspondiente, esta acción se realiza por un *startswith* cada palabra reservada leida correctamente se ingresa al arreglo de los tokens leidos por medio de un objeto de tipo token y agregandolos a un diccionario.
Al leer un comentario este se ignora en el analizador, por eso puede venir cualquier cosa en un comentario ingresado por el usuario ya sea normal o multilinea.
Conforme se avanza en el texto, se aumenta ya sea la variable *fila* *columna*.
Si la instruccion se desea imprimir en la consola, se agrega en el arreglo *resultados* el cual se retorna para que este se imprima en la consola del sistema al final del analisis
Al final retorna los resultados para mostrarlos en la consola de la aplicación
![analizar3](https://i.ibb.co/Y7xVTTZ/analizar-sintactico.png)
![analizar4](https://i.ibb.co/p0gCVzn/analizar-sintactico2.png)
![analizar5](https://i.ibb.co/CKtJrX5/analizar-sintactico3.png)
![analizar6](https://i.ibb.co/rFMRxN5/analizar-sintactico4.png)
![analizar7](https://i.ibb.co/p2yJhXV/analizar-sintactico5.png)
![analizar8](https://i.ibb.co/HhhKPK0/analizar-sintactico6.png)
![analizar9](https://i.ibb.co/syMCX3T/analizar-sintactico7.png)
### objetos
# errores.py
# **Clase**: Error
Esta clase tiene como atributos *tipo*: que es el tipo de error encontrado, ya sea lexico o sintactico, *Error*: es el error en si mismo, el caracter o palabra no reconocido por el analizador, *fila*: es la fila donde se encuentra el error, *columna*: es la columna donde se encuentra el error. 
![error](https://i.ibb.co/Y2rb5yY/error.png)
# tokens.py
Esta clase tiene como atributos *tipo*: que es el tipo de token encontrado, *lexema*: es el caracter o palabra reservada reconocida por el analizador, *fila*: es la fila donde se encuentra el token, *columna*: es la columna donde se encuentra el token. 
# **Clase**: token
![token](https://i.ibb.co/bBn7m7z/token.png)