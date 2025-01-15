import pygame
from ataques import Ataque
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
    pos_x = screen_width * 0.2
    pos_y = screen_height * 0.2

    for i, personagem in enumerate(personagens_selecionados):
        if i == 1:
            pos_x = screen_width * 0.03
            pos_y += screen_height * 0.15
        elif i == 2:
            pos_x = screen_width * 0.2
            pos_y += screen_height * 0.17

        if personagem.vida > 0:
            tela.blit(personagem.imagem, (pos_x, pos_y))
        else:
            personagem.esta_vivo = False
            personagens_selecionados.remove(personagem)

        personagem.x = pos_x
        personagem.y = pos_y
        
        if personagem.nome == "Hefesto":
            for robo in personagem.robos_ativos:  # Lista de robôs ativos de Hefesto
                if robo.esta_vivo:
                    robo.desenhar(tela)

def desenha_inimigos(tela, inimigos, screen_width, screen_height):
    pos_x = screen_width * 0.6
    pos_y = screen_height * 0.2

    for i, inimigo in enumerate(inimigos):
        if i == 0 and inimigo.nome == 'Cerbero':
            pos_x = screen_width * 0.65
            pos_y += screen_height * 0.05
            inimigo.x = pos_x
            inimigo.y = pos_y
        elif i == 1:
            pos_x = screen_width * 0.65
            pos_y += screen_height * 0.25
            inimigo.x = pos_x
            inimigo.y = pos_y

        if inimigo.vida > 0:
            # Inverter a imagem horizontalmente
            imagem_invertida = pygame.transform.flip(inimigo.imagem, True, False)
            tela.blit(imagem_invertida, (pos_x, pos_y))
        else:
            inimigo.esta_vivo = False
            inimigos.remove(inimigo)
            continue

        # Desenhar a barra de vida
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
    """
    Preenche as informações da tela de batalha, exibindo os ataques do personagem atual.
    Mostra 6 opções de ataques posicionados dentro de info-batalha.png.
    """
    font = pygame.font.Font('fonts/Dalek.ttf', 15)
    cor_texto = (255, 255, 255)
    posicoes_info = []

    # Carregar ataques do personagem atual
    ataques = personagem_atual.lista_ataques

    # Carregar a imagem base (info-batalha.png)
    imagem_base = pygame.image.load('images/batalha/info-batalha.png').convert_alpha()
    largura_base, altura_base = imagem_base.get_size()

    # Posição da imagem base
    img_info_batalha_pos = (screen_width * 0.05, screen_height * 0.8)
    tela.blit(imagem_base, img_info_batalha_pos)

    # Calcular área disponível dentro da imagem base
    margem_horizontal = 10  # Espaço horizontal nas bordas
    margem_vertical = 10  # Espaço vertical nas bordas
    largura_disponivel = largura_base - 2 * margem_horizontal
    altura_disponivel = altura_base - 2 * margem_vertical

    # Dimensões dos botões - aumentadas
    largura_botao = (largura_disponivel // 3) - 5  # Maior largura dos botões
    altura_botao = (altura_disponivel // 2) - 5  # Maior altura dos botões

    # Posição inicial para o primeiro botão
    pos_x_inicial = img_info_batalha_pos[0] + margem_horizontal
    pos_y_inicial = img_info_batalha_pos[1] + margem_vertical

    # Gerar botões (3 em cima, 3 embaixo)
    for i, ataque in enumerate(ataques[:6]):  # Limitar a 6 ataques
        # Calcular linha e coluna
        linha = i // 3  # 0 para primeira linha, 1 para segunda linha
        coluna = i % 3  # 0, 1, 2 para cada coluna

        # Calcular posição do botão
        pos_x = pos_x_inicial + coluna * (largura_botao + 5)  # Aumentado espaçamento horizontal
        pos_y = pos_y_inicial + linha * (altura_botao + 5)   # Aumentado espaçamento vertical

        # Desenhar retângulo do botão (simula info-batalha reduzido)
        pygame.draw.rect(tela, (128, 128, 128), (pos_x, pos_y, largura_botao, altura_botao), border_radius=4)

        # Adicionar texto do ataque no centro do botão
        texto_ataque = font.render(ataque.nome, True, cor_texto)
        texto_pos_x = pos_x + (largura_botao - texto_ataque.get_width()) // 2
        texto_pos_y = pos_y + (altura_botao - texto_ataque.get_height()) // 2
        tela.blit(texto_ataque, (texto_pos_x, texto_pos_y))

        # Salvar posição para interações futuras
        posicoes_info.append((pos_x, pos_y, largura_botao, altura_botao))

    # Renderizar informações dos personagens selecionados
    font = pygame.font.Font('fonts/god-of-war.ttf', 24)
    pos_x = screen_width * 0.5 - 90
    pos_y = screen_height * 0.85 - 20

    for personagem in personagens_selecionados:
        nome = font.render(personagem.nome, True, cor_texto)
        vida = font.render(f'{personagem.vida} / {personagem.vida_max}', True, (255, 0, 0))
        tela.blit(nome, (pos_x, pos_y))
        tela.blit(vida, (pos_x + 140, pos_y))
        pos_y += 40

    return posicoes_info

