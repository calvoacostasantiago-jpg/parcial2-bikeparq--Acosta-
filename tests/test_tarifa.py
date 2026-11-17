import pytest

from bikeparq.tarifa import calcular_tarifa


def test_cp01_carro_una_hora():
    assert calcular_tarifa(60, "carro") == 3000


def test_cp02_moto_ultimo_minuto_de_gracia():
    assert calcular_tarifa(10, "moto") == 0


def test_cp03_tipo_invalido():
    with pytest.raises(ValueError):
        calcular_tarifa(60, "bicicleta")
