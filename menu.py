import pygame  # type: ignore 
from pygame.locals import *  # type: ignore
from personagem import Personagem
from constants import y_seta_correcao, x_seta_correcao

# Função para fazer transição de fade
def fade_transition(screen, image, fade_speed=15):
    fade_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    fade_surface.blit(image, (0, 0))
    fade_surface.set_alpha(0)

    # Fade-out
    for alpha in range(0, 256, fade_speed):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

    # Fade-in
    for alpha in range(255, -1, -fade_speed):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(15)

# Função para desenhar opções de jogo
def desenha_opcoes_jogo(screen, menu_options, selected_option, screen_width, screen_height):
    font = pygame.font.Font('fonts/god-of-war.ttf', 60)
    gold = (254, 181, 70)
    black = (0, 0, 0)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    selected_option = -1

    for i, option in enumerate(menu_options):
        color = black if i != selected_option else gold
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 100 + i * 80))

        if text_rect.collidepoint(mouse_x, mouse_y):
            selected_option = i
            color = gold

        pygame.draw.rect(screen, color, text_rect.inflate(20, 10), border_radius=5, width=3)
        screen.blit(text, text_rect.topleft)

    pygame.display.flip()
    return selected_option

def desenha_menu(tela, screen_width, screen_height):
    personagens = Personagem.cria_personagens()
    desenha_fundo(tela, screen_width, screen_height)
    return desenha_abas(tela, personagens, screen_width, screen_height)

def desenha_fundo(tela, screen_width, screen_height):
    img_fundo = pygame.image.load("images/menu/menu-personagens.png")
    img_fundo = pygame.transform.scale(img_fundo, (screen_width, screen_height))
    tela.blit(img_fundo, (0, 0))

    font = pygame.font.Font('fonts/god-of-war.ttf', 45)
    cor_titulo = (255, 255, 255)
    texto_titulo = font.render('Olimpius!', True, cor_titulo)

    largura_texto = texto_titulo.get_width()
    altura_texto = texto_titulo.get_height()
    posicao_texto = ((screen_width - largura_texto) // 2, 40)
    cor_fundo = (119, 160, 162)
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
    desenha_icones_abas(tela, screen_width, screen_height)
    desenha_botao_voltar(tela)

def desenha_icones_abas(tela, screen_width, screen_height):
    # Desenha ícones de seta diretamente
    seta_direita = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.polygon(seta_direita, (255, 255, 255), [(40, 25), (10, 5), (10, 45)])
    seta_esquerda = pygame.Surface((50, 50), pygame.SRCALPHA)
    pygame.draw.polygon(seta_esquerda, (255, 255, 255), [(10, 25), (40, 5), (40, 45)])
    
    tela.blit(seta_esquerda, (50, screen_height // 2))
    tela.blit(seta_direita, (screen_width - 100, screen_height // 2))
    
def desenha_botao_voltar(tela):
    font = pygame.font.Font('fonts/god-of-war.ttf', 30)
    cor_fundo = (255, 162, 116)
    cor_borda = (255, 255, 255)
    cor_texto = (255, 255, 255)
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
    botao_voltar = desenha_botao_voltar(tela)

    while True:
        desenha_fundo(tela, screen_width, screen_height)
        desenha_botoes(tela, grupos_personagens[aba_atual], screen_width, screen_height, cursor)
        desenha_icones_abas(tela, screen_width, screen_height)
        botao_voltar = desenha_botao_voltar(tela)

        # Mensagem de seleção
        font_grande = pygame.font.Font('fonts/god-of-war.ttf', 80)
        mensagem = f"Selecione {faltam} personagens"
        texto_mensagem = font_grande.render(mensagem, True, (254, 181, 70))
        largura_mensagem = texto_mensagem.get_width()
        tela.blit(texto_mensagem, ((screen_width - largura_mensagem) // 2, 125))
        
         # Teclas de instrução

        font_pequena = pygame.font.Font('fonts/nomes.ttf', 30)
        instrucoes = "Teclas: C ou 0 Selecionar | 1 - 3 ou Q - E Mudar abas"
        texto_instrucoes = font_pequena.render(instrucoes, True, (254, 181, 70))
        largura_instrucoes = texto_instrucoes.get_width()
        tela.blit(texto_instrucoes, ((screen_width - largura_instrucoes) // 2, screen_height - 130))

        # Exibir número da aba
        texto_aba = font_pequena.render(f"Aba {aba_atual + 1}/{len(grupos_personagens)}", True, (255, 255, 255))
        tela.blit(texto_aba, (screen_width // 2 - texto_aba.get_width() // 2, screen_height - 70))
        pygame.display.flip()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_clicado = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique esquerdo
                    mouse_clicado = True
                    if botao_voltar.collidepoint(event.pos):
                        return None  # Voltar ao menu principal
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_KP1, pygame.K_q] and aba_atual > 0:
                    aba_atual -= 1
                    cursor = 0
                elif event.key in [pygame.K_KP3, pygame.K_e] and aba_atual < len(grupos_personagens) - 1:
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
                    personagem = grupos_personagens[aba_atual][cursor]
                    if personagem not in selecionados and len(selecionados) < 3:
                        personagem.selecionado = True
                        selecionados.append(personagem)
                        faltam -= 1
                    elif personagem in selecionados:
                        personagem.selecionado = False
                        selecionados.remove(personagem)
                        faltam += 1

        # Detecção com mouse para personagens
        for i, personagem in enumerate(grupos_personagens[aba_atual]):
            colunas = 5
            linhas = 2
            margem_horizontal = 100
            margem_vertical = 150

            largura_espaco = (screen_width - 2 * margem_horizontal) // colunas
            altura_espaco = (screen_height - 2 * margem_vertical) // linhas

            coluna = i % colunas
            linha = i // colunas

            posicao_botao = (
                margem_horizontal + coluna * largura_espaco + largura_espaco // 2,
                margem_vertical + linha * altura_espaco + altura_espaco // 2
            )

            rect_botao = pygame.Rect(
                posicao_botao[0] - 75, posicao_botao[1] - 75, 150, 150
            )

            if rect_botao.collidepoint(mouse_x, mouse_y):
                cursor = i  # Move o cursor para onde o mouse está
                if mouse_clicado:
                    personagem = grupos_personagens[aba_atual][i]
                    if personagem not in selecionados and len(selecionados) < 3:
                        personagem.selecionado = True
                        selecionados.append(personagem)
                        faltam -= 1
                    elif personagem in selecionados:
                        personagem.selecionado = False
                        selecionados.remove(personagem)
                        faltam += 1

        # Detecção de clique nas setas para navegação
        seta_esquerda_rect = pygame.Rect(50, screen_height // 2, 50, 50)
        seta_direita_rect = pygame.Rect(screen_width - 100, screen_height // 2, 50, 50)

        if seta_esquerda_rect.collidepoint(mouse_x, mouse_y) and mouse_clicado and aba_atual > 0:
            aba_atual -= 1
            cursor = 0
        if seta_direita_rect.collidepoint(mouse_x, mouse_y) and mouse_clicado and aba_atual < len(grupos_personagens) - 1:
            aba_atual += 1
            cursor = 0

        if len(selecionados) == 3:
            return selecionados

def desenha_botoes(tela, personagens, screen_width, screen_height, cursor):
    font = pygame.font.Font('fonts/nomes.ttf', 30)
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