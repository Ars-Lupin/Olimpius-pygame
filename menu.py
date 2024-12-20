import pygame  # type: ignore
from pygame.locals import *  # type: ignore
from personagem import Personagem
from constants import y_seta_correcao, x_seta_correcao

def desenha_menu(tela, screen_width, screen_height):
    personagens = Personagem.cria_personagens()
    desenha_fundo(tela, screen_width, screen_height)
    return desenha_abas(tela, personagens, screen_width, screen_height)

def desenha_fundo(tela, screen_width, screen_height):
    img_fundo = pygame.image.load("images/menu/fundo-menu.jpg")
    img_fundo = pygame.transform.scale(img_fundo, (screen_width, screen_height))
    tela.blit(img_fundo, (0, 0))

    font = pygame.font.Font('fonts/god-of-war.ttf', 45)
    cor_titulo = (255, 255, 255)
    texto_titulo = font.render('Olimpius!', True, cor_titulo)

    largura_texto = texto_titulo.get_width()
    altura_texto = texto_titulo.get_height()
    posicao_texto = ((screen_width - largura_texto) // 2, 40)
    cor_fundo = (203, 54, 23)
    cor_borda = cor_titulo

    pygame.draw.rect(
        tela, 
        cor_borda,
        (posicao_texto[0] - 27, posicao_texto[1] - 7, largura_texto + 54, altura_texto + 14)
    )

    pygame.draw.rect(
        tela, 
        cor_fundo,
        (posicao_texto[0] - 25, posicao_texto[1] - 5, largura_texto + 50, altura_texto + 10)
    )

    tela.blit(texto_titulo, posicao_texto)

    # Botão de voltar
    desenha_botao_voltar(tela)

def desenha_botao_voltar(tela):
    font = pygame.font.Font('fonts/god-of-war.ttf', 30)
    cor_fundo = (203, 54, 23)
    cor_borda = (255, 255, 255)
    cor_texto = (254, 181, 70)
    texto = "Voltar"

    texto_voltar = font.render(texto, True, cor_texto)
    largura_texto = texto_voltar.get_width()
    altura_texto = texto_voltar.get_height()

    x, y = 20, 20  # Posição do botão
    largura_botao = largura_texto + 20
    altura_botao = altura_texto + 10

    pygame.draw.rect(tela, cor_borda, (x - 5, y - 5, largura_botao + 10, altura_botao + 10))
    pygame.draw.rect(tela, cor_fundo, (x, y, largura_botao, altura_botao))
    tela.blit(texto_voltar, (x + 10, y + 5))

    return pygame.Rect(x, y, largura_botao, altura_botao)

def desenha_abas(tela, personagens, screen_width, screen_height):
    grupos_personagens = [personagens[i:i+10] for i in range(0, len(personagens), 10)]
    aba_atual = 0
    cursor = 0
    selecionados = []
    faltam = 3
    botao_voltar = desenha_botao_voltar(tela)  # Retângulo do botão de voltar

    while True:
        desenha_fundo(tela, screen_width, screen_height)
        botao_voltar = desenha_botao_voltar(tela)
        desenha_botoes(tela, grupos_personagens[aba_atual], screen_width, screen_height, cursor)

        # Mensagem de seleção
        font_grande = pygame.font.Font('fonts/god-of-war.ttf', 80)
        mensagem = f"Selecione {faltam} personagens"
        texto_mensagem = font_grande.render(mensagem, True, (254, 181, 70))
        largura_mensagem = texto_mensagem.get_width()
        tela.blit(texto_mensagem, ((screen_width - largura_mensagem) // 2, 50))

        # Teclas de instrução
        font_pequena = pygame.font.Font('fonts/god-of-war.ttf', 30)
        instrucoes = "Teclas: [C] Selecionar | [0/1/3 do NumPad] Mudar abas"
        texto_instrucoes = font_pequena.render(instrucoes, True, (254, 181, 70))
        largura_instrucoes = texto_instrucoes.get_width()
        tela.blit(texto_instrucoes, ((screen_width - largura_instrucoes) // 2, screen_height - 30))

        # Exibir número da aba
        texto_aba = font_pequena.render(f"Aba {aba_atual + 1}/{len(grupos_personagens)}", True, (255, 255, 255))
        tela.blit(texto_aba, (screen_width // 2 - texto_aba.get_width() // 2, screen_height - 70))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and botao_voltar.collidepoint(event.pos):
                    return None  # Indica que o jogador quer voltar ao menu principal
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP0 or event.key == pygame.K_c:  # Selecionar personagem
                    personagem = grupos_personagens[aba_atual][cursor]
                    if personagem not in selecionados and len(selecionados) < 3:
                        personagem.selecionado = True
                        selecionados.append(personagem)
                        faltam -= 1
                    elif personagem in selecionados:
                        personagem.selecionado = False
                        selecionados.remove(personagem)
                        faltam += 1
                elif event.key == pygame.K_KP1 and aba_atual > 0:  # Mudar aba para a esquerda
                    aba_atual -= 1
                    cursor = 0
                elif event.key == pygame.K_KP3 and aba_atual < len(grupos_personagens) - 1:  # Mudar aba para a direita
                    aba_atual += 1
                    cursor = 0
                elif event.key in [pygame.K_UP, pygame.K_w]:
                    cursor = max(0, cursor - 5)
                elif event.key in [pygame.K_DOWN, pygame.K_s]:
                    cursor = min(len(grupos_personagens[aba_atual]) - 1, cursor + 5)
                elif event.key in [pygame.K_LEFT, pygame.K_a]:
                    cursor = max(0, cursor - 1)
                elif event.key in [pygame.K_RIGHT, pygame.K_d]:
                    cursor = min(len(grupos_personagens[aba_atual]) - 1, cursor + 1)
                elif event.key == pygame.K_RETURN:
                    if len(selecionados) < 3:  # Não começar o jogo, piscar o texto
                        for _ in range(3):
                            tela.fill((0, 0, 0))
                            pygame.display.flip()
                            pygame.time.wait(200)
                            tela.blit(texto_mensagem, ((screen_width - largura_mensagem) // 2, 50))
                            pygame.display.flip()
                            pygame.time.wait(200)
                    else:
                        return selecionados


def desenha_botoes(tela, personagens, screen_width, screen_height, cursor):
    font = pygame.font.Font('fonts/god-of-war.ttf', 30)
    cor_texto = (255, 255, 255)
    cor_cursor = (255, 0, 0)

    colunas = 5
    linhas = 2
    margem_horizontal = 100
    margem_vertical = 150

    largura_espaco = (screen_width - 2 * margem_horizontal) // colunas
    altura_espaco = (screen_height - 2 * margem_vertical) // linhas

    for i, personagem in enumerate(personagens):
        coluna = i % colunas
        linha = i // colunas

        posicao_botao = (
            margem_horizontal + coluna * largura_espaco + largura_espaco // 2,
            margem_vertical + linha * altura_espaco + altura_espaco // 2
        )

        img_personagem = personagem.imagem_menu_selecionado if personagem.selecionado else personagem.imagem_menu
        img_personagem = pygame.transform.scale(img_personagem, (150, 150))
        tela.blit(img_personagem, (posicao_botao[0] - 75, posicao_botao[1] - 75))
        personagem.posicao_menu = (posicao_botao[0] - x_seta_correcao, posicao_botao[1] - y_seta_correcao)

        texto_botao = font.render(personagem.nome, True, cor_texto)
        largura_texto = texto_botao.get_width()
        tela.blit(texto_botao, (posicao_botao[0] - largura_texto // 2, posicao_botao[1] + 80))

        if i == cursor:  # Desenhar cursor
            pygame.draw.rect(
                tela, cor_cursor, 
                (posicao_botao[0] - 80, posicao_botao[1] - 80, 160, 160), 3
            )
