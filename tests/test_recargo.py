import pytest

from bikeparq.recargo import aplicar_recargo_nocturno


def test_recargo_por_entrada_nocturna():
    assert aplicar_recargo_nocturno(3000, 22) == 5000


@pytest.mark.parametrize(
    "hora, esperado",
    [(0, 5000), (5, 5000), (6, 3000), (10, 3000), (19, 3000), (20, 5000), (23, 5000)],
)
def test_limites_de_horario(hora, esperado):
    assert aplicar_recargo_nocturno(3000, hora) == esperado


def test_sin_recargo_en_tiempo_de_gracia():
    assert aplicar_recargo_nocturno(0, 23) == 0


@pytest.mark.parametrize("hora", [-1, 24])
def test_hora_fuera_de_rango(hora):
    with pytest.raises(ValueError):
        aplicar_recargo_nocturno(3000, hora)
