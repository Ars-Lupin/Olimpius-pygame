import pygame # type: ignore
from pygame.locals import * # type: ignore
from constants import largura_tela, altura_tela
from personagem import Personagem
from constants import largura_tela, altura_tela, y_seta_correcao, x_seta_correcao

def desenha_menu(tela):
    personagens = Personagem.cria_personagens()
    desenha_fundo(tela)
    desenha_botoes(tela, personagens)
    return seleciona_personagens(tela, personagens)

def desenha_fundo(tela):
    # Carregando a imagem de fundo do menu e redimesionando para o tamanho da tela.
    img_fundo = pygame.image.load("images/menu/fundo-menu.jpg")
    img_fundo = pygame.transform.scale(img_fundo, (largura_tela, altura_tela))

    # Função para desenhar em cima de uma outra superfície (desenhar a imagem de fundo por cima da tela, partindo do canto superior esquerdo).
    tela.blit(img_fundo, (0, 0))

    # Definindo a fonte, a cor do título e o título que ficará no menu principal.
    font = pygame.font.Font(None, 45)
    cor_titulo = (255, 255, 255)
    texto_titulo = font.render('IntroBattle!', True, cor_titulo)

    # Definindo a posição do texto e escrevendo o título no menu principal.
    largura_texto = texto_titulo.get_width()
    altura_texto = texto_titulo.get_height()
    posicao_texto = ((largura_tela - largura_texto) // 2, 40)
    cor_fundo = (203, 54, 23)
    cor_borda = cor_titulo

    # Desenhando um retângulo para colocar um fundo no título.
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


def desenha_botoes(tela, personagens):
    # Definindo a fonte e a cor do texto que ficará nos botões.
    font = pygame.font.Font('fonts/Anton-Regular.ttf', 30)
    cor_texto = (255, 255, 255)

    # Variáveis para controlar a posição dos botões.
    cont = 0
    flag = 1

    # Desenhando os botões de cada personagem.
    for i, personagem in enumerate(personagens):
        # Definindo a posição do texto e escrevendo o texto nos botões.
        texto_botao = font.render(personagem.nome, True, cor_texto)
        cont += 1

        if (cont > 3):
            num = 150

            if flag:
                num = -130
                flag = 0

            posicao_botao = (largura_tela // 2 + num, altura_tela // 2 + 240)
        else:
            direction = i

            if i == 2:
                direction = -1

            posicao_botao = (largura_tela // 2 - direction * 250, altura_tela // 2)

        if personagem.selecionado:
            img_personagem = personagem.imagem_menu_selecionado
        else: 
            img_personagem = personagem.imagem_menu
        img_personagem = pygame.transform.scale(img_personagem, (150, 150))
        tela.blit(img_personagem, (posicao_botao[0] - 100, posicao_botao[1] - 100))
        personagem.posicao_menu = (posicao_botao[0] - x_seta_correcao, posicao_botao[1] - y_seta_correcao)

        tam = 60

        if personagem.nome == "Ártemis" or personagem.nome == "Poseidon":
            tam = 80

        posicao_texto = (posicao_botao[0] - tam, posicao_botao[1] + 50)
        tela.blit(texto_botao, posicao_texto)

def seleciona_personagens(tela, personagens):
    font = pygame.font.Font('fonts/god-of-war.ttf', 55)
    personagens_selecionados = []
    qtd_personagens_selecionados = 0
    pos_menu = personagens[0].posicao_menu
    img_seta = pygame.image.load('images/menu/seta.png')
    img_seta = pygame.transform.scale(img_seta, (300, 300))

    while qtd_personagens_selecionados < 3:
        cor_texto_info = (203, 54, 23)
        texto_info = font.render(
            f'Escolha {3 - qtd_personagens_selecionados} {"personagem" if qtd_personagens_selecionados == 2 else "personagens"}!',
            True,
            cor_texto_info
        )
        posicao_texto_info = ((largura_tela - texto_info.get_width()) // 2, 120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pos_menu = move_seta(personagens, pos_menu, 'up')
                elif event.key == K_DOWN:
                    pos_menu = move_seta(personagens, pos_menu, 'down')
                elif event.key == K_LEFT:
                    pos_menu = move_seta(personagens, pos_menu, 'left')
                elif event.key == K_RIGHT:
                    pos_menu = move_seta(personagens, pos_menu, 'right')
                elif event.key == K_z:
                    for personagem in personagens:
                        if personagem.posicao_menu == pos_menu:
                            if not personagem.selecionado:
                                personagens_selecionados.append(personagem)
                                qtd_personagens_selecionados += 1
                                personagem.selecionado = True
                                break
                            else:
                                personagem.selecionado = False
                                qtd_personagens_selecionados -= 1
                                personagens_selecionados.remove(personagem)
                                break

        desenha_fundo(tela)
        desenha_botoes(tela, personagens)
        tela.blit(texto_info, posicao_texto_info)
        tela.blit(img_seta, pos_menu)
        pygame.display.flip()

    return personagens_selecionados


def move_seta(personagens, pos_menu, tecla):
    if tecla == 'up':
        if pos_menu[1] == personagens[3].posicao_menu[1] and pos_menu[0] == personagens[3].posicao_menu[0]:
            pos_menu = (personagens[1].posicao_menu[0], personagens[1].posicao_menu[1])
        elif pos_menu[1] == personagens[4].posicao_menu[1] and pos_menu[0] == personagens[4].posicao_menu[0]:
            pos_menu = (personagens[2].posicao_menu[0], personagens[2].posicao_menu[1])

    elif tecla == 'down':
        if ((pos_menu[1] == personagens[0].posicao_menu[1] and pos_menu[0] == personagens[0].posicao_menu[0]) or
            (pos_menu[1] == personagens[1].posicao_menu[1] and pos_menu[0] == personagens[1].posicao_menu[0])):
            pos_menu = (personagens[3].posicao_menu[0], personagens[3].posicao_menu[1])
        elif pos_menu[1] == personagens[2].posicao_menu[1] and pos_menu[0] == personagens[2].posicao_menu[0]:
           pos_menu = (personagens[4].posicao_menu[0], personagens[4].posicao_menu[1])

    elif tecla == 'left':
        if pos_menu[0] == personagens[0].posicao_menu[0] and pos_menu[1] == personagens[0].posicao_menu[1]:
            pos_menu = (personagens[1].posicao_menu[0], personagens[1].posicao_menu[1])
        elif pos_menu[0] == personagens[2].posicao_menu[0] and pos_menu[1] == personagens[2].posicao_menu[1]:
            pos_menu = (personagens[0].posicao_menu[0], personagens[0].posicao_menu[1])
        elif pos_menu[0] == personagens[4].posicao_menu[0] and pos_menu[1] == personagens[4].posicao_menu[1]:
            pos_menu = (personagens[3].posicao_menu[0], personagens[3].posicao_menu[1])

    elif tecla == 'right':
        if pos_menu[0] == personagens[0].posicao_menu[0] and pos_menu[1] == personagens[0].posicao_menu[1]:
            pos_menu = (personagens[2].posicao_menu[0], personagens[2].posicao_menu[1])
        elif pos_menu[0] == personagens[1].posicao_menu[0] and pos_menu[1] == personagens[1].posicao_menu[1]:
            pos_menu = (personagens[0].posicao_menu[0], personagens[0].posicao_menu[1])
        elif pos_menu[0] == personagens[3].posicao_menu[0] and pos_menu[1] == personagens[3].posicao_menu[1]:
            pos_menu = (personagens[4].posicao_menu[0], personagens[4].posicao_menu[1])

    return pos_menu