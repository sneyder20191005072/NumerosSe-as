# Se realizo un programa para leer por camara web los gesto de una mano y decir que numero en lenguaje de señas es el correspondiente
![image](https://user-images.githubusercontent.com/81379348/137372530-eadfb942-5a91-466f-846b-6530878ed7c0.png)

# al ejecutar el archivo numero.py aparece la camara web en el cual se hace el numero con la mano derecha y  hay aparece el numero correspondiente al lenguaje de señas
![image](https://user-images.githubusercontent.com/81379348/137372842-9099b683-84e6-47af-b2bf-d76378fb0857.png)

# se pudo diferenciar cada gesto primero diferenciando en cada programa la parte de leer las manos y dibujarles puntos despues se diferencio el numero que le otorga la libreria mediapipe
![image](https://user-images.githubusercontent.com/81379348/137372317-e75167d3-e3c9-4848-b407-23b061a6000c.png)

# a los puntos de interes de la mano y se vio que la punta de los dedos tienen un numero se metio el correspondiente a los 5 dedos a un arreglo
![image](https://user-images.githubusercontent.com/81379348/137372993-fc771aa1-fd68-4f43-8259-0e4c99b63dbd.png)


# para diferenciar que dedo si un dedo se baja es cuando el numero correspondiente es menor o al numero de la falange del correspondiente dedo que en cada dedo es -2  entonces por posicion solo se le resto 2 al eje de las x

![image](https://user-images.githubusercontent.com/81379348/137373107-75988be9-4445-4edb-879e-2bf1cca9c455.png)

#  para el pulgar como este la punta del dedo no alcanza a bajar se opto por saber la posicion ya que cuando el dedo esta "cerrado" se corre hacia la izquierda de suposicion inicial entonces se utilizo esto para saber la posicion del pulgar.
![image](https://user-images.githubusercontent.com/81379348/137373325-2e9f5b79-e15c-4ca9-9e80-c6dc07ad73bd.png)

# cuando los dedos estaban abiertos se les asigno un 1 
![image](https://user-images.githubusercontent.com/81379348/137373520-cf59ea4c-bd55-4e38-a527-ebd33e9903fb.png)
![image](https://user-images.githubusercontent.com/81379348/137373673-09de0760-e884-4310-82d9-f019cc7f88e1.png)

# y cuando no un 0 
![image](https://user-images.githubusercontent.com/81379348/137373560-8b80b950-b6e1-45f0-87de-c39c701d5800.png)
![image](https://user-images.githubusercontent.com/81379348/137373723-bc300dd4-76ba-4ec0-b3e5-9aa24365bfa6.png)



# ya con esto se hicieron una serie de condicionales para saber que dedos se cierran para  cada numero correspondiente al lenguaje de señas y se agrego una imagen ilustrativa que sale cada vez que se realiza un numero.
