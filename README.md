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
**Importa**: *analizador_lexico, graficador*
## **Funciones**
### *seleccionar_archivo*
**Parametros**: nombre del cuadro de texto
Esta función permite abrir un archivo de texto al usuario por medio de la función de tkinter 
*filedialog.askopenfilename()* inserta el texto en el cuadro de texto y reinicia los nodos anteriores si es que tuvieran datos de analisis anteriores por medio de la función *graficador.reiniciar()* y asigna la ruta a la variable *ruta_archivo*
![archivo](https://i.ibb.co/tBpNm9y/seleccionar-archivo.png)
### *guardar*
**Parametros**: nombre del cuadro de texto
Esta función permite o bien sobreescribir el archivo si es que existe o crear uno nuevo y guardarlo con el nombre que desee el usuario por medio de una validación de la variable *ruta_archivo*, si es que contiene la ruta de un archivo abierto.
![guardar](https://i.ibb.co/Qksqjkq/guardar.png)
### *guardar_como*
**Parametros**: nombre del cuadro de texto
Esta función permite guardar como un archivo aparte el texto que el usuario haya ingresado y le asigna la ruta a la variable *ruta_archivo*
### *salir*
Esta funcion simplemente cierra la ventana junto con el proceso con la funcion *destroy()*
![guardar_salir](https://i.ibb.co/fnnpsrD/guardar-como-y-salir.png)
### *buscando_errores*
**Parametros**: diccionario de errores
Esta funcion recibe como parametro un diccionario el cual contendra los errores del texto dentro de un arreglo, dependiendo la longitud del arreglo mostrará un mensaje de que no hay ningun error, o creará un archivo .json con los errores y lo abrirá con el bloc de notas.
![buscando_errores](https://i.ibb.co/NtS74XV/buscando-errores.png)
### *reporte_documento*
Esta funcion determina si hay operaciones ingresadas por el usuario por medio de una condicion con la varible del archivo **analizador_lexico** *datos_validados* si los hay grafica normalmente, si no, manda una advertencia al usuario.
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
Esta clase tiene como atributos *tipo*, que es tipo de operación aritmetica, *valor1*, que es el primer valor ingresado, *valor2* que es el segundo valor ingresado, *resultado* que es el resultado de la operacion aritmetica dado los dos valores.
![operacion](https://i.ibb.co/Lxy3mJs/operacion.png)
## **Funciones**
### *operar*
**Parametros**: tipo de operacion, valor 1 y valor2
Esta funcion opera los dos valores ingresados teniendo como condición el tipo de operacion, por ejemplo, si el tipo de operación es "suma" suma los dos valores, o si es division, divide los dos valores asegurandose que no sea 0 el segundo.
Redondea todas las operaciones a 4 decimales.
![operar1](https://i.ibb.co/JR9T6dX/operar1.png)
![operar2](https://i.ibb.co/27XQjDx/operar2.png)
![operar3](https://i.ibb.co/ryngrCr/operar3.png)
![operar4](https://i.ibb.co/gd0dNQk/operar4.png)
# tokens.py
# **Clase**: token
Esta clase tiene como atributos *texto*, que es el nombre que se le dará al documento, *fondo*, que es color de los nodos, *fuente*, que es color de la letra y *forma* que es la forma que tendra los nodos.
![estilo_grafico](https://i.ibb.co/3RBPfrC/estilo-grafico.png)