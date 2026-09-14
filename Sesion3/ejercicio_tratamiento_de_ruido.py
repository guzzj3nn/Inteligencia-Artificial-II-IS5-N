import cv2
import numpy as np

# =====================================================================
# TALLER DE LABORATORIO FINAL: MORFOLOGÍA MATEMÁTICA (PÁGINA 6)
# =====================================================================

# 1. Cargar la imagen directamente en escala de grises
# (Usa el archivo de la sesión anterior o el que tengas en tu directorio)
nombre_archivo = 'Ejercicio 1 - Sesion1.jpeg'
imagen_gris = cv2.imread(nombre_archivo, cv2.IMREAD_GRAYSCALE)

if imagen_gris is None:
    print(f"[ERROR]: No se encontró el archivo '{nombre_archivo}'.")
else:
    # 2. Binarización estática con un umbral que genere algo de ruido
    # Usamos un umbral intermedio (ej. 110) para rescatar imperfecciones
    _, original_binarizada = cv2.threshold(imagen_gris, 110, 255, cv2.THRESH_BINARY)
    cv2.imwrite('1_original_binarizada.png', original_binarizada)
    print("1. Imagen binarizada base guardada.")

    # 3. Construir un Elemento Estructurante (Kernel) de 3x3
    # Usamos una forma rectangular de unos, común para propósitos generales
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # 4. Operación morfológica de APERTURA (Erosión seguida de Dilatación)
    # Ideal para eliminar pequeños puntos blancos aislados en el fondo (ruido de sal)
    apertura = cv2.morphologyEx(original_binarizada, cv2.MORPH_OPEN, kernel)
    cv2.imwrite('2_resultado_apertura.png', apertura)
    print("2. Operación de Apertura guardada con éxito.")

    # 5. Operación morfológica de CIERRE (Dilatación seguida de Erosión)
    # Ideal para rellenar pequeños huecos negros dentro del objeto (ruido de pimienta)
    cierre = cv2.morphologyEx(original_binarizada, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite('3_resultado_cierre.png', cierre)
    print("3. Operación de Cierre guardada con éxito.")

    print("\n[PROCESO COMPLETADO]: Revisa los 3 archivos .png generados a la izquierda.")
