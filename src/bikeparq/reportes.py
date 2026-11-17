def resumen_del_dia(registros):
    total = 0
    carros = 0
    motos = 0
    for registro in registros:
        tipo = registro["tipo"]
        if tipo == "carro":
            carros += 1
        elif tipo == "moto":
            motos += 1
        else:
            continue
        total += registro["valor"]
    return {"total": total, "carros": carros, "motos": motos}


def mayor_cobro(registros):
    return max((registro["valor"] for registro in registros), default=0)
