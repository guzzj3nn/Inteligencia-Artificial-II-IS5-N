import cv2
import matplotlib.pyplot as plt

# =====================================================================
# TALLER DE LABORATIO 2: ANÁLISIS ESTADÍSTICO (PÁGINA 5)
# =====================================================================

# 1. Cargar la imagen RGB usando el nombre del archivo en la raíz
imagen = cv2.imread('Ejercicio 1 - Sesion1.jpeg')

if imagen is None:
    print("[ERROR]: No se pudo abrir la imagen. Revisa el nombre del archivo.")
else:
    # 2. Separar la imagen en sus 3 canales individuales (B, G, R)
    # OpenCV entrega los canales en orden: 0=Azul, 1=Verde, 2=Rojo
    canales = cv2.split(imagen) 
    
    colores_lineas = ('b', 'g', 'r') # Colores que usará Matplotlib para dibujar
    nombres_canales = ('Canal Azul (B)', 'Canal Verde (G)', 'Canal Rojo (R)')

    # Configurar las dimensiones y etiquetas del gráfico
    plt.figure(figsize=(10, 5))
    plt.title("Histogramas Superpuestos por Canal de Color")
    plt.xlabel("Intensidad del Píxel (0 al 255)")
    plt.ylabel("Cantidad de Píxeles con esa Intensidad")

    # 3 y 4. Calcular el histograma de cada canal y graficarlos juntos
    for i, color in enumerate(colores_lineas):
        # cv2.calcHist(imágenes, canales, máscara, tamaño_bins, rangos)
        hist = cv2.calcHist([imagen], [i], None, [256], [0, 256])
        
        # Dibujar la línea en el gráfico
        plt.plot(hist, color=color, label=nombres_canales[i], linewidth=2)
        plt.xlim([0, 256])

    plt.legend() # Muestra la cajita con los nombres de cada color
    plt.grid(True, linestyle='--', alpha=0.5) # Agrega una cuadrícula de fondo

    # NOTA DE ENTORNOS CLOUD: Como estamos en Codespaces, no podemos usar plt.show()
    # porque causaría un error de pantalla. En su lugar, guardamos el gráfico como imagen.
    plt.savefig('grafico_histogramas.png', dpi=300, bbox_inches='tight')
    print("¡Perfecto! El análisis estadístico ha terminado.")
    print("El gráfico se guardó como 'grafico_histogramas.png' en tu menú izquierdo.")
