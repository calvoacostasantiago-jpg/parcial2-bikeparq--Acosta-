RECARGO_NOCTURNO = 2000
INICIO_NOCHE = 20
FIN_NOCHE = 5
HORA_MAXIMA = 23


def aplicar_recargo_nocturno(tarifa: int, hora_entrada: int) -> int:
    if not 0 <= hora_entrada <= HORA_MAXIMA:
        raise ValueError("La hora debe estar entre 0 y 23")
    if tarifa != 0 and (hora_entrada >= INICIO_NOCHE or hora_entrada <= FIN_NOCHE):
        return tarifa + RECARGO_NOCTURNO
    return tarifa
