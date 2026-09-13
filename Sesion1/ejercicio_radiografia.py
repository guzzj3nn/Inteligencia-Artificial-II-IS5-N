import numpy as np

# 1. Crear la matriz de prueba 5x5 simulando una radiografía sobreexpuesta
np.random.seed(42) 
matriz_original = np.random.randint(200, 255, (5, 5))

# 2. Aplicar los parámetros lineales (Reducción de contraste 50% y brillo -50)
alpha = 0.5
beta = -50.0
matriz_procesada = (alpha * matriz_original) + beta

# 3. Asegurar los límites con np.clip() y convertir a tipo np.uint8
matriz_procesada = np.clip(matriz_procesada, 0, 255).astype(np.uint8)

# 4. Imprimir los resultados para comparar
print("=== MATRIZ ORIGINAL (SOBREEXPUESTA) ===")
print(matriz_original)
print("\n=== MATRIZ PROCESADA (CON AJUSTE) ===")
print(matriz_procesada)

