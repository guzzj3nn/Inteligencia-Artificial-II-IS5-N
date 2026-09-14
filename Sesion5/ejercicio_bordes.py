import cv2
import numpy as np

# =====================================================================
# TALLER DE LABORATORIO: INSPECTOR DE BORDES (PÁGINA 4)
# =====================================================================

# 1. Cargar la imagen en escala de grises
nombre_archivo = 'Ejercicio 1 - Sesion1.jpeg'
imagen = cv2.imread(nombre_archivo, cv2.IMREAD_GRAYSCALE)

if imagen is None:
    print(f"[ERROR]: No se pudo abrir la imagen '{nombre_archivo}'.")
else:
    # 2. Generar Bordes usando Sobel X (Bordes Verticales) y Sobel Y (Horizontales)
    sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
    
    # Convertir a valores absolutos de 8 bits para guardar como imagen
    sobel_x_img = cv2.convertScaleAbs(sobel_x)
    sobel_y_img = cv2.convertScaleAbs(sobel_y)
    
    cv2.imwrite('sobel_x_verticales.png', sobel_x_img)
    cv2.imwrite('sobel_y_horizontales.png', sobel_y_img)
    print("1. Componentes Sobel X y Sobel Y guardadas.")

    # 4. Experimentación con el algoritmo Canny (Diferentes umbrales)
    
    # Configuración A: Umbrales bajos (Sensible, capta mucho ruido/texturas)
    canny_bajo = cv2.Canny(imagen, 10, 50)
    cv2.imwrite('canny_umbrales_10_50.png', canny_bajo)
    
    # Configuración B: Umbrales altos (Estricto, solo bordes muy marcados)
    canny_alto = cv2.Canny(imagen, 200, 250)
    cv2.imwrite('canny_umbrales_200_250.png', canny_alto)
    
    # Configuración C: Umbral estándar/óptimo sugerido
    canny_optimo = cv2.Canny(imagen, 50, 150)
    cv2.imwrite('canny_umbrales_50_150_optimo.png', canny_optimo)

    print("2. Experimentos de Canny procesados con éxito.")
    print("[TERMINADO]: Abre y compara los archivos .png generados a la izquierda.")
