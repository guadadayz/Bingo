from src.bingo import carton

def contar_celdas_ocupadas():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda

    assert contador == 15

def test_no_menor_de_15():
    assert contar_celdas_ocupadas() => 15

def test_no_mayor_de_15():
    assert contar_celdas_ocupadas() =< 15

def test_columnas_ocupadas():
    mi_carton = carton()
    contador = 0
    for i in range(9):
        if not(mi_carton[0][i] or mi_carton[1][i] or mi_carton[2][i]):
            assert False
    assert True
