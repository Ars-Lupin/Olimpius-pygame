import pygame # type: ignore
from batalha import desenha_fundo, desenha_personagens, preenche_infos, desenha_inimigos
from inimigos import Inimigo
from personagem import Personagem

def realiza_batalha(tela, personagens_selecionados, screen_width, screen_height):
    inimigos = Inimigo.cria_inimigos()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        Personagem.verifica_personagens_vivos(personagens_selecionados)
        Inimigo.verifica_inimigos_vivos(inimigos)

        if len(personagens_selecionados) <= 0 and len(inimigos) > 0:
            pygame.time.delay(500)
            return False
        elif len(inimigos) <= 0 and len(personagens_selecionados) > 0:
            return True

        desenha_fundo(tela, personagens_selecionados, screen_width, screen_height)
        desenha_personagens(tela, personagens_selecionados, screen_width, screen_height)
        desenha_inimigos(tela, inimigos, screen_width, screen_height)

        # Ordena a lista de turnos com base na velocidade
        turno = sorted(personagens_selecionados + inimigos, key=lambda x: x.velocidade, reverse=True)

        processa_turnos(tela, personagens_selecionados, inimigos, turno, screen_width, screen_height)

        pygame.display.flip()


def processa_turnos(tela, personagens_selecionados, inimigos, turno, screen_width, screen_height):
    while turno:
        personagem_atual = turno.pop(0)

        if personagem_atual.esta_vivo:
            if personagem_atual in personagens_selecionados:
                jogador_realiza_acao(tela, personagens_selecionados, inimigos, personagem_atual, turno, screen_width, screen_height)
            else:
                personagem_atual.ataca_personagem(personagens_selecionados)

        if len(personagens_selecionados) <= 0 or len(inimigos) <= 0:
            break


def jogador_realiza_acao(tela, personagens_selecionados, inimigos, personagem_atual, turno, screen_width, screen_height):
    img_seta = pygame.image.load('images/batalha/seta-escura.png')
    img_seta = pygame.transform.scale(img_seta, (300, 300))
    pos_menu = 0

    # Assumindo que 'preenche_infos' já exibe as habilidades de cada personagem
    poderes = personagem_atual.lista_ataques  # Lista de poderes ou habilidades do personagem

    # Preenche as informações da tela, incluindo os ataques do personagem
    posicoes_info = preenche_infos(tela, personagens_selecionados, personagem_atual, screen_width, screen_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if pos_menu < len(poderes) - 1:
                        pos_menu += 1
                elif event.key == pygame.K_LEFT:
                    if pos_menu > 0:
                        pos_menu -= 1
                elif event.key in [pygame.K_RETURN, pygame.K_c, pygame.K_KP0]:
                    # Ativa o poder selecionado
                    poder_selecionado = poderes[pos_menu]
                    poder_selecionado.uso(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height)
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  
                        
                        x, y = event.pos
                        if check_mouse_over_poderes(x, y, posicoes_info): 
                            poder_selecionado = poderes[pos_menu]
                            poder_selecionado.uso(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height)
                            return

            # Mouse selecionando
            elif event.type == pygame.MOUSEMOTION:
                # Detecta se o mouse está sobre algum poder
                x, y = event.pos
                if check_mouse_over_poderes(x, y, posicoes_info):
                    pos_menu = get_poder_selected_by_mouse(x, y, posicoes_info)

        desenha_fundo(tela, personagens_selecionados, screen_width, screen_height)
        desenha_personagens(tela, personagens_selecionados, screen_width, screen_height)
        desenha_inimigos(tela, inimigos, screen_width, screen_height)

        # Preenche as informações novamente (com a borda desenhada)
        preenche_infos(tela, personagens_selecionados, personagem_atual, screen_width, screen_height)

        # Desenha a borda vermelha ao redor do poder selecionado
        desenha_borda_selecionada(tela, pos_menu, posicoes_info)

        pygame.display.flip()


def desenha_borda_selecionada(tela, pos_menu, posicoes_info):

    cor_borda = (255, 0, 0)  # Cor vermelha

    # Posição e tamanho do poder selecionado
    pos_x, pos_y, largura, altura = posicoes_info[pos_menu]

    # Desenha a borda vermelha ao redor do poder selecionado
    pygame.draw.rect(tela, cor_borda, (pos_x - 10, pos_y - 10, largura + 10, altura + 10), 5)


def check_mouse_over_poderes(x, y, posicoes_info):
    """
    Verifica se o mouse está sobre algum poder da lista de posições.
    """
    for i, (pos_x, pos_y, largura, altura) in enumerate(posicoes_info):
        if pos_x <= x <= pos_x + largura and pos_y <= y <= pos_y + altura:
            return True
    return False


def get_poder_selected_by_mouse(x, y, posicoes_info):
    """
    Retorna o índice do poder selecionado com o mouse.
    """
    for i, (pos_x, pos_y, largura, altura) in enumerate(posicoes_info):
        if pos_x <= x <= pos_x + largura and pos_y <= y <= pos_y + altura:
            return i
    return 0

def tela_final(tela, personagens_selecionados, inimigos, mensagem, screen_width, screen_height):
    img_fundo = pygame.image.load('images/batalha/fundo-batalha.png')
    img_fundo = pygame.transform.scale(img_fundo, (screen_width, screen_height))
    tela.blit(img_fundo, (0, 0))

    font = pygame.font.Font('fonts/god-of-war.ttf', 50)
    cor_texto = (255, 255, 255)
    texto = font.render(mensagem, True, cor_texto)
    largura_texto = texto.get_width()
    posicao_texto = ((screen_width - largura_texto) // 2, 200)
    tela.blit(texto, posicao_texto)

    pos_x = screen_width // 2 - 500
    pos_y = screen_height // 2 - 100

    if mensagem == 'Parabens, voce venceu!':
        for personagem in personagens_selecionados:
            personagem.imagem = pygame.transform.scale(personagem.imagem, (300, 300))
            tela.blit(personagem.imagem, (pos_x, pos_y))
            pos_x += 300
    else:
        for inimigo in inimigos:
            pos_x += 100
            if inimigo.nome == 'Cerbero':
                inimigo.imagem = pygame.transform.scale(inimigo.imagem, (200, 200))
            else:
                inimigo.imagem = pygame.transform.scale(inimigo.imagem, (300, 300))
            tela.blit(inimigo.imagem, (pos_x, pos_y))
            pos_x += 300
            pos_y += 20

    pygame.display.flip()
    pygame.time.delay(4000)
    