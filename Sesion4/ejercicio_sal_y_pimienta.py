import cv2
import numpy as np

# =====================================================================
# TALLER DE LABORATORIO: ESTRATEGIAS DE SUAVIZADO (PÁGINA 4)
# =====================================================================

# 1. Cargar imagen base o generar una sintética si no existe una imagen
nombre_archivo = 'Ejercicio 1 - Sesion1.jpeg'
imagen_base = cv2.imread(nombre_archivo, cv2.IMREAD_GRAYSCALE)

if imagen_base is None:
    # Si no encuentra el archivo, crea una matriz gris base de 400x400
    imagen_base = np.ones((400, 400), dtype=np.uint8) * 50

# --- INYECCIÓN DE RUIDO SAL Y PIMIENTA (Para cumplir el punto 1 del taller) ---
imagen_ruidosa = imagen_base.copy()
h, w = imagen_ruidosa.shape
# Añadir sal (puntos blancos)
num_sal = int(0.05 * h * w)
for _ in range(num_sal):
    imagen_ruidosa[np.random.randint(0, h), np.random.randint(0, w)] = 255
# Añadir pimienta (puntos negros)
num_pimienta = int(0.05 * h * w)
for _ in range(num_pimienta):
    imagen_ruidosa[np.random.randint(0, h), np.random.randint(0, w)] = 0

cv2.imwrite('1_imagen_con_ruido.png', imagen_ruidosa)
print("1. Imagen con ruido generada y guardada.")

# --- 2. APLICACIÓN DE LOS FILTROS CON KERNEL DE 7x7 ---
k_size = 7

# Filtro de Media (Promedio simple)
blur_media = cv2.blur(imagen_ruidosa, (k_size, k_size))
cv2.imwrite('2_resultado_media.png', blur_media)

# Filtro Gaussiano
blur_gauss = cv2.GaussianBlur(imagen_ruidosa, (k_size, k_size), 0)
cv2.imwrite('3_resultado_gaussiano.png', blur_gauss)

# Filtro de Mediana
blur_mediana = cv2.medianBlur(imagen_ruidosa, k_size)
cv2.imwrite('4_resultado_mediana.png', blur_mediana)

print("2. Filtros procesados con éxito en formato 7x7.")
print("[TERMINADO]: Revisa los archivos .png creados en el menú de la izquierda.")
