import pytest

from bikeparq.tarifa import calcular_tarifa


@pytest.mark.parametrize("minutos", [-1, 1441])
def test_minutos_fuera_de_rango(minutos):
    with pytest.raises(ValueError):
        calcular_tarifa(minutos, "carro")


def test_tope_diario():
    assert calcular_tarifa(1440, "carro") == 25000
