import pytest
from Tarea1 import basic_operations
from Tarea1 import count_char
# test para funcion basic_operations


@pytest.mark.parametrize(

    # permite relizar varias evaluaciones en una misma funcion
    # se definen variables de entrada y la esperada
    "op1,op2,operac, expected",
    # diferentes valores a probar en la funcion
    [(1, 2, 1, 3), (2, 3, 1, 5),
     (3, 5, 1, 7), (1, 2, 2, -1),
     (8, 3, 2, 5), (5, 3, 2, 3),
     (5, 2, 3, 2), (6, 3, 3, 2),
     (40, 5, 3, 5)]
    )
# define funcion de test_basic_operations
def test_basic_operations(op1, op2, operac, expected):
    # permite evaluar las distintas combinaciones
    # en la funcion solicitada e indicar error
    assert basic_operations(op1, op2, operac) == expected

# test para funcion basic_operations error string como entrada
# permite relizar varias evaluaciones en una misma funcion


@pytest.mark.parametrize(
    # se definen variables de entrada y la esperada
    "op1,op2,operac, expected",
    # diferentes valores a probar en la funcion
    [("a", 2, 1, 3), (2, 3, 1, 5),
     (1, "s", 2, -1), (8, 3, 2, 5),
     (5, 3, "h", 2), (6, 3, 3, 2),
     (40, "f", 3, 8)]
    )
# define funcion de test_basic_operations_error
def test_basic_operations_error(op1, op2, operac, expected):
    # permite evaluar las distintas combinaciones
    #  en la funcion solicitada e indicar error
    assert basic_operations(op1, op2, operac) == expected

    # test para funcion basic_operations cero en division
    # permite relizar varias evaluaciones en una misma funcion


@pytest.mark.parametrize(
    # se definen variables de entrada y la esperada
    "op1,op2,operac, expected",
    # diferentes valores a probar en la funcion
    [(9, 0, 3, 3), (14, 7, 3, 2),
     (10, 0, 3, 5), (15, 3, 3, 5)]
    )
# define funcion de test_basic_operations_cero
def test_basic_operations_cero(op1, op2, operac, expected):
    assert basic_operations(op1, op2, operac) == expected

# test para funcion count_char conteo
# permite relizar varias evaluaciones en una misma funcion


@pytest.mark.parametrize(
    # se definen variables de entrada y la esperada
    "oracn, conteo",
    # diferentes valores a probar en la funcion
    [("sofia", 5), ("casa", 2), ("ave", 5)]
    )
# define funcion de
# test_count_char_conteo
def test_count_char_conteo(oracn, conteo):
    # permite evaluar las distintas combinaciones
    #  en la funcion solicitada e indicar error
    assert count_char(oracn) == conteo

    # test para funcion count_char no string
    # permite relizar varias evaluaciones en una misma funcion


@pytest.mark.parametrize(
    # se definen variables de entrada y la esperada
    "oracn, conteo",
    [("sofia", 5), ("casa", 4), (85, 2)]
    )
# define funcion de test_countChar_valido
def test_countChar_valido(oracn, conteo):
    # permite evaluar las distintas combinaciones
    # en la funcion solicitada e indicar error
    assert count_char(oracn) == conteo
