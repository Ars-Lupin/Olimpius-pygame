import pygame # type: ignore
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

    def __init__(self, nome, ataque, defesa, vida_max, velocidade, src_imagem, src_imagem_menu, src_imagem_menu_selecionado):
        self.nome = nome
        self.ataque = ataque
        self.defesa = defesa
        self.vida_max = vida_max
        self.vida = vida_max
        self.velocidade = velocidade
        self.imagem = pygame.image.load(src_imagem)
        self.imagem = pygame.transform.scale(self.imagem, (230, 230))

        if self.nome == 'Poseidon':
            self.imagem = pygame.transform.scale(self.imagem, (255, 255))

        self.defesa_ativa = False
        self.habilidade_ativa = False
        self.posicao_menu = None
        self.selecionado = False
        self.esta_vivo = True
        self.imagem_menu = pygame.image.load(src_imagem_menu)
        self.imagem_menu_selecionado = pygame.image.load(src_imagem_menu_selecionado)

    def exibir_imagem(self, tela, pos_x, pos_y):
        tela.blit(self.imagem_atual, (pos_x, pos_y))

    @staticmethod
    def cria_personagens():
        # Criando as instâncias dos personagens e salvando em uma lista.
        return [
            Personagem('Zeus', 80, 60, 150, 70, 'images/batalha/zeus.png', 'images/menu/zeus-menu.png', 'images/menu/zeus-menu-selecionado.png'),
            Personagem('Atena', 70, 90, 130, 80, 'images/batalha/atena.png', 'images/menu/atena-menu.png', 'images/menu/atena-menu-selecionado.png'),
            Personagem('Ares', 90, 50, 140, 60, 'images/batalha/ares.png', 'images/menu/ares-menu.png', 'images/menu/ares-menu-selecionado.png'),
            Personagem('Artemis', 75, 55, 120, 90, 'images/batalha/artemis.png', 'images/menu/artemis-menu.png', 'images/menu/artemis-menu-selecionado.png'),
            Personagem('Poseidon', 85, 65, 160, 65, 'images/batalha/poseidon.png', 'images/menu/poseidon-menu.png', 'images/menu/poseidon-menu-selecionado.png')
        ]
    
    def ataca_inimigo(self, tela, inimigos, personagens_selecionados, personagem_atual):
        pos_seta = inimigos[0].posicao_batalha
        img_seta = pygame.image.load('images/batalha/seta.png')
        img_seta = pygame.transform.scale(img_seta, (300, 300))

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
                    elif event.key == pygame.K_z:
                        inimigo = None

                        for i in inimigos:
                            if i.posicao_batalha == pos_seta:
                                inimigo = i
                                break

                        if inimigo is not None:
                            dano = round(self.ataque * (50 / (50 + inimigo.defesa)))
                            inimigo.vida -= dano

                            if inimigo.vida <= 0:
                                inimigo.esta_vivo = False
                                inimigos.remove(inimigo)
                            return True
                    elif event.key == pygame.K_x:
                        return False
            
            desenha_fundo(tela, personagens_selecionados)
            desenha_personagens(tela, personagens_selecionados)
            desenha_inimigos(tela, inimigos)
            preenche_infos(tela, personagens_selecionados, personagem_atual)
            tela.blit(img_seta, pos_seta)
            pygame.display.flip()

    @staticmethod
    def verifica_personagens_vivos(personagens_selecionados):
        for personagem in personagens_selecionados:
            if not personagem.esta_vivo:
                personagens_selecionados.remove(personagem)

    @staticmethod
    def move_seta(inimigos, pos_seta, direcao):
        if direcao == 'up':
            if len(inimigos) >= 2 and pos_seta[0] == inimigos[1].posicao_batalha[0] and pos_seta[1] == inimigos[1].posicao_batalha[1]:
                pos_seta = (inimigos[0].posicao_batalha[0], inimigos[0].posicao_batalha[1])
        elif direcao == 'down':
            if len(inimigos) >= 2 and pos_seta[0] == inimigos[0].posicao_batalha[0] and pos_seta[1] == inimigos[0].posicao_batalha[1]:
                pos_seta = (inimigos[1].posicao_batalha[0], inimigos[1].posicao_batalha[1])
        return pos_seta
    
    def defende(self):
        self.defesa_ativa = True
        self.defesa *= 2

    @staticmethod
    def retira_defesa(personagens_selecionados):
        for personagem in personagens_selecionados:
            if personagem.defesa_ativa:
                personagem.defesa_ativa = False
                personagem.defesa //= 2

    def habilidade(self):
        self.habilidade_ativa = True
        self.ataque = round(self.ataque * 1.35)

    @staticmethod
    def retira_habilidade(personagens_selecionados):
        for personagem in personagens_selecionados:
            if personagem.habilidade_ativa:
                personagem.habilidade_ativa = False
                personagem.ataque //= 1.35