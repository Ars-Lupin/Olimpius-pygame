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

        turno = []
        turno.extend(personagens_selecionados)
        turno.extend(inimigos)
        turno.sort(key=lambda x: x.velocidade, reverse=True)

        posicoes_info = preenche_infos(tela, personagens_selecionados, turno[0], screen_width, screen_height)
        seleciona_opcao(tela, personagens_selecionados, inimigos, posicoes_info, turno, screen_width, screen_height)

        pygame.display.flip()

def seleciona_opcao(tela, personagens_selecionados, inimigos, posicoes_info, turno, screen_width, screen_height):
    img_seta = pygame.image.load('images/batalha/seta-escura.png')
    img_seta = pygame.transform.scale(img_seta, (300, 300))
    pos_menu = 0

    while True:
        personagem_is_inimigo = True
        atacou_inimigo = True

        if len(turno) == 0:
            break

        personagem_atual = turno[0]

        if personagem_atual in personagens_selecionados:
            personagem_is_inimigo = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        if pos_menu < 2:
                            pos_menu += 1
                    elif event.key == pygame.K_LEFT:
                        if pos_menu > 0:
                            pos_menu -= 1
                    elif event.key == pygame.K_z:
                        if pos_menu == 0:
                            atacou_inimigo = personagem_atual.ataca_inimigo(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height)
                        elif pos_menu == 1:
                            personagem_atual.defende()
                        elif pos_menu == 2:
                            personagem_atual.habilidade()
                            atacou_inimigo = personagem_atual.ataca_inimigo(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height)
                            
                        if atacou_inimigo:
                            turno.pop(0)
        else:
            personagem_atual.ataca_personagem(personagens_selecionados)
            turno.pop(0)

        if len(personagens_selecionados) <= 0 or len(inimigos) <= 0:
            return

        desenha_fundo(tela, personagens_selecionados, screen_width, screen_height)
        desenha_personagens(tela, personagens_selecionados, screen_width, screen_height)
        desenha_inimigos(tela, inimigos, screen_width, screen_height)
        posicoes_info = preenche_infos(tela, personagens_selecionados, personagem_atual, screen_width, screen_height)

        if not personagem_is_inimigo:
            tela.blit(img_seta, posicoes_info[pos_menu])
        else:
            pygame.display.flip()
            pygame.time.delay(500)

        for personagem_or_inimigo in turno:
            if not personagem_or_inimigo.esta_vivo:
                turno.remove(personagem_or_inimigo)
        
        pygame.display.flip()

    Personagem.retira_defesa(personagens_selecionados)
    Personagem.retira_habilidade(personagens_selecionados)

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
    