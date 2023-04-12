from tkinter import W


entrada = "+5a3b2.5345a232a2"
lexemas = []
numeros = "0123456789"
simbolo = "+-"
ponto = "."
def automato(estado_atual,alfabeto,cont_int,cont_float,lexema):
    if estado_atual == 0:
        for i in numeros:
            if alfabeto == i:
                lexema = lexema+str(alfabeto)
                return 1, cont_int,cont_float,lexema
        for i in simbolo:
            if alfabeto == i:
                lexema = lexema+str(alfabeto)
                return 2, cont_int,cont_float,lexema
    if estado_atual == 1:
        for i in numeros:
            if alfabeto == i:
                lexema = lexema+str(alfabeto)
                return 1, cont_int,cont_float,lexema
        if alfabeto == ponto:
            lexema = lexema+str(alfabeto)
            return 4, cont_int,cont_float,lexema
        else:
            lexemas.append(lexema)
            lexema = ""
            estado_atual = 3
            cont_int+=1
    if estado_atual == 2:
        for i in numeros:
            if alfabeto == i:
                lexema = lexema+str(alfabeto)
                return 1, cont_int,cont_float,lexema
        return 0, cont_int,cont_float,lexema
    if estado_atual == 4:
        for i in numeros:
            if alfabeto == i:
                lexema = lexema+str(alfabeto)
                return 4, cont_int,cont_float,lexema
        lexemas.append(lexema)
        lexema = ""
        cont_float+=1
        estado_atual = 3
    if estado_atual == 3:
        estado_atual = 0
        estado_atual,cont_int,cont_float,lexema = automato(estado_atual,alfabeto,cont_int,cont_float,lexema)
    return estado_atual,cont_int,cont_float,lexema


def main():
    cont_int = 0
    cont_float = 0
    estado_atual = 0
    lexema = ""
    for i in entrada:
        alfabeto = i
        estado_atual,cont_int,cont_float,lexema = automato(estado_atual,alfabeto,cont_int,cont_float,lexema)
    if estado_atual == 1:
        cont_int+=1
        lexemas.append(lexema)
    if estado_atual == 4:
        cont_float+=1
        lexemas.append(lexema)
    print("inteiros contados: "+str(cont_int)+" , floats contados: "+str(cont_float))
    print(lexemas)           
main()
