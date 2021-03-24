# Color Detection
![img](./images/003.png)

0. [Ejecutar archivo](#schema0)
1. [Importar librerías](#schema1)
2. [Tomar una imagen del usuario](#schema2)
3. [Leer el .csv](#shema3)
4. [Establecer un evento de devolución de llamada del mouse en una ventana](#schema4)
5. [Crea la función draw_function](#schema5)
6. [Obtener el color](#schema6)
7. [Leer la imagen con opencv](#schema7)
8. [Declaración de variables globales](#schema8)
9. [Main del programa](#schema9)

<hr>

<a name="schema0"></a>

# 0. Ejecutar archivo
~~~
python color-detection.py -i colorpic.jpg
~~~
<hr>

<a name="schema1"></a>

# 1. Importar librerías
~~~python
import cv2
import numpy as np
import pandas as pd
import argparse

~~~
<hr>

<a name="schema2"></a>

# 2. Tomar una imagen del usuario
Estamos usando la biblioteca `argparse` para crear un analizador de argumentos. Podemos dar directamente una ruta de imagen desde el símbolo del sistema.

~~~python
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
~~~
<hr>

<a name="schema3"></a>

# 3. Leer el .csv
Con `pd.read_csv()` leemos el csv, como vemos no tiene ningún nombre en las columnas se lo vamos a asignar.
![csv](./images/001.png)
~~~python
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('./data/colors.csv', names = index, header = None)
~~~
![csv](./images/002.png)

<hr>

<a name="schema4"></a>

# 4. Establecer un evento de devolución de llamada del mouse en una ventana
Primero, creamos una ventana en la que se mostrará la imagen de entrada. Luego, configuramos una función de devolución de llamada que se llamará cuando ocurra un evento de mouse.
~~~python
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)
~~~
<hr>

<a name="schema5"></a>


# 5. Crea la función draw_function
Calculará los valores rgb del píxel en el que hacemos doble clic. Los parámetros de la función tienen el nombre del evento, las coordenadas (x, y) de la posición del mouse, etc. En la función, verificamos si se hace doble clic en el evento, luego calculamos y configuramos los valores r, g, b junto con x, y posiciones del ratón.

~~~python
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
~~~
<hr>

<a name="schema6"></a>

# 6. Obtener el color

~~~python
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname
~~~
<hr>

<a name="schema7"></a>

# 7. Leer la imagen con opencv
~~~python
img = cv2.imread(img_path)
~~~
<hr>

<a name="schema8"></a>

# 8. Declaración de variables globales
~~~python
clicked = False
r = g = b = xpos = ypos = 0
~~~
<hr>

<a name="schema9"></a>

# 9. Main del programa

~~~python
while(1):
    
    cv2.imshow("image",img)
    if (clicked):
        #crear un rectaángulo
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Crear el texto a mostrar
        text = getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)
        
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
  
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
    #romper el bucle con ESC 
    if cv2.waitKey(20) & 0xFF ==27:
        break


cv2.destroyAllWindows()

~~~

















(https://data-flair.training/blogs/project-in-python-colour-detection/)
(https://www.pyimagesearch.com/2014/06/02/opencv-load-image/)
(https://medium.com/@MeerAjaz/the-function-is-not-implemented-6804e9b38b06)