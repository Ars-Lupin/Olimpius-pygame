import pygame 
from menu import desenha_menu
from jogo import realiza_batalha, tela_final
from inimigos import Inimigo
from pygame.locals import *
import copy

# Inicialização do pygame
pygame.init()

# Configurações da tela
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
print(screen_width, screen_height)
pygame.display.set_caption("Menu do Jogo - Olimpius")

# Carregar imagem tema para o menu
menu_theme_image = pygame.image.load('images/menu/Olimpius.png')
menu_theme_image = pygame.transform.scale(menu_theme_image, (screen_width, screen_height))

# Fonte e cores
font = pygame.font.Font('fonts/god-of-war.ttf', 30) 
white = (255, 255, 255)
black = (0, 0, 0)
gray = (100, 100, 100)
gold = (254, 181, 70)

def fade_transition(screen, image, fade_speed=15):
    """
    Aplica um efeito de fade-out e fade-in para a transição de menus.
    """
    fade_surface = pygame.Surface((screen_width, screen_height))
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

# Função para exibir a imagem do menu inicial e esperar por tecla
running = True
start_time = pygame.time.get_ticks()
while running:
    screen.blit(menu_theme_image, (0, 0))



    # Espera por uma tecla após 2 segundos
    if pygame.time.get_ticks() - start_time > 3000:
        # Renderiza a mensagem com o efeito de dissolução
        mensagem = font.render("Pressione qualquer tecla para continuar", True, gold)
        mensagem_rect = mensagem.get_rect(center=(screen_width // 2, (screen_height // 2) + 250))
        screen.blit(mensagem, mensagem_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                running = False  # Fecha o loop após pressionar uma tecla

font = pygame.font.Font('fonts/god-of-war.ttf', 60) 
menu_options = ["Solo", "Dois Jogadores", "Sair"]
selected_option = 0
fade_transition(screen, menu_theme_image)

def menu_principal():
    """Função principal do menu do jogo."""
    global screen

    menu_options = ["Solo", "Dois Jogadores", "Sair"]
    selected_option = 0

    while True:
        menu_theme_image = pygame.image.load('images/menu/menu-modo-de-jogo.png')
        menu_theme_image = pygame.transform.scale(menu_theme_image, (screen_width, screen_height))
        screen.blit(menu_theme_image, (0, 0))


        for i, option in enumerate(menu_options):
            color = black if i == selected_option else gold
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 100 + i * 80))

            if i == selected_option:
                pygame.draw.rect(screen, gold, text_rect.inflate(20, 10), border_radius=5, width=3)

            screen.blit(text, text_rect.topleft)

        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key in [K_RETURN, K_c]:
                    fade_transition(screen, menu_theme_image)
                    if selected_option == 0:
                        iniciar_jogo()
                    elif selected_option == 1:
                        print("Modo Dois Jogadores selecionado")  # Adicione lógica apropriada aqui
                    elif selected_option == 2:
                        pygame.quit()
                        exit()
                        
            if event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for i, option in enumerate(menu_options):
                    option_rect = font.render(option, True, gold).get_rect(center=(screen_width // 2, screen_height // 2 - 100 + i * 80))
                    if option_rect.collidepoint(mouse_x, mouse_y):
                        selected_option = i  # Alterar a seleção com o mouse
                        break
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                for i, option in enumerate(menu_options):
                    option_rect = font.render(option, True, gold).get_rect(
                        center=(screen_width // 2, screen_height // 2 - 100 + i * 80)
                    )
                    if option_rect.collidepoint(event.pos):
                        selected_option = i
                        fade_transition(screen, menu_theme_image)
                        if selected_option == 0:
                            iniciar_jogo()
                        elif selected_option == 1:
                            print("Modo Dois Jogadores selecionado")  # Adicione lógica apropriada aqui
                        elif selected_option == 2:
                            pygame.quit()
                            exit()


def iniciar_jogo():
    """Inicia o jogo e gerencia vitória ou derrota."""
    clock = pygame.time.Clock()
    while True:
        personagens_selecionados = desenha_menu(screen, screen_width, screen_height)
        if personagens_selecionados is None:
            break  # Volta para o menu principal

        personagens_selecionados_copy = copy.copy(personagens_selecionados)
        inimigos = Inimigo.cria_inimigos()
        ganhou = realiza_batalha(screen, personagens_selecionados, screen_width, screen_height)

        if ganhou:
            mensagem = 'Parabens, voce venceu!'
        else:
            mensagem = 'Você perdeu! Deseja tentar novamente?'

        tela_final(screen, personagens_selecionados_copy, inimigos, mensagem, screen_width, screen_height)
        opcao_pos_batalha = menu_pos_batalha(mensagem)

        if opcao_pos_batalha == "jogar":
            continue  # Reinicia a batalha
        elif opcao_pos_batalha == "menu":
            break  # Retorna ao menu principal
        elif opcao_pos_batalha == "sair":
            pygame.quit()
            exit()

        clock.tick(60)


def menu_pos_batalha(mensagem): 
    """Menu após a batalha, oferecendo opções de jogar novamente, voltar ao menu ou sair."""
    menu_options = ["Jogar Novamente", "Voltar ao Menu", "Sair"]
    selected_option = 0

    while True:
        # Calcula o tamanho do fundo com base nas opções
        max_text_width = max(font.size(option)[0] for option in menu_options)
        text_height = font.size(menu_options[0])[1]
        box_width = max_text_width + 100
        box_height = (text_height + 20) * len(menu_options) + 40

        # Fundo da mensagem semi-transparente
        background_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)
        background_surface.fill((50, 50, 50, 200))  # Cinza escuro semi-transparente
        pygame.draw.rect(background_surface, (150, 150, 150, 200), (0, 0, box_width, box_height), 5)
        screen.blit(background_surface, (screen_width // 2 - box_width // 2, screen_height // 2 - box_height // 2))

        # Renderiza o texto das opções
        for i, option in enumerate(menu_options):
            color = gold if i == selected_option else white
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - (len(menu_options) * text_height // 2) + i * (text_height + 20)))
            screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == K_RETURN:
                    if selected_option == 0:
                        return "jogar"
                    elif selected_option == 1:
                        return "menu"
                    elif selected_option == 2:
                        return "sair"



# Iniciar o programa principal
if __name__ == "__main__":
    menu_principal()
