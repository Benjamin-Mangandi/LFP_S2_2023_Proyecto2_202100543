# **Analizador Lexico y Sintactico**
## *Manual de usuario*
### **Segundo Semestre 2023**
# **Información General**
Esta aplicación tiene la finalidad de ser un analizador lexico y sintactico para el reconocimiento de distintas isntrucciones escritas por el usuario, la aplicacion consta de un cuadro de texto donde el usuario puede ingresar las distintas instrucciones o bien cargar un archivo *.BIZDATA*, el cuadro de la derecha representaria la consola de la aplicación, la cual serviria para imprimir los datos que necesite el usuario.
## **Inicio**
Al iniciar el programa se verá la siguiente ventana:
Tiene varias opciones que puedes escoger, el boton *archivo* sirve para que puedas cargar un archivo *.BIZDATA* ya existente en tu computadora al programa, guardar en un archivo el texto hecho en el programa o salir de la aplicación.
![inicio1](https://i.ibb.co/X31DQBq/Inicio.png)
![inicio2](https://i.ibb.co/94gBNFW/inicio2.png)
## **Analizar**
Al analizar el texto el programa reconocerá las instrucciones permitidas ingresadas por el usuario, al final el scaner, la aplicación mandará una notificación en dado caso haya algun error de tipo lexico o sintactico, en caso contrario le notificará al usuario que el analisis terminó.
![analizar](https://i.ibb.co/yRycnTd/inicio3.png)
![analizar2](https://i.ibb.co/xDzHqQ0/analizar.png)
## **Reportes**
Al terminar de analizar tu archivo, puedes presionar el boton ***Reportes***, el cual desplegará una serie de 3 opciones.
### **Reporte de Tokens**
Este reporte consta de los tokens leidos correctamente durante el analisis, la información que se brinda en este reporte es: el tipo de token leido, el token, la fila y columna en la que se encuentra.
### **Reporte de Errores**
Este reporte consta de los errores encontrados al momento de analizar las instrucciones, la información que se brinda en este reporte es: el tipo de error encontrado, el error, la fila y columna en la que se encuentra.
### **Arbol de Derivación**
Este reporte consta de las instrucciones leidas de manera grafica, y como las instrucciones se van derivando en más.