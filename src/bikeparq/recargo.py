def aplicar_recargo_nocturno(tarifa: int, hora_entrada: int) -> int:
    if hora_entrada < 0 or hora_entrada > 23:
        raise ValueError("La hora debe estar entre 0 y 23")
    if tarifa != 0 and (hora_entrada >= 20 or hora_entrada <= 5):
        return tarifa + 2000
    return tarifa
