import os, sys
from math import *


def resumen_del_dia(l):
    Total=0
    c=0; m=0
    for i in range(len(l)):
        r = l[i]
        if r["tipo"]=="carro":
            c=c+1
            Total=Total+r["valor"]
        else:
            if r["tipo"]=="moto":
                m=m+1
                Total=Total+r["valor"]
    return {"total":Total,"carros":c,"motos":m}


def mayor_cobro(l):
    x = None
    for r in l:
        if x == None or r["valor"] > x:
            x = r["valor"]
    if x == None:
        return 0
    return x
