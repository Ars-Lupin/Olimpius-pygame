import pygame
from pygame.locals import *

def desenha_fundo(tela,personagens_selecionados, screen_width, screen_height):
    img_fundo = pygame.image.load('images/batalha/fundo-batalha.png')
    img_fundo = pygame.transform.scale(img_fundo, (screen_width, screen_height))
    tela.blit(img_fundo, (0, 0))

    img_info_batalha = pygame.image.load('images/batalha/info-batalha.png')
    img_info_batalha_rect = img_info_batalha.get_rect()
    img_info_batalha_pos = (screen_width * 0.05, screen_height * 0.8)
    tela.blit(img_info_batalha, img_info_batalha_pos)

    img_info_personagens = pygame.image.load('images/batalha/info-personagens.png')
    img_info_personagens_pos = (
        img_info_batalha_pos[0] + img_info_batalha_rect.width,
        screen_height * 0.8
    )
    tela.blit(img_info_personagens, img_info_personagens_pos)

def desenha_personagens(tela, personagens_selecionados, screen_width, screen_height):
    pos_x = screen_width * 0.15
    pos_y = screen_height * 0.2

    for i, personagem in enumerate(personagens_selecionados):
        if i == 1:
            pos_x = screen_width * 0.05
            pos_y += screen_height * 0.15
        elif i == 2:
            pos_x += screen_width * 0.15
            pos_y += screen_height * 0.17

        if personagem.vida > 0:
            tela.blit(personagem.imagem, (pos_x, pos_y))
        else:
            personagem.esta_vivo = False
            personagens_selecionados.remove(personagem)

def desenha_inimigos(tela, inimigos, screen_width, screen_height):
    pos_x = screen_width * 0.6
    pos_y = screen_height * 0.2

    for i, inimigo in enumerate(inimigos):
        if i == 0 and inimigo.nome == 'Cerbero':
            pos_x = screen_width * 0.65
            pos_y += screen_height * 0.05
        elif i == 1:
            pos_x = screen_width * 0.65
            pos_y += screen_height * 0.25

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

def preenche_infos(tela, personagens_selecionados, personagem_atual, screen_width, screen_height):
    font = pygame.font.Font('fonts/god-of-war.ttf', 30)
    cor_texto = (255, 255, 255)
    posicoes_info = []

    if personagem_atual in personagens_selecionados:
        personagem = font.render(f"{personagem_atual.nome}'s turn!", True, cor_texto)
        ataque = font.render(f'Attack', True, cor_texto)
        defesa = font.render(f'Defend', True, cor_texto)
        habilidade = font.render('Skill', True, cor_texto)

        posicao_ataque = (screen_width * 0.05 + 60, screen_height * 0.8 + 40 + personagem.get_height())
        posicao_defesa = (screen_width * 0.05 + ataque.get_width() + 140, screen_height * 0.8 + 40 + personagem.get_height())
        posicao_habilidade = (screen_width * 0.05 + ataque.get_width() + defesa.get_width() + 220, screen_height * 0.8 + 40 + personagem.get_height())

        tela.blit(personagem, (screen_width * 0.05 + 60, screen_height * 0.8 + 10))
        tela.blit(ataque, posicao_ataque)
        tela.blit(defesa, posicao_defesa)
        tela.blit(habilidade, posicao_habilidade)

        posicao_ataque_seta = (screen_width * 0.05 + 60 - 75, screen_height * 0.8 + 40 + personagem.get_height() - 65)
        posicao_defesa_seta = (screen_width * 0.05 + ataque.get_width() + 140 - 75, screen_height * 0.8 + 40 + personagem.get_height() - 60)
        posicao_habilidade_seta = (screen_width * 0.05 + ataque.get_width() + defesa.get_width() + 220 - 75, screen_height * 0.8 + 40 + personagem.get_height() - 65)
        posicoes_info.extend([posicao_ataque_seta, posicao_defesa_seta, posicao_habilidade_seta])
    else:
        inimigo = font.render(f"{personagem_atual.nome}'s turn!", True, cor_texto)
        tela.blit(inimigo, (screen_width * 0.05 + 60, screen_height * 0.8 + 10))

    font = pygame.font.Font('fonts/god-of-war.ttf', 24)
    pos_x = screen_width * 0.5 - 90
    pos_y = screen_height * 0.85 - 20

    for personagem in personagens_selecionados:
        nome = font.render(personagem.nome, True, cor_texto)
        vida = font.render(f'{personagem.vida}  /  {personagem.vida_max}', True, (255, 0, 0))
        tela.blit(nome, (pos_x, pos_y))
        tela.blit(vida, (pos_x + 140, pos_y))
        pos_y += 40

    return posicoes_info
