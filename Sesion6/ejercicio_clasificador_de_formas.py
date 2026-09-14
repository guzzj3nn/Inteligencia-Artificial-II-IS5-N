import cv2
import numpy as np

# =====================================================================
# TALLER DE LABORATORIO: CLASIFICADOR DE FORMAS (PÁGINA 4)
# =====================================================================

# 1. Cargar la imagen original a color
nombre_archivo = 'Ejercicio 1 - Sesion1.jpeg'
img_color = cv2.imread(nombre_archivo)

if img_color is None:
    print(f"[ERROR]: No se pudo abrir la imagen '{nombre_archivo}'.")
else:
    # --- PIPELINE DE PROCESAMIENTO ---
    # Paso A: Conversión a escala de grises
    img_gris = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    # Paso B: Umbralsación binaria (Ajusta el umbral 120 según tu iluminación)
    _, img_bin = cv2.threshold(img_gris, 120, 255, cv2.THRESH_BINARY_INV)
    
    # Paso C: Limpieza Morfológica (Apertura para eliminar ruidos del fondo)
    kernel = np.ones((3, 3), np.uint8)
    img_limpia = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernel)
    
    # Paso D: Detección de Contornos Externos
    contornos, _ = cv2.findContours(img_limpia, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    print(f"Se encontraron un total de {len(contornos)} objetos potenciales.\n")
    
    # --- LOGICA DE NEGOCIO EMPRESARIAL ---
    # Definimos el umbral de área 'X' para separar objetos grandes de pequeños
    UMBRAL_AREA_X = 5000 
    
    img_resultado = img_color.copy()
    contador = 1

    for cnt in contornos:
        # 3. Calcular e imprimir el área en píxeles
        area = cv2.contourArea(cnt)
        
        # Filtro básico para ignorar ruido residual microscópico
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            
            # 4. Clasificación según la regla de negocio
            if area > UMBRAL_AREA_X:
                # Objeto Grande -> Bounding Box AZUL en BGR: (255, 0, 0)
                cv2.rectangle(img_resultado, (x, y), (x + w, y + h), (255, 0, 0), 2)
                tipo = "Grande (Azul)"
            else:
                # Objeto Pequeño -> Bounding Box ROJO en BGR: (0, 0, 1255)
                cv2.rectangle(img_resultado, (x, y), (x + w, y + h), (0, 0, 255), 2)
                tipo = "Pequeno (Rojo)"
                
            print(f"Objeto #{contador}: Area = {area:.1f} pixeles -> Clasificacion: {tipo}")
            contador += 1

    # Guardar el panel de análisis final
    cv2.imwrite('resultado_clasificador_formas.png', img_resultado)
    print("\n[PROCESO TERMINADO]: Imagen analizada guardada como 'resultado_clasificador_formas.png'.")
