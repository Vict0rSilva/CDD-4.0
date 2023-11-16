class Pessoas:
#Metodo  construtor
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.paroudeComer = False
        self.falando = False
        self.paroudeFalar = False
        self.dormindo = False
        self.paroudeDormir = False

    def comer(self,comida):
        if self.comendo == True:
            print(f"{self.nome} ja esta comendo {comida}")
        else:
            print(f"{self.nome} foi comer, {comida}")
            self.comendo = True
    def parardeComer(self):
        if self.paroudeComer == False:
            print(f"{self.nome} ja parou de comer")
        else:
            print(f"{self.nome} parou de comer")
            self.paroudeComer = False

    def falar(self):
        if self.falando == True:
            print(f"{self.nome} falou")
        else:
            print(f"{self.nome} Esta falando")
            self.falando = True

    def paroudeFalar(self):
        if self.paroudeFalar == False:
            print(f"{self.nome} ja parou de Falar")
        else:
            print(f"{self.nome} parou de falar")
            self.paroudeFalar = False

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} ja esta domindor")
        else:
            print(f"{self.nome} Foi dormir ")
            self.dormindo = True

    def paroudeDormir(self):
        if self.dormindo == False:
            print(f"{self.nome} parou de domir")
        else:
            print(f"{self.nome} acordou ")
            self.dormindo = False