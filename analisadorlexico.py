from classes.automato import Automato
sinais = "+-"
digitos = "1234567890"
ponto = "."
letras = "qwertyuioasdfghjklpzxcvbnm"
cont_int = 0
cont_float = 0
cadeia = "123ab2.3bac+1+2.32.0"
#criação do automato que conta floats
automato_int = Automato("+-1234567890qwertyuioasdfghjklpzxcvbnm.",4)
for numero in digitos:
    automato_int.adicionar_transicao(0,numero,1)
    automato_int.adicionar_transicao(1,numero,1)
    automato_int.adicionar_transicao(2,numero,1)
for sinal in sinais:
    automato_int.adicionar_transicao(0,sinal,2)
    automato_int.adicionar_transicao_estrela(1,sinal,3)
for letra in letras:
    automato_int.adicionar_transicao_estrela(1,letra,3)
    automato_int.adicionar_transicao(2,letra,0)
automato_int.adicionar_transicao_estrela(1,".",3)
automato_int.definir_aceitacao(1)
estado_atual = 0
for letra in cadeia:
    estado_atual = automato_int.fazer_transicao(estado_atual,letra)
    if automato_int.fazer_transicao_estrela(estado_atual,letra) == 1:
            cont_int+=1
            estado_atual = 0
            print(letra)
            automato_int.fazer_transicao(estado_atual,letra)

if automato_int.finalizou_aceitou(estado_atual) == 1:
    cont_int+=1
#criando o automato que conta floats
automato_float = Automato("+-1234567890qwertyuioasdfghjklpzxcvbnm.",6)
automato_float.mostrar_alfabeto()
for numero in digitos:
    automato_float.adicionar_transicao(0,numero,1)
    automato_float.adicionar_transicao(1,numero,1)
    automato_float.adicionar_transicao(2,numero,1)
    automato_float.adicionar_transicao(3,numero,4)
    automato_float.adicionar_transicao(4,numero,4)
for sinal in sinais:
    automato_float.adicionar_transicao(0,sinal,2)
    automato_float.adicionar_transicao_estrela(4,sinal,3)
for letra in letras:
    automato_float.adicionar_transicao_estrela(4,letra,5)
    automato_float.adicionar_transicao(2,letra,0)
    automato_float.adicionar_transicao(1,letra,0)
    automato_float.adicionar_transicao(3,letra,0)
automato_float.adicionar_transicao(1,".",3)
automato_float.definir_aceitacao(4)
estado_atual = 0
for letra in cadeia:
    estado_atual = automato_float.fazer_transicao(estado_atual,letra)
    if automato_float.fazer_transicao_estrela(estado_atual,letra) == 1:
            cont_float+=1
            estado_atual = 0
            print(letra)
            automato_float.fazer_transicao(estado_atual,letra)
if automato_float.finalizou_aceitou(estado_atual) == 1:
    cont_float+=1
print("quantidade de inteiros: "+str(cont_int)+",quantidade de floats:"+str(cont_float))