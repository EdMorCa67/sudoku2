

def comprobar_filas(sudoku):
    for fila in sudoku:
        
        fila_sin_ceros = [num for num in fila ]
        if len(set(fila_sin_ceros)) < len(fila_sin_ceros):
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

    #"---------------Check filas ---------------"
    assert comprobar_filas(correcto) is True
    assert comprobar_filas(incorrecto1) is False
    assert comprobar_filas(incorrecto2) is True
    assert comprobar_filas(incorrecto3) is True
    assert comprobar_filas(incorrecto5) is True
    assert comprobar_filas(incorrecto6) is False