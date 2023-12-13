import cv2
import numpy as np
import time


# Función para cargar la imagen con transparencia desde un archivo PNG
def cargar_imagen_transparente(ruta, dimensiones_deseadas=(640, 480)):
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    if imagen is not None:
        imagen = cv2.resize(imagen, dimensiones_deseadas)
    return imagen

# Función para superponer la imagen en el video
def superponer_imagen(video, imagen, posicion=(0, 0)):
    # Obtener las dimensiones del video
    altura, ancho, _ = video.shape

    # Obtener las dimensiones de la imagen
    altura_imagen, ancho_imagen, _ = imagen.shape

    # Calcular la posición en la que se superpondrá la imagen (centrado)
    x = (ancho - ancho_imagen) // 2
    y = (altura - altura_imagen) // 2

    # Crear una máscara para la región de interés en el video
    mascara = imagen[:, :, 3] / 255.0
    mascara = cv2.resize(mascara, (ancho_imagen, altura_imagen))

    # Superponer la imagen en el video
    for c in range(0, 2):
        video[y:y + altura_imagen, x:x + ancho_imagen, c] = \
            video[y:y + altura_imagen, x:x + ancho_imagen, c]*(1 - mascara) + \
            imagen[:, :, c]* mascara
    return video

# Capturar video desde la cámara web (cambiar 0 por el índice de la cámara si es necesario)
captura = cv2.VideoCapture(0)

# Configura la frecuencia de fotogramas deseada 
fps = 120
captura.set(cv2.CAP_PROP_FPS, fps)

# Redimensionar el video a 1080x1080
captura.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Cargar la imagen transparente y redimensionar a 1080x1080
ruta_imagen = 'Mira.png'
print(f'Ruta de la imagen: {ruta_imagen}')
imagen_superpuesta = cargar_imagen_transparente(ruta_imagen)

while True:

    # Capturar el fotograma actual
    ret, fotograma = captura.read()

    # Redimensionar el fotograma a 1080x1080
    fotograma = cv2.resize(fotograma, (640, 480))
            
    # Superponer la imagen en el fotograma
    fotograma_superpuesto = superponer_imagen(fotograma, imagen_superpuesta)
    # Mostrar el fotograma resultante
    cv2.imshow('Superposición de Imagen', fotograma_superpuesto)
    
    # Mostrar el fotograma resultante
    cv2.imshow('Superposición de Imagen', fotograma)

    # Salir del bucle si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar los recursos
captura.release()
cv2.destroyAllWindows()
