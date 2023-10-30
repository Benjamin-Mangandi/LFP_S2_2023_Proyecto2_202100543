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
## Partes del Proyecto
### **Archivos y Carpetas**
### Carpeta Principal
# main.py
**Importa**: *analizador_lexico, analizador_sintactico*
![menu](https://i.ibb.co/ZSbvR50/menu.png)
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
![reporte](https://i.ibb.co/1r4B68t/reporte-errores.png)
# reportes.py
### analizadores
## **Funciones**
### *analizar*
# analizador_lexico.py
Este archivo contiene todos los abecedarios que usa el analizador para validar caracteres y palabras.
## **Funciones**
### *analizar*
**Parametros**: texto del cuadro de texto
Esta función analiza el texto del cuadro de texto en busca de errores caracter a caracter; si encuentra un caracter que no esté en abecedario lo incluye como un error, y se suma al contador de errores, la fila y la columna.
Al terminar el analisis, le pasa el texto al analizador sintactico.
![analizar2](https://i.ibb.co/k3MwPbV/analizar2.png)
# analizador_sintactico.py
## **Funciones**
### *Analizar*
**Parametros**: texto mandado del analizador lexico
Esta funcion grafica los nodos creados por medio de la funcion *render()* y le da nombre al documento por medio del parametro ingresado que es en donde se guardan los datos del estilo en la posicion 0 y lo abre en un archivo pdf
![analizar3](https://i.ibb.co/fFzns3y/reinicar-graficar.png)
### objetos
# errores.py
# **Clase**: Error
Esta clase tiene como atributos *tipo*: que es el tipo de error encontrado, ya sea lexico o sintactico, *Error*: es el error en si mismo, el caracter o palabra no reconocido por el analizador, *fila*: es la fila donde se encuentra el error, *columna*: es la columna donde se encuentra el error. 
![error](https://i.ibb.co/Y2rb5yY/error.png)
# tokens.py
Esta clase tiene como atributos *tipo*: que es el tipo de token encontrado, *lexema*: es el caracter o palabra reservada reconocida por el analizador, *fila*: es la fila donde se encuentra el token, *columna*: es la columna donde se encuentra el token. 
# **Clase**: token
![token](https://i.ibb.co/bBn7m7z/token.png)