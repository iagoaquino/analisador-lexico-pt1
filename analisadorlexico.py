from tkinter import W


entrada = "+5a3b2.5345a2"
numeros = "0123456789"
simbolo = "+-"
ponto = "."
def automato(estado_atual,alfabeto,cont_int,cont_float):
    print("estado atual: "+str(estado_atual)+",alfabeto: "+str(alfabeto))
    if estado_atual == 0:
        for i in numeros:
            if alfabeto == i:
                return 1, cont_int,cont_float
        for i in simbolo:
            if alfabeto == i:
                return 2, cont_int,cont_float
    if estado_atual == 1:
        for i in numeros:
            if alfabeto == i:
                return 1, cont_int,cont_float
        if alfabeto == ponto:
            return 4, cont_int,cont_float
        else:
            estado_atual = 3
            cont_int+=1
    if estado_atual == 2:
        for i in numeros:
            if alfabeto == i:
                return 1, cont_int,cont_float
        return 0, cont_int,cont_float
    if estado_atual == 4:
        for i in numeros:
            if alfabeto == i:
                return 4, cont_int,cont_float
        cont_float+=1
        estado_atual = 3
    if estado_atual == 3:
        estado_atual = 0
        estado_atual,cont_int,cont_float = automato(estado_atual,alfabeto,cont_int,cont_float)
    return estado_atual,cont_int,cont_float


def main():
    cont_int = 0
    cont_float = 0
    estado_atual = 0
    for i in entrada:
        alfabeto = i
        estado_atual,cont_int,cont_float = automato(estado_atual,alfabeto,cont_int,cont_float)
    if estado_atual == 1:
        cont_int+=1
    if estado_atual == 4:
        cont_float+=1
    print("inteiros contados: "+str(cont_int)+" , floats contados: "+str(cont_float))             
main()
