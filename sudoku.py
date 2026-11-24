
from src.comprobar_columna import comprobar_columna
from src.comprobar_cuadrado import comprobar_cuadrado
from src.comprobar_filas import comprobar_filas
from src.comprobar_numero import comprobar_numero


def sudoku(sudoku):
    return comprobar_cuadrado(sudoku) and comprobar_numero(sudoku) and comprobar_columna(sudoku) and comprobar_filas(sudoku)




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


    assert sudoku(correcto) is True
    assert sudoku(incorrecto1) is False
    assert sudoku(incorrecto2)is False
    assert sudoku(incorrecto4)is False
    assert sudoku(incorrecto5) is False
    assert sudoku(incorrecto6) is False