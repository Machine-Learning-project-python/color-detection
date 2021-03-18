from cv2 import cv2
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
data = pd.read_csv('./data/colors.csv', names = index, header = None)

#coordenadas x, y donde hace click el raton
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

#función para calcular la distancia mínima de todos los colores y obtener el color más coincidente
def getColorName(R,G,B):
    minimun = float("inf")
    colorName = ""
    #minimun = 10000
    for i in range(len(data)):
        distance = abs(R -int(data.loc[i,"R"])) + abs(G -int(data.loc[i, "G"])) + abs(B- int(data.loc[i,"B"]))
        if (distance <= minimum):
            minimun = distance
            colorName = data.loc[i,"color_name"]
            
    return colorName


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):
    
    cv2.imshow("image",img)
    if (clicked):
        
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        
        #Creating text string to display( Color name and RGB values )
        
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        

        #For very light colours we will display text in black colour
        if(r + g + b >= 600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
                    
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break


cv2.destroyAllWindows()
