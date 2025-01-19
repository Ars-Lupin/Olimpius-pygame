import random

class Efeito:
    def __init__(self, nome, duracao, chance_aplicar):
        self.nome = nome
        self.duracao = duracao
        self.chance_aplicar = chance_aplicar

    def aplicar_efeito(elemento, personagem):
        if elemento and random.randint(1, 100) <= elemento.efeito.chance_aplicar:
            elemento.efeito.aplicar(personagem)

    def verificar(self, personagem):
        pass


class Queimadura(Efeito):
    def __init__(self):
        super().__init__(nome="Queimadura", duracao=3, chance_aplicar=75)

    def verificar(self, personagem):
        personagem.vida -= 20  # Dano contínuo
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)


class Molhado(Efeito):
    def __init__(self):
        super().__init__(nome="Molhado", duracao=3, chance_aplicar=80)

    def verificar(self, personagem):
        personagem.mana -= 5  # Reduz recuperação de mana
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)


class Eletrocutado(Efeito):
    def __init__(self):
        super().__init__(nome="Eletrocutado", duracao=3, chance_aplicar=45)

    def verificar(self, personagem):
        if random.randint(1, 100) <= 35:
            personagem.perde_turno = True
        personagem.vida -= 15
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)


class Cegueira(Efeito):
    def __init__(self):
        super().__init__(nome="Cegueira", duracao=2, chance_aplicar=60)

    def verificar(self, personagem):
        personagem.ataque_mira = False
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)


class Enraizado(Efeito):
    def __init__(self):
        super().__init__(nome="Enraizado", duracao=2, chance_aplicar=65)

    def verificar(self, personagem):
        personagem.velocidade = max(0, personagem.velocidade - 30)  # Reduz velocidade
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)


class ControleMental(Efeito):
    def __init__(self):
        super().__init__(nome="Controle Mental", duracao=2, chance_aplicar=50)

    def verificar(self, personagem):
        personagem.controlado = True
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)
            personagem.controlado = False
            
class Bebado(Efeito):
    def __init__(self):
        super().__init__(nome="Bebado", duracao=2, chance_aplicar=60)

    def verificar(self, personagem):
        personagem.forca = -15
        personagem.velocidade = -10
        personagem.resistencia = -5
        personagem.magia = -5
        personagem.vigor = -10
        personagem.controle = -30
        
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.efeitos.remove(self)
            personagem.controlado = False
