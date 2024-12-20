import pygame # type: ignore
from pygame.locals import *
from constants import largura_tela, altura_tela, x_info_batalha, y_info_batalha, x_info_personagens, y_info_personagens

def desenha_fundo(tela, personagens_selecionados, screen_width, screen_height):
    img_fundo = pygame.image.load('images/batalha/fundo-batalha.png')
    img_fundo = pygame.transform.scale(img_fundo, (screen_width, screen_height))
    tela.blit(img_fundo, (0, 0))

    img_info_batalha = pygame.image.load('images/batalha/info-batalha.png')
    tela.blit(img_info_batalha, (x_info_batalha, y_info_batalha))

    img_info_personagens = pygame.image.load('images/batalha/info-personagens.png')
    tela.blit(img_info_personagens, (x_info_personagens, y_info_personagens))

def desenha_personagens(tela, personagens_selecionados, screen_width, screen_height):
    pos_x = 150
    pos_y = 100

    for i, personagem in enumerate(personagens_selecionados):
        if i == 1:
            pos_x = 0
            pos_y += 110
        elif i == 2:
            pos_x += 150
            pos_y += 130

        if personagem.vida > 0:
            tela.blit(personagem.imagem, (pos_x, pos_y))
        else:
            personagem.esta_vivo = False
            personagens_selecionados.remove(personagem)

def desenha_inimigos(tela, inimigos):
    pos_x = 600
    pos_y = 110

    for i, inimigo in enumerate(inimigos):
        if i == 0 and inimigo.nome == 'Cerbero':
            pos_x = 650
            pos_y += 50
        elif i == 1:
            pos_x = 650
            pos_y += 250

        if inimigo.vida > 0:
            tela.blit(inimigo.imagem, (pos_x, pos_y))
        else:
            inimigo.esta_vivo = False
            inimigos.remove(inimigo)
            continue

        img_hp_vazio = pygame.image.load('images/batalha/hp-vazio.png')
        img_hp_vazio = pygame.transform.scale(img_hp_vazio, (inimigo.vida_max + 50, 40))

        if inimigo.nome == 'Hades':
            inimigo.posicao_batalha = (pos_x - 110, pos_y - 30)
            tela.blit(img_hp_vazio, (pos_x + 205, pos_y + 102))
            pygame.draw.rect(
                tela,
                (203, 54, 23),
                (pos_x + 246, pos_y + 120, inimigo.vida, 10),
                border_radius=10
            )
        elif inimigo.nome == 'Cerbero':
            inimigo.posicao_batalha = (pos_x - 160, pos_y - 70)
            tela.blit(img_hp_vazio, (pos_x + 155, pos_y + 20))
            pygame.draw.rect(
                tela,
                (203, 54, 23),
                (pos_x + 200, pos_y + 36, inimigo.vida - 5, 12),
                border_radius=10
            )

def preenche_infos(tela, personagens_selecionados, personagem_atual):
    font = pygame.font.Font('fonts/god-of-war.ttf', 30)
    cor_texto = (255, 255, 255)
    posicoes_info = []

    if personagem_atual in personagens_selecionados:
        personagem = font.render(f"{personagem_atual.nome}'s turn!", True, cor_texto)
        ataque = font.render(f'Attack', True, cor_texto)
        defesa = font.render(f'Defend', True, cor_texto)
        habilidade = font.render('Skill', True, cor_texto)

        posicao_ataque = (x_info_batalha + 60, y_info_batalha + 40 + personagem.get_height())
        posicao_defesa = (x_info_batalha + ataque.get_width() + 140, y_info_batalha + 40 + personagem.get_height())
        posicao_habilidade = (x_info_batalha + ataque.get_width() + defesa.get_width() + 220, y_info_batalha + 40 + personagem.get_height())

        tela.blit(personagem, (x_info_batalha + 60, y_info_batalha + 10))
        tela.blit(ataque, posicao_ataque)
        tela.blit(defesa, posicao_defesa)
        tela.blit(habilidade, posicao_habilidade)

        posicao_ataque_seta = (x_info_batalha + 60 - 75, y_info_batalha + 40 + personagem.get_height() - 65)
        posicao_defesa_seta = (x_info_batalha + ataque.get_width() + 140 - 75, y_info_batalha + 40 + personagem.get_height() - 60)
        posicao_habilidade_seta = (x_info_batalha + ataque.get_width() + defesa.get_width() + 220 - 75, y_info_batalha + 40 + personagem.get_height() - 65)
        posicoes_info.extend([posicao_ataque_seta, posicao_defesa_seta, posicao_habilidade_seta])
    else:
        inimigo = font.render(f"{personagem_atual.nome}'s turn!", True, cor_texto)
        tela.blit(inimigo, (x_info_batalha + 60, y_info_batalha + 10))

    font = pygame.font.Font('fonts/god-of-war.ttf', 24)
    pos_x = x_info_personagens + 20
    pos_y = y_info_personagens + 20

    for personagem in personagens_selecionados:
        nome = font.render(personagem.nome, True, cor_texto)
        vida = font.render(f'{personagem.vida}  /  {personagem.vida_max}', True, (255, 0, 0))
        tela.blit(nome, (pos_x, pos_y))
        tela.blit(vida, (pos_x + 140, pos_y))
        pos_y += 40

    return posicoes_info
            