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
![reporte](https://i.ibb.co/RQwqTQ8/reporte-documento.png)
### analizadores
# analizador_lexico.py
Este archivo contiene todos los abecedarios que usa el analizador para validar caracteres y palabras.
## **Funciones**
### *analizar*
**Parametros**: texto del cuadro de texto
Esta función analiza el texto del cuadro de texto en busca de errores, y al mismo tiempo reiniciar la grafica por medio de la funcion *reiniciar()*y los errores de archivos anteriores.
analiza caracter a caracter el texto brindado y si encuentra un caracter que no esté en abecedario lo incluye como un error, y se suma al contador de errores, la fila y la columna.
al terminar lee las configuraciones del archivo de texto para la grafica y sus nodos y lo guarda en el arreglo *datos_estilo*.
![analizar1](https://i.ibb.co/HpZxhxk/analizar1.png)
![analizar2](https://i.ibb.co/k3MwPbV/analizar2.png)
por medio de un ciclo for lee cada operacion ingresada por el usuario mediante el texto y validando si los nombres de las claves son los correctos, al llegar a los valores, verifica si hay solo un valor o dos, y si un valor es en realidar un arreglo con mas valores, en ese caso manda a llamar a la funcion *sub_operacioes()* recibiendo el valor retornado por la funcion en la variable *resultado*  si no entonces manda a llamar a la funcion *operar()* e igualmente recibiendo el valor en la variable *resultado*; con los valores verificados se crea una variable de tipo **operacion**, se guarda en el arreglo *datos_validados* y se mandan como parametros para la funcion *crear_nodos()*
![analizar3](https://i.ibb.co/vz5tPqY/analizar3.png)
![analizar4](https://i.ibb.co/FJmjXXt/analizar4.png)
Al terminar de verificar las operaciones pueden occurir dos casos, si el arreglo de errores está vacio manda un notificacion al usuario informandole que no hay ningún error, y si hay por lo menos un error, manda una advertencia de que se encontraron errores y que puede pulsar el boton *"ver errores"* en el menú principal
![analizar5](https://i.ibb.co/5MtyR9M/analizar5.png)
### *sub_operaciones*
**Parametros**: posicion del arreglo 1, posicion del arreglo 2, arreglo de operaciones, operacion, nombre de la clave
Esta función realiza las subo-peracion que requiera el usuario al validar que los nombres de las claves sean correctos y dependiendo que si un valor es otro arreglo o no, si es un valor manda a operar los valores con la función *operar()* de la clase **operacion** si es un arreglo, manda a llamar a la funcion *sub_sub_operaciones*
![sub_operaciones](https://i.ibb.co/Pwr8kWT/sub-operar1.png)
![sub_operaciones2](https://i.ibb.co/J5Sw3N1/sub-operar2.png)
### *sub_sub_operaciones*
**Parametros**: posicion del arreglo 1, posicion del arreglo 2, arreglo de operaciones, operacion, nombre de la clave
Esta funcion sigue el mismo principio que la anterior, realiza las sub-operaciones que requiera la funcion anterior con los datos recolectados de la funcion anterior, y dependiendo si un valor es un arreglo o no, manda a llamar a la funcion *operar()* para validar los datos.
![sub2_operaciones](https://i.ibb.co/87RKhDT/sub-sub-operar.png)
![sub2_operaciones2](https://i.ibb.co/tLyPTgd/sub-sub-operar2.png)
# analizador_sintactico.py
## **Funciones**
### *reiniciar*
Esta funcion simplemente reinicia los nodos ya creados en analisis anteriores por medio de *clear()*
### *graficar*
**Parametros**: arreglo
Esta funcion grafica los nodos creados por medio de la funcion *render()* y le da nombre al documento por medio del parametro ingresado que es en donde se guardan los datos del estilo en la posicion 0 y lo abre en un archivo pdf
![reiniciar y graficar](https://i.ibb.co/fFzns3y/reinicar-graficar.png)
### *crear_nodo*
**Parametros**: arreglo, numero, clave_numerica, varible de tipo estilo.
esta funcion crea y le da el estilo a los nodos, tiene una condicion con la clave numerica, si es igual a 1 es que solo se crean 2 nodos para esa operacion por medio de una funcion *node()* y la funcion *edge()* para unirlos, si es 0, se hacen 3 nodos para una operacion con su respectivo estilo.
![crear_nodo](https://i.ibb.co/fXVDPYF/crear-nodo.png)

### objetos
# errores.py
# **Clase**: Error
Esta clase tiene como atributos *tipo*: que es el tipo de error encontrado, ya sea lexico o sintactico, *Error*: es el error en si mismo, el caracter o palabra no reconocido por el analizador, *fila*: es la fila donde se encuentra el error, *columna*: es la columna donde se encuentra el error. 
![error](https://i.ibb.co/Y2rb5yY/error.png)
# tokens.py
Esta clase tiene como atributos *tipo*: que es el tipo de token encontrado, *lexema*: es el caracter o palabra reservada reconocida por el analizador, *fila*: es la fila donde se encuentra el token, *columna*: es la columna donde se encuentra el token. 
# **Clase**: token
![token](https://i.ibb.co/bBn7m7z/token.png)