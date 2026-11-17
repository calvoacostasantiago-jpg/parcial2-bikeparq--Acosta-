# NO MODIFIQUE ESTE ARCHIVO. Estas pruebas deben seguir pasando después del Punto 4.
from bikeparq.reportes import mayor_cobro, resumen_del_dia

REGISTROS = [
    {"tipo": "carro", "valor": 3000},
    {"tipo": "moto", "valor": 1500},
    {"tipo": "carro", "valor": 600},
    {"tipo": "bicicleta", "valor": 999},
]


def test_resumen_suma_solo_carros_y_motos():
    assert resumen_del_dia(REGISTROS) == {"total": 5100, "carros": 2, "motos": 1}


def test_resumen_de_un_dia_sin_registros():
    assert resumen_del_dia([]) == {"total": 0, "carros": 0, "motos": 0}


def test_mayor_cobro_del_dia():
    assert mayor_cobro(REGISTROS) == 3000


def test_mayor_cobro_sin_registros_es_cero():
    assert mayor_cobro([]) == 0
