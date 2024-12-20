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

def fade_transition(screen, image, fade_speed=5):
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

    # Renderiza a mensagem com o efeito de dissolução
    mensagem = font.render("Pressione qualquer tecla para continuar", True, gold)
    mensagem_rect = mensagem.get_rect(center=(screen_width // 2, (screen_height // 2) + 250))
    screen.blit(mensagem, mensagem_rect)
    pygame.display.flip()

    # Espera por uma tecla após 2 segundos
    if pygame.time.get_ticks() - start_time > 2500:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                running = False  # Fecha o loop após pressionar uma tecla

font = pygame.font.Font('fonts/god-of-war.ttf', 60) 
menu_options = ["Solo", "Dois Jogadores", "Sair"]
selected_option = 0

running = True
while running:
    # Carregar e exibir a imagem do menu
    menu_theme_image = pygame.image.load('images/menu/menu-modo-de-jogo.png')
    menu_theme_image = pygame.transform.scale(menu_theme_image, (screen_width, screen_height))
    screen.blit(menu_theme_image, (0, 0))

    # Renderizar opções do menu centralizadas com retângulos dourados
    for i, option in enumerate(menu_options):
        color = black if i == selected_option else gold
        text = font.render(option, True, color)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 - 100 + i * 80))

        # Desenhar retângulo dourado ao redor da opção selecionada
        if i == selected_option:
            pygame.draw.rect(screen, gold, text_rect.inflate(20, 10), border_radius=5, width=3)

        screen.blit(text, text_rect.topleft)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key in [K_RETURN, K_c]:
                fade_transition(screen, menu_theme_image)
                if selected_option == 0:
                    print("Modo Solo selecionado")
                    run = True
                    clock = pygame.time.Clock()

                    while run:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False

                        personagens_selecionados = desenha_menu(screen, screen_width, screen_height)
                        personagens_selecionados_copy = copy.copy(personagens_selecionados)
                        inimigos = Inimigo.cria_inimigos()
                        ganhou = realiza_batalha(screen, personagens_selecionados, screen_width, screen_height)

                        if ganhou:
                            mensagem = 'Parabens, voce venceu!'
                        else:
                            mensagem = 'Tente novamente, você perdeu!'

                        tela_final(screen, personagens_selecionados_copy, inimigos, mensagem, screen_width, screen_height)
                        pygame.display.flip()
                        clock.tick(60)

                    pygame.quit()
                elif selected_option == 1:
                    print("Modo Dois Jogadores selecionado")
                    # Implementar a lógica do modo de dois jogadores
                elif selected_option == 2:
                    running = False

pygame.quit()
