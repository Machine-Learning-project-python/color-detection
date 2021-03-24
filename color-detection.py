import cv2
import numpy as np
import pandas as pd
import argparse
import matplotlib.pyplot as plt

#Tomar una imagen del usuario
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

#Leer la imagen con opencv
img = cv2.imread(img_path)

#declaración de variables globales
clicked = False
r = g = b = xpos = ypos = 0


#Leemos el csv y le asignamos el nombre a las columnas
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('./data/colors.csv', names = index, header = None)

#coordenadas x, y donde hace doble click izquierdo del raton, event =7
def draw_function(event, x,y,flags,param):
   
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(event, event == cv2.EVENT_LBUTTONDBLCLK )
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
        

#función para calcular la distancia mínima de todos los colores y obtener el color más coincidente
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)
cv2.imshow("image",img)
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
