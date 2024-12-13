import pygame # type: ignore
from constants import largura_tela, altura_tela
from menu import desenha_menu
from jogo import realiza_batalha, tela_final
from inimigos import Inimigo
import copy

def main():
    pygame.init()

    # Definindo o tamanho da tela.
    tela = pygame.display.set_mode((largura_tela, altura_tela))

    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        personagens_selecionados = desenha_menu(tela)
        personagens_selecionados_copy = copy.copy(personagens_selecionados)
        inimigos = Inimigo.cria_inimigos()
        ganhou = realiza_batalha(tela, personagens_selecionados)

        if ganhou:
            mensagem = 'Parabens, voce venceu!'
        else:
            mensagem = 'Tente novamente, voce perdeu!'
        
        tela_final(tela, personagens_selecionados_copy, inimigos, mensagem)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()