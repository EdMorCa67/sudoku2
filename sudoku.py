def comprobar_cuadrado(sudoku):
    filas = len(sudoku) 
    for col in sudoku :
        if len(col) != filas:
            return False
    return True   

def comprobar_enteros(sudoku):

    for fila in sudoku:
        for col in fila:
            if type(col) == str:
                return False
            elif not col % 1 == 0:
                return False

    return True


def comprobar_filas(sudoku):
    for fila in sudoku:
        
        fila_sin_ceros = [num for num in fila ]
        if len(set(fila_sin_ceros)) < len(fila_sin_ceros):
            return False
    return True 

def comprobar_columna(sudoku):
    for columna in zip(*sudoku):
        columna_sin_ceros = [num for num in columna ]
        if len(set(columna_sin_ceros)) < len(columna_sin_ceros):
            return False
    return True        


def comprobar_rango(sudoku):
    numeros_validos = range(1 , len(sudoku) +1 )
    for fila in sudoku:
        for numero in fila:
            if numero not in numeros_validos:
                return False
    return True

if __name__ == "__main__":

    correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

    incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

    incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

    incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

    incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

    incorrecto5 = [[1, 1.5],
               [1.5, 1]]

    incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]
    # "----------CUADRADOS------------")
    assert comprobar_cuadrado(correcto)is True
    assert comprobar_cuadrado(correcto) is True
    assert comprobar_cuadrado(incorrecto1) is True
    assert comprobar_cuadrado(incorrecto2)is True
    assert comprobar_cuadrado(incorrecto3)is True
    assert comprobar_cuadrado(incorrecto5)is True
    assert comprobar_cuadrado(incorrecto6)is False
    #"-----ENTEROS---------")
    #---------------------------------------------
    assert comprobar_enteros(correcto) is True
    assert comprobar_enteros(incorrecto1) is True
    assert comprobar_enteros(incorrecto2)is True
    assert comprobar_enteros(incorrecto4)is False
    assert comprobar_enteros(incorrecto5) is False
    assert comprobar_enteros(incorrecto6) is True
    #"---------------Check filas ---------------"
    assert comprobar_filas(correcto) is True
    assert comprobar_filas(incorrecto2) is True
    assert comprobar_filas(incorrecto3) is True
    assert comprobar_filas(incorrecto5) is True
    assert comprobar_filas(incorrecto6) is False
    #-----------------columnas-----------------
    assert comprobar_columna(correcto) is True
    assert comprobar_columna(incorrecto1) is False
    assert comprobar_columna(incorrecto2)is False
    assert comprobar_columna(incorrecto4)is True
    assert comprobar_columna(incorrecto5) is True
    assert comprobar_columna(incorrecto6) is False
    #---------------------rango-------------------
    assert comprobar_rango(correcto) is True
    assert comprobar_rango(incorrecto1) is True
    assert comprobar_rango(incorrecto2)is True
    assert comprobar_rango(incorrecto4)is False
    assert comprobar_rango(incorrecto5) is False
    assert comprobar_rango(incorrecto6) is False
    #--------------------check_num----------------
    assert comprobar_numero(correcto) is True
    assert comprobar_numero(incorrecto1) is False
    assert comprobar_numero(incorrecto2)is False
    assert comprobar_numero(incorrecto4)is False
    assert comprobar_numero(incorrecto5) is False
    assert comprobar_numero(incorrecto6) is False

    assert sudoku(correcto) is True
    assert sudoku(incorrecto1) is False
    assert sudoku(incorrecto2)is False
    assert sudoku(incorrecto4)is False
    assert sudoku(incorrecto5) is False
    assert sudoku(incorrecto6) is False