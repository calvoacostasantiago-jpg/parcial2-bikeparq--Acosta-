from bikeparq.recargo import aplicar_recargo_nocturno


def test_recargo_por_entrada_nocturna():
    assert aplicar_recargo_nocturno(3000, 22) == 5000
