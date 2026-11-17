# Pasos del BDD. Los pasos que ya están aquí funcionan: no los cambie.
from pytest_bdd import given, parsers, scenarios, then, when

from bikeparq.tarifa import calcular_tarifa

scenarios("cobro.feature")


@given(parsers.parse('un vehículo tipo "{tipo}"'), target_fixture="vehiculo")
def vehiculo(tipo):
    return {"tipo": tipo}


@when(parsers.parse("permanece {minutos:d} minutos"))
def permanece(vehiculo, minutos):
    vehiculo["cobro"] = calcular_tarifa(minutos, vehiculo["tipo"])


@then(parsers.parse("el cobro es de {cobro:d} pesos"))
def cobro_esperado(vehiculo, cobro):
    assert vehiculo["cobro"] == cobro


# PUNTO 3: agregue aquí los pasos de sus escenarios del recargo nocturno.
