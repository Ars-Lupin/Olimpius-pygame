import pygame # type: ignore
import random

class Inimigo:
    '''
    Atributos dos inimigos:
        - Nome;
        - Ataque;
        - Defesa;
        - Vida máxima;
        - Vida atual;
        - Velocidade;
        - Imagem;
        - Posição na batalha;
        - Vivo.
    '''

    def __init__(self, nome, ataque, defesa, vida_max, velocidade, src_imagem):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida_max = vida_max
        self.vida = vida_max
        self.velocidade = velocidade
        self.imagem = pygame.image.load(src_imagem)
        self.posicao_batalha = None
        self.x = 0
        self.y = 0

        if self.nome == 'Cerbero':
            self.imagem = pygame.transform.scale(self.imagem, (150, 150))
        else:
            self.imagem = pygame.transform.scale(self.imagem, (230, 230))
        self.esta_vivo = True

    @staticmethod
    def cria_inimigos():
        return [
            Inimigo('Hades', 70, 60, 140, 60, 'images/batalha/hades.png'), 
            Inimigo('Cerbero', 80, 70, 160, 50, 'images/batalha/cerbero.png')
        ]
    
    def ataca_personagem(self, personagens_selecionados):
        personagem = personagens_selecionados[random.randint(0, len(personagens_selecionados) - 1)]
        dano = round(self.ataque * (50 / (50 + personagem.resistencia)))
        personagem.vida -= dano

        if personagem.vida <= 0:
            personagem.esta_vivo = False
            personagens_selecionados.remove(personagem)

    @staticmethod
    def verifica_inimigos_vivos(inimigos):
        for inimigo in inimigos:
            if not inimigo.esta_vivo:
                inimigos.remove(inimigo)