import cv2
import numpy as np

# =====================================================================
# TALLER DE LABORATORIO 1: TRANSFORMACIÓN DE ESPACIOS
# =====================================================================

# 1. Crear un píxel BGR de prueba completamente amarillo intenso
# OpenCV usa el orden inverso: [Azul, Verde, Rojo]
pixel = np.array([0, 255, 255], dtype=np.uint8)

# 2. Calcular matemáticamente su valor en escala de grises usando NumPy
# Fórmula ponderada: Y = 0.299*R + 0.587*G + 0.114*B
# En nuestro arreglo 'pixel': pixel[2] es Rojo, pixel[1] es Verde, pixel[0] es Azul
gris_matematico = (0.299 * pixel[2]) + (0.587 * pixel[1]) + (0.114 * pixel[0])

# 3. Imprimir el resultado del cálculo en la terminal
print(f"1. Valor matemático calculado: {gris_matematico}")


# 4. Usar la función optimizada de OpenCV sobre la imagen real
try:
    # Cargamos el archivo usando su nombre exacto en el directorio raíz
    imagen = cv2.imread('Ejercicio 1 - Sesion1.jpeg')
    
    # Validamos si la imagen se cargó correctamente para evitar errores vacíos
    if imagen is None:
        print("[ERROR]: No se pudo abrir el archivo 'Ejercicio 1 - Sesion1.jpeg'.")
        print("Asegúrate de que el archivo esté guardado en la raíz de tu espacio de trabajo.")
    else:
        # Convertimos la imagen real a escala de grises
        img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        print("2. ¡Imagen real convertida a gris con éxito!")
        
        # NOTA DE ENTORNOS CLOUD: Reemplazamos cv2.imshow por cv2.imwrite
        # Debido a que Codespaces no cuenta con una interfaz de pantalla física,
        # guardamos el resultado como un nuevo archivo ejecutable.
        cv2.imwrite('resultado_gris.jpg', img_gris)
        print("¡Perfecto! La imagen se guardó correctamente como 'resultado_gris.jpg'.")
        print("Puedes abrirla haciendo clic sobre ella en el menú de la izquierda.")

except Exception as e:
    print(f"Ocurrió un error inesperado durante el procesamiento: {e}")
