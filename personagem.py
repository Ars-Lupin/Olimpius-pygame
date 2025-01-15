import pygame  # type: ignore
from ataques import Ataque
from defesas import Defesa
from batalha import desenha_fundo, desenha_personagens, preenche_infos, desenha_inimigos

class Personagem:
    '''
    Atributos dos personagens:
        - Nome;
        - Ataque;
        - Defesa;
        - Vida máxima;
        - Vida atual;
        - Velocidade;
        - Imagem;
        - Defesa ativa;
        - Habilidade ativa;
        - Posição no menu principal;
        - Foi selecionado;
        - Vivo.
    '''

    def __init__(self, nome, forca, magia, controle, resistencia, velocidade, vida, vigor, src_imagem, src_imagem_menu, src_imagem_menu_selecionado, ataques, defesas):
        self.nome = nome
        self.forca = forca
        self.magia = magia
        self.controle = controle
        self.resistencia = resistencia
        self.velocidade = velocidade
        self.vigor = vigor
        self.vida_max = vida
        self.vida = vida
        self.imagem = pygame.image.load(src_imagem)
        self.imagem = pygame.transform.scale(self.imagem, (230, 230))
        self.lista_ataques = Ataque.cria_ataques(nome)
        self.lista_defesas = Defesa.cria_defesas(nome)

        self.defesa_ativa = False
        self.habilidade_ativa = False
        self.posicao_menu = None
        self.selecionado = False
        self.esta_vivo = True
        self.imagem_menu = pygame.image.load(src_imagem_menu)
        self.imagem_menu_selecionado = pygame.image.load(src_imagem_menu_selecionado)
        self.robos_ativos = [] if nome == "Hefesto" else None
        self.x = 0
        self.y = 0

    def exibir_imagem(self, tela, pos_x, pos_y):
        tela.blit(self.imagem, (pos_x, pos_y))

    @staticmethod
    def cria_personagens():
        # Lista de 20 personagens
        personagens = [
            Personagem('Afrodite', 60, 50, 110, 85, 70, 120, 100, 'images/batalha/afrodite.png', 'images/menu/afrodite-menu.png', 'images/menu/afrodite-menu-selecionado.png', Ataque.cria_ataques('Afrodite'), Defesa.cria_defesas('Afrodite')),
            Personagem('Alos', 75, 55, 130, 85, 80, 150, 120, 'images/batalha/alos.png', 'images/menu/alos-menu.png', 'images/menu/alos-menu-selecionado.png', Ataque.cria_ataques('Alos'), Defesa.cria_defesas('Alos')),
            Personagem('Apolo', 70, 60, 140, 85, 90, 130, 110, 'images/batalha/apolo.png', 'images/menu/apolo-menu.png', 'images/menu/apolo-menu-selecionado.png', Ataque.cria_ataques('Apolo'), Defesa.cria_defesas('Apolo')),
            Personagem('Ares', 90, 50, 140, 60, 85, 160, 100, 'images/batalha/ares.png', 'images/menu/ares-menu.png', 'images/menu/ares-menu-selecionado.png', Ataque.cria_ataques('Ares'), Defesa.cria_defesas('Ares')),
            Personagem('Artemis', 75, 55, 120, 90, 100, 140, 90, 'images/batalha/artemis.png', 'images/menu/artemis-menu.png', 'images/menu/artemis-menu-selecionado.png', Ataque.cria_ataques('Artemis'), Defesa.cria_defesas('Artemis')),
            Personagem('Atena', 70, 90, 130, 80, 95, 170, 120, 'images/batalha/atena.png', 'images/menu/atena-menu.png', 'images/menu/atena-menu-selecionado.png', Ataque.cria_ataques('Atena'), Defesa.cria_defesas('Atena')),
            Personagem('Celion', 70, 70, 140, 70, 80, 150, 100, 'images/batalha/celion.png', 'images/menu/celion-menu.png', 'images/menu/celion-menu-selecionado.png', Ataque.cria_ataques('Celion'), Defesa.cria_defesas('Celion')),
            Personagem('Demeter', 70, 70, 130, 70, 85, 160, 110, 'images/batalha/demeter.png', 'images/menu/demeter-menu.png', 'images/menu/demeter-menu-selecionado.png', Ataque.cria_ataques('Demeter'), Defesa.cria_defesas('Demeter')),
            Personagem('Dionisio', 80, 70, 130, 70, 80, 170, 120, 'images/batalha/dionisio.png', 'images/menu/dionisio-menu.png', 'images/menu/dionisio-menu-selecionado.png', Ataque.cria_ataques('Dionisio'), Defesa.cria_defesas('Dionisio')),
            Personagem('Draktel', 90, 80, 160, 60, 70, 180, 130, 'images/batalha/draktel.png', 'images/menu/draktel-menu.png', 'images/menu/draktel-menu-selecionado.png', Ataque.cria_ataques('Draktel'), Defesa.cria_defesas('Draktel')),
            Personagem('Hades', 95, 70, 170, 60, 85, 200, 140, 'images/batalha/hades.png', 'images/menu/hades-menu.png', 'images/menu/hades-menu-selecionado.png', Ataque.cria_ataques('Hades'), Defesa.cria_defesas('Hades')),
            Personagem('Hefesto', 70, 80, 150, 50, 80, 190, 140, 'images/batalha/hefesto.png', 'images/menu/hefesto-menu.png', 'images/menu/hefesto-menu-selecionado.png', Ataque.cria_ataques('Hefesto'), Defesa.cria_defesas('Hefesto')),
            Personagem('Hera', 65, 75, 140, 75, 80, 170, 120, 'images/batalha/hera.png', 'images/menu/hera-menu.png', 'images/menu/hera-menu-selecionado.png', Ataque.cria_ataques('Hera'), Defesa.cria_defesas('Hera')),
            Personagem('Hercules', 100, 90, 200, 50, 85, 210, 150, 'images/batalha/hercules.png', 'images/menu/hercules-menu.png', 'images/menu/hercules-menu-selecionado.png', Ataque.cria_ataques('Hercules'), Defesa.cria_defesas('Hercules')),
            Personagem('Hermes', 60, 45, 120, 95, 100, 140, 100, 'images/batalha/hermes.png', 'images/menu/hermes-menu.png', 'images/menu/hermes-menu-selecionado.png', Ataque.cria_ataques('Hermes'), Defesa.cria_defesas('Hermes')),
            Personagem('Luna', 85, 65, 150, 80, 90, 180, 130, 'images/batalha/luna.png', 'images/menu/luna-menu.png', 'images/menu/luna-menu-selecionado.png', Ataque.cria_ataques('Luna'), Defesa.cria_defesas('Luna')),
            Personagem('Pantheon', 100, 100, 200, 50, 85, 230, 160, 'images/batalha/pantheon.png', 'images/menu/pantheon-menu.png', 'images/menu/pantheon-menu-selecionado.png', Ataque.cria_ataques('Pantheon'), Defesa.cria_defesas('Pantheon')),
            Personagem('Poseidon', 85, 65, 160, 65, 85, 190, 140, 'images/batalha/poseidon.png', 'images/menu/poseidon-menu.png', 'images/menu/poseidon-menu-selecionado.png', Ataque.cria_ataques('Poseidon'), Defesa.cria_defesas('Poseidon')),
            Personagem('Shaya', 65, 60, 125, 90, 90, 160, 120, 'images/batalha/shaya.png', 'images/menu/shaya-menu.png', 'images/menu/shaya-menu-selecionado.png', Ataque.cria_ataques('Shaya'), Defesa.cria_defesas('Shaya')),
            Personagem('Zeus', 80, 60, 150, 70, 95, 170, 130, 'images/batalha/zeus.png', 'images/menu/zeus-menu.png', 'images/menu/zeus-menu-selecionado.png', Ataque.cria_ataques('Zeus'), Defesa.cria_defesas('Zeus'))
        ]
        return personagens
    def ataca_inimigo(self, tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        pos_seta = inimigos[0].posicao_batalha
        img_seta = pygame.image.load('images/batalha/seta.png')
        img_seta = pygame.transform.scale(img_seta, (300, 300))

        # Variável para controlar o ataque selecionado
        ataque_selecionado = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        pos_seta = Personagem.move_seta(inimigos, pos_seta, 'up')
                    elif event.key == pygame.K_DOWN:
                        pos_seta = Personagem.move_seta(inimigos, pos_seta, 'down')
                    elif event.key == pygame.K_LEFT:
                        ataque_selecionado = max(0, ataque_selecionado - 1)
                    elif event.key == pygame.K_RIGHT:
                        ataque_selecionado = min(len(self.lista_ataques) - 1, ataque_selecionado + 1)
                    elif event.key == pygame.K_z:
                        inimigo = next((i for i in inimigos if i.posicao_batalha == pos_seta), None)
                        if inimigo:
                            ataque = self.lista_ataques[ataque_selecionado]
                            dano = ataque.calcula_dano(self, inimigo)  # Usando cálculo do ataque
                            inimigo.vida -= dano
                            if inimigo.vida <= 0:
                                inimigo.esta_vivo = False
                                inimigos.remove(inimigo)
                            return True
                    elif event.key == pygame.K_x:
                        return False

            # Atualização da tela
            desenha_fundo(tela, personagens_selecionados, screen_width, screen_height)
            desenha_personagens(tela, personagens_selecionados, screen_width, screen_height)
            desenha_inimigos(tela, inimigos, screen_width, screen_height)
            preenche_infos(tela, personagens_selecionados, personagem_atual, screen_width, screen_height)

            # Mostrar a seta no inimigo selecionado
            tela.blit(img_seta, pos_seta)

            # Exibir ataque selecionado na interface
            texto_ataque = f"Ataque: {self.lista_ataques[ataque_selecionado].nome}"
            fonte = pygame.font.Font(None, 36)
            texto_surface = fonte.render(texto_ataque, True, (255, 255, 255))
            tela.blit(texto_surface, (50, screen_height - 50))

            pygame.display.flip()
        
    @staticmethod
    def verifica_personagens_vivos(personagens_selecionados):
        personagens_selecionados[:] = [p for p in personagens_selecionados if p.esta_vivo]

    @staticmethod
    def move_seta(inimigos, pos_seta, direcao):
        if direcao == 'up':
            for i in range(1, len(inimigos)):
                if pos_seta == inimigos[i].posicao_batalha:
                    pos_seta = inimigos[i - 1].posicao_batalha
                    break
        elif direcao == 'down':
            for i in range(len(inimigos) - 1):
                if pos_seta == inimigos[i].posicao_batalha:
                    pos_seta = inimigos[i + 1].posicao_batalha
                    break
        return pos_seta


