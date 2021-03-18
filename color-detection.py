import cv2
import numpy as np
import pandas as pd
import argparse

#Tomar una imagen del usuario
'''
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']
'''



#Leemo el csv y le asignamos el nombre a las columnas
index = ["color", "color_name", "hex", "R", "G", "B"]
data = pd.read_csv('./data/colors.csv', names = index, header = None)
print(data.head())
