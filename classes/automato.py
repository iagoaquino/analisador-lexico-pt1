sinais = "+-"
digitos = "1234567890"
ponto = "."
letras = "qwertyuioasdfghjklpzxcvbnm"
cont_int = 0
cadeia = "123ab23bac+1"
#definição classe estado
class Estado:
    def __init__(self):
        self.transicoes = []
        self.transicoes_estrela = []
    def mostrar_transicoes(self):
        print(self.transicoes)
    def mostrar_transicoes_estrela(self):
        print(self.transicoes_estrela)
#definição classe automato    
class Automato:
    def __init__(self,palavras,quant_estados):
        self.alfabeto = []
        self.estados = []
        self.estados_aceitacao = []
        for i in range(quant_estados):
            estado = Estado()
            self.estados.append(estado)
        for letra in palavras:
            if  letra not in self.alfabeto:
                self.alfabeto.append(letra)
#metodos   
    def adicionar_transicao(self,estado_atual,alfabeto,estado_transicao):
        if alfabeto in self.alfabeto and estado_transicao in range(len(self.estados)):
            transicao = []
            transicao.append(alfabeto)
            transicao.append(estado_transicao)
            self.estados[estado_atual].transicoes.append(transicao)
        else:
            print("alfabeto não aceito")

    def adicionar_transicao_estrela(self,estado_atual,alfabeto,estado_transicao):
        if alfabeto in self.alfabeto and estado_transicao in range(len(self.estados)):
            transicao = []
            transicao.append(alfabeto)
            transicao.append(estado_transicao)
            self.estados[estado_atual].transicoes_estrela.append(transicao)
        else:
            print("alfabeto não aceito") 

    def definir_aceitacao(self,num_estado):
        self.estados_aceitacao.append(num_estado)

    def finalizou_aceitou(self,estado_atual):
        if estado_atual in self.estados_aceitacao:
            return 1
        return 0

    def fazer_transicao(self,estado_atual,alfabeto):
        novo_estado = 0
        for i in range(len(self.estados[estado_atual].transicoes)):
            if alfabeto == self.estados[estado_atual].transicoes[i][0]:
                print("entrei")
                novo_estado = self.estados[estado_atual].transicoes[i][1]
                print(novo_estado)
        return novo_estado
    
    def fazer_transicao_estrela(self,estado_atual,alfabeto):
        for i in range(len(self.estados[estado_atual].transicoes_estrela)):
            for alfabeto in self.estados[estado_atual].transicoes_estrela[i]:
                return 1
        return 0
            
    def mostrar_alfabeto(self):
        print(self.alfabeto)

    def mostrar_tamanho_estados(self):
        print(len(self.estados))

automato_int = Automato("+-1234567890qwertyuioasdfghjklpzxcvbnm.",4)
for numero in digitos:
    automato_int.adicionar_transicao(0,numero,1)
    automato_int.adicionar_transicao(1,numero,1)
    automato_int.adicionar_transicao(2,numero,1)
for sinal in sinais:
    automato_int.adicionar_transicao(0,sinal,2)
for letra in letras:
    automato_int.adicionar_transicao_estrela(1,letra,3)
    automato_int.adicionar_transicao(2,letra,0)
estado_atual = 0
for letra in cadeia:
    estado_atual = automato_int.fazer_transicao(estado_atual,letra)
    if automato_int.fazer_transicao_estrela(estado_atual,letra) == 1:
            cont_int+=1
            estado_atual = 0
            automato_int.fazer_transicao(estado_atual,letra)
print(cont_int)
