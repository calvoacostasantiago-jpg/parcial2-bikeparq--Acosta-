PRECIO_POR_MINUTO = {"carro": 60, "moto": 30}
TOPE_DIARIO = {"carro": 25_000, "moto": 12_000}
MINUTOS_DE_GRACIA = 10
MINUTOS_MAXIMOS = 1440


def calcular_tarifa(minutos: int, tipo: str) -> int:
    """Devuelve lo que se cobra por `minutos` de permanencia de un vehículo `tipo`."""
    if tipo not in PRECIO_POR_MINUTO:
        raise ValueError(f"Tipo de vehículo no válido: {tipo}")
    if minutos < 0 or minutos > MINUTOS_MAXIMOS:
        raise ValueError("Los minutos deben estar entre 0 y 1440")
    if minutos <= MINUTOS_DE_GRACIA:
        return 0
    valor = (minutos - MINUTOS_DE_GRACIA) * PRECIO_POR_MINUTO[tipo]
    return min(valor, TOPE_DIARIO[tipo])
