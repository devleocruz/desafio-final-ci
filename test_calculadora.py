from calculadora import somar

def test_soma_positivos():
    assert somar(2, 3) == 5

def test_soma_numero_negativo():
    assert somar(-2, 3) == 1