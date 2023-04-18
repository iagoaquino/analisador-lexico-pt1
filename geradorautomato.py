from classes.automato import Automato
texto = "aabbabababa"
def criar_automato_padrao(padrao,alfabeto):
    automato_padrao = Automato(alfabeto,len(padrao)+1)
    for pos in range(len(padrao)):
        if pos == 0:
            automato_padrao.adicionar_transicao(pos,padrao[pos],pos+1)
            for letra in alfabeto:
                if letra != padrao[pos]: 
                    automato_padrao.adicionar_transicao(pos,letra,pos)   
        elif pos == 1:
            automato_padrao.adicionar_transicao(pos,padrao[pos],pos+1)
            automato_padrao.adicionar_transicao(pos,padrao[pos-1],pos)
            for letra in alfabeto:
                if letra != padrao[pos] and letra !=padrao[pos-1]:
                    automato_padrao.adicionar_transicao(pos,letra,0)
        else:
            automato_padrao.adicionar_transicao(pos,padrao[pos],pos+1)
            for letra in alfabeto:
                if letra != padrao[pos]:
                    automato_padrao.adicionar_transicao(pos,letra,0)
    automato_padrao.definir_aceitacao(len(padrao))
    return automato_padrao

def main():
    automato = criar_automato_padrao("aba","qazwsxedcrfvtgbyhnujmik,ol.pç;~/1234567890-=")
    cont_padrao = 0
    estado_atual = 0
    automato.mostrar_aceitacao()
    for letra in texto:
        print("estado_antes: "+str(estado_atual)+", letra: "+letra)
        estado_atual = automato.fazer_transicao(estado_atual,letra)
        print("estado_depois: "+str(estado_atual)+", letra: "+letra)
        if automato.finalizou_aceitou(estado_atual) == 1:
            cont_padrao += 1
            estado_atual = 0
    print(cont_padrao)

main()