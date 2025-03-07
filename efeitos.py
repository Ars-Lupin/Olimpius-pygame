import random

class Efeito:
    def __init__(self, nome, duracao, chance_aplicar):
        self.nome = nome
        self.duracao = duracao
        self.chance_aplicar = chance_aplicar

    def aplicar(self, personagem):
        if random.randint(1, 100) <= self.chance_aplicar:
            personagem.efeitos.append(self)

    def verificar(self, personagem):
        pass
    
    def remover_efeito(self, personagem):
        if self in personagem.efeitos:
            personagem.efeitos.remove(self)

# ---------------------- EFEITOS ----------------------

class Queimadura(Efeito):
    DANO = 20
    DURACAO = 3
    CHANCE = 85

    def __init__(self):
        super().__init__("Queimadura", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.vida -= self.DANO
        self.duracao -= 1
        if self.duracao <= 0:
            self.remover_efeito(personagem)

class Molhado(Efeito):
    PERDA_MANA = 5
    DURACAO = 3
    CHANCE = 80

    def __init__(self):
        super().__init__("Molhado", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.mana -= self.PERDA_MANA
        self.duracao -= 1
        if self.duracao <= 0:
            self.remover_efeito(personagem)

class Eletrocutado(Efeito):
    DANO = 15
    PERDE_TURNO_CHANCE = 35
    DURACAO = 3
    CHANCE = 45

    def __init__(self):
        super().__init__("Eletrocutado", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        if random.randint(1, 100) <= self.PERDE_TURNO_CHANCE:
            personagem.perde_turno = True
        personagem.vida -= self.DANO
        self.duracao -= 1
        if self.duracao <= 0:
            self.remover_efeito(personagem)

class Cegueira(Efeito):
    DURACAO = 2
    CHANCE = 60

    def __init__(self):
        super().__init__("Cegueira", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.ataque_mira = False
        self.duracao -= 1
        if self.duracao <= 0:
            self.remover_efeito(personagem)

class Sangramento(Efeito):
    DANO = 45
    DURACAO = 4
    CHANCE = 60

    def __init__(self):
        super().__init__("Sangramento", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.vida -= self.DANO
        self.duracao -= 1
        if self.duracao <= 0:
            self.remover_efeito(personagem)

class Envenenado(Efeito):
    DANO = 35
    PENALIDADE = -10
    DURACAO = 4
    CHANCE = 90

    def __init__(self):
        super().__init__("Envenenado", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.vida -= self.DANO
        self.modificar_atributos(personagem, self.PENALIDADE)
        self.duracao -= 1
        if self.duracao <= 0:
            self.modificar_atributos(personagem, -self.PENALIDADE)
            self.remover_efeito(personagem)

    @staticmethod
    def modificar_atributos(personagem, valor):
        personagem.forca += valor
        personagem.velocidade += valor
        personagem.resistencia += valor

class Enraizado(Efeito):
    REDUCAO_VELOCIDADE = 30
    DURACAO = 2
    CHANCE = 65

    def __init__(self):
        super().__init__("Enraizado", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.velocidade = max(0, personagem.velocidade - self.REDUCAO_VELOCIDADE)
        self.duracao -= 1
        if self.duracao <= 0:
            self.remover_efeito(personagem)

class ControleMental(Efeito):
    DURACAO = 2
    CHANCE = 50

    def __init__(self):
        super().__init__("Controle Mental", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        personagem.controlado = True
        self.duracao -= 1
        if self.duracao <= 0:
            personagem.controlado = False
            self.remover_efeito(personagem)

class Bebado(Efeito):
    PENALIDADES = {
        "forca": -15,
        "velocidade": -10,
        "resistencia": -5,
        "magia": -5,
        "vigor": -10,
        "controle": -30
    }
    DURACAO = 2
    CHANCE = 60

    def __init__(self):
        super().__init__("Bebado", self.DURACAO, self.CHANCE)

    def verificar(self, personagem):
        self.modificar_atributos(personagem, self.PENALIDADES)
        self.duracao -= 1
        if self.duracao <= 0:
            self.modificar_atributos(personagem, {k: -v for k, v in self.PENALIDADES.items()})
            self.remover_efeito(personagem)

    @staticmethod
    def modificar_atributos(personagem, valores):
        for atributo, valor in valores.items():
            setattr(personagem, atributo, getattr(personagem, atributo) + valor)

