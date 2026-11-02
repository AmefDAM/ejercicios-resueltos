# Dada una lista de lista representando una matriz n*n:
# Define una rutina que devuelve True si la entrada es una matriz indentidad
# y False en otro caso.

# Una matriz identidad es una matriz cuadrada en la que todos los elementos
# en la diagonal principal son 1 y el resto de elementos fuera de la
# diagonal principal son 0. 
# (Una matriz cuadrada es una matriz con el numero de filas
# igual al numero de columnas)

def esMatrizCuadrada(matrix):
    return len(matrix) == len(matrix[0])


def esMatrizIdentidad(matrix):
    # Escribe aqui tu codigo
    if esMatrizCuadrada(matrix):
        filas = 0
        while filas < len(matrix):
            columnas = 0
            while columnas < len(matrix[filas]):
                if columnas == filas:
                    if matrix[filas][columnas] != 1:
                         return False
                else:
                    if matrix[filas][columnas] != 0:
                        return False
                columnas += 1
            filas += 1
    else:
         return False
    return True



# Casos test:

if __name__ == '__main__':
    # Test Cases:

assert esMatrizIdentidad([[1,0,0,0],
                          [0,1,0,0],
                          [0,0,1,0],
                          [0,0,0,1]]) is True
#>>>True

assert esMatrizIdentidad([[1,0,0],
                          [0,1,0],
                          [0,0,0]]) is False
#>>>False

assert esMatrizIdentidad([[2,0,0],
                          [0,2,0],
                          [0,0,2]]) is False
#>>>False

assert esMatrizIdentidad([[1,0,0,0],
                          [0,1,0,2],
                          [0,0,1,0],
                          [0,0,0,1]]) is False
#>>>False

assert esMatrizIdentidad([[1,-1,1],
                          [0,0,0,1]]) is False
#>>>False

assert esMatrizIdentidad([[1,0,0,0,0,0,0,0,0]]) is False
#>>>False

assert esMatrizIdentidad([[0,1,0],
                          [0,0,1]]) is False
#>>>False


# Casos test que no satisfacen la precondición
# de que la matriz sea cuadrada:

assert esMatrizIdentidad([[1,0,0,0],
                          [0,1,1,0],
                          [0,0,0,1]]) is False
#>>>False

assert esMatrizIdentidad([[1,0,0,0,0,0,0,0,0]]) is False
#>>>False

print("All tests passed")