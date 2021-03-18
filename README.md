# Color Detection


1. [Importar librerías](#schema1)
2. [Tomar una imagen del usuario](#schema2)
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


# 3. Leer el .csv
Con `pd.read_csv()` leemos el csv, como vemos no tiene ningún nombre en las columnas se lo vamos a asignar.
![csv](./images/001.png)































(https://data-flair.training/blogs/project-in-python-colour-detection/)