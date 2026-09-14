import numpy as np

# 1. Definir la matriz de la Imagen (I) y el Kernel de realce (K)
I = np.array([
    [100, 100, 100],
    [100, 200, 100],
    [100, 100, 100]
], dtype=np.float32)

K = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

# 2. Calcular el producto Hadamard (multiplicación elemento a elemento)
matriz_resultante = I * K

# 3. Sumar todos los valores para obtener el valor del píxel central
pixel_central = np.sum(matriz_resultante)

# Mostrar resultados
print("Matriz producto Hadamard:")
print(matriz_resultante)
print("\nValor del píxel central procesado:", pixel_central)