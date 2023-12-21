import cv2
import numpy as np

def cargar_imagen_transparente(ruta, dimensiones_deseadas=(640, 480)):
    imagen = cv2.imread(ruta, cv2.IMREAD_UNCHANGED)
    if imagen is not None:
        imagen = cv2.resize(imagen, dimensiones_deseadas)
    return imagen

captura = cv2.VideoCapture(1)
fps = 120
captura.set(cv2.CAP_PROP_FPS, fps)
captura.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ruta_imagen = 'Mira.png'
imagen_superpuesta = cargar_imagen_transparente(ruta_imagen)

# Toma de dimensiones fuera del bucle
altura, ancho, _ = captura.read()[1].shape
altura_imagen, ancho_imagen, _ = imagen_superpuesta.shape
x = (ancho - ancho_imagen) // 2
y = (altura - altura_imagen) // 2

# Operación de superposición de imagen fuera del bucle
mascara_expanded = np.expand_dims(imagen_superpuesta[:, :, 3] / 255.0, axis=2)
imagen_superpuesta_ponderada = imagen_superpuesta[:, :, :3] * mascara_expanded

while True:
    ret, fotograma = captura.read()

    # Muestra el mismo resultado de superposición de imagen en cada fotograma
    fotograma[y:y+altura_imagen, x:x+ancho_imagen, :] = \
        fotograma[y:y+altura_imagen, x:x+ancho_imagen, :] * (1 - mascara_expanded) + \
        imagen_superpuesta_ponderada

    cv2.imshow('Superposición de Imagen', fotograma)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

captura.release()
cv2.destroyAllWindows()
