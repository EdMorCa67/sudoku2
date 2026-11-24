


def comprobar_enteros(sudoku):

    for fila in sudoku:
        for col in fila:
            if type(col) != int:
                return False
            elif col % 1 != 0:
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

    #"-----ENTEROS---------")
    #---------------------------------------------
    assert comprobar_enteros(correcto) is True
    assert comprobar_enteros(incorrecto1) is True
    assert comprobar_enteros(incorrecto2)is True
    assert comprobar_enteros(incorrecto4)is False
    assert comprobar_enteros(incorrecto5) is False
    assert comprobar_enteros(incorrecto6) is True