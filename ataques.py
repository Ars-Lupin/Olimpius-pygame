import random
import pygame
import os
from pygame.locals import *  
class Ataque:
    """
    Classe para gerenciar os ataques de cada personagem.
    """

    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao
        
    class Robo:
        def __init__(self, nome, forca, magia, controle, resistencia, velocidade, vigor, vida, src_imagem, x, y):
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
            self.imagem = pygame.transform.scale(self.imagem, (200, 200))  # Ajuste da imagem
            self.lista_ataques = Ataque.cria_ataques(nome)
            self.lista_defesas = None
            self.defesa_ativa = False
            self.habilidade_ativa = False
            self.posicao_menu = None
            self.selecionado = False
            self.esta_vivo = True
            self.x = x
            self.y = y

        def desenhar(self, tela):
            tela.blit(self.imagem, (self.x, self.y))
            # Desenhar barra de vida
            largura_barra = 100
            altura_barra = 10
            vida_ratio = max(0, self.vida / self.vida_max)
            pygame.draw.rect(tela, (255, 0, 0), (self.x + 50, self.y-200, largura_barra, altura_barra))  # Barra total
            pygame.draw.rect(tela, (0, 255, 0), (self.x + 50, self.y-200, largura_barra * vida_ratio, altura_barra))  # Vida restante

        def receber_dano(self, dano):
            self.vida -= dano
            if self.vida <= 0:
                self.esta_vivo = False
    
    @staticmethod         
    def exibir_animacao(tela, caminho_pasta, pos_x, pos_y, frame_rate=0.1):
        quadros = sorted([
            os.path.join(caminho_pasta, f)
            for f in os.listdir(caminho_pasta)
            if f.endswith('.png') or f.endswith('.jpg')
        ])
        
        for quadro in quadros:
            imagem = pygame.image.load(quadro)
            imagem = pygame.transform.scale(imagem, (200, 200))
            tela.blit(imagem, (pos_x, pos_y))
            pygame.display.update()
            pygame.time.delay(int(frame_rate * 1000))


    def uso(self, tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        """
        Executa a função do ataque.
        """
        self.funcao(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height)

    @staticmethod
    def cria_ataques(nome_personagem):
        """
        Retorna uma lista de ataques com base no nome do personagem.
        Cada ataque é uma instância da classe Ataque, com nome e função associados.
        """
        ataques_por_personagem = {
            'Afrodite': [
                Ataque('Lança Divina', Ataque.lanca_divina),
                Ataque('Escudo de Luz', Ataque.escudo_de_luz),
                Ataque('Flecha Sagrada', Ataque.flecha_sagrada),
                Ataque('Ataque Solar', Ataque.ataque_solar),
                Ataque('Chuva de Luz', Ataque.chuva_de_luz),
                Ataque('Explosão Celestial', Ataque.explosao_celestial),
            ],
            'Zeus': [
                Ataque('Julgamento Divino', Ataque.julgamento_divino),
                Ataque('Raio Divino', Ataque.raio_divino),
                Ataque('Tempestade divina', Ataque.tempestade),
                Ataque('Punho Trovão', Ataque.soco),
                Ataque('Explosão de Trovão', Ataque.explosao_de_trovão),
                Ataque('Matador de Chronos', Ataque.matador_de_chronos),
            ],
            'Alos': [
                Ataque('Relâmpago', Ataque.relampago),
                Ataque('Raio Divino', Ataque.raio_divino),
                Ataque('Tempestade', Ataque.tempestade),
                Ataque('Fúria do Olimpo', Ataque.furia_do_olimpo),
                Ataque('Explosão de Trovão', Ataque.explosao_de_trovão),
                Ataque('Tremores da alma', Ataque.tremores_da_alma),
            ],
            'Celion': None,
            'Draktel': None,
            'Hefesto': [
                Ataque('Punho forjador', Ataque.soco),
                Ataque('Criação divina', Ataque.criar_robos),
                Ataque('Destruir pra construir', Ataque.destruir_pra_construir),
            ],
            'Hercules': [                
                Ataque('Touro de Creta', Ataque.flecha_solar),
                Ataque('Cavalos de Diomedes', Ataque.explosao_solar),
                Ataque('Aves do lago Estínfalo', Ataque.musica_curativa),
                Ataque('Luz da Verdade', Ataque.luz_da_verdade),
                Ataque('Chuva de Flechas', Ataque.chuva_de_flechas),
                Ataque('Aura Radiante', Ataque.aura_radiante),
                ],
            'Hermes': None,
            'Luna': None,
            'Pantheon': None,
            'Poseidon': None,
            'Shaya': None,
            'Apolo': [
                Ataque('Flecha Solar', Ataque.flecha_solar),
                Ataque('Explosão Solar', Ataque.explosao_solar),
                Ataque('Música Curativa', Ataque.musica_curativa),
                Ataque('Luz da Verdade', Ataque.luz_da_verdade),
                Ataque('Chuva de Flechas', Ataque.chuva_de_flechas),
                Ataque('Aura Radiante', Ataque.aura_radiante),
            ],
            'Ares': [
                Ataque('Golpe de Espada', Ataque.golpe_de_espada),
                Ataque('Carga Violenta', Ataque.carga_violenta),
                Ataque('Bandeira da Guerra', Ataque.bandeira_da_guerra),
                Ataque('Rugido de Guerra', Ataque.rugido_de_guerra),
                Ataque('Fúria do Campo de Batalha', Ataque.furia_do_campo),
                Ataque('Chamas da Guerra', Ataque.chamas_da_guerra),
            ],
            'Artemis': [
                Ataque('Flecha da Lua', Ataque.flecha_da_lua),
                Ataque('Armadilha da Floresta', Ataque.armadilha_da_floresta),
                Ataque('Invocação de Lobos', Ataque.invocacao_de_lobos),
                Ataque('Tiro Múltiplo', Ataque.tiro_multiplo),
                Ataque('Sombra da Noite', Ataque.sombra_da_noite),
                Ataque('Golpe da Lua Cheia', Ataque.golpe_da_lua),
            ],
            'Atena': [
                Ataque('Lança da Justiça', Ataque.lanca_da_justica),
                Ataque('Escudo Protetor', Ataque.escudo_protetor),
                Ataque('Estratégia Divina', Ataque.estrategia_divina),
                Ataque('Chama da Sabedoria', Ataque.chama_da_sabedoria),
                Ataque('Olhar de Coruja', Ataque.olhar_de_coruja),
                Ataque('Investida da Lança', Ataque.investida_da_lanca),
            ],
            'Demeter': [
                Ataque('Crescimento Rápido', Ataque.crescimento_rapido),
                Ataque('Chicote de Videiras', Ataque.chicote_de_videiras),
                Ataque('Colheita Curativa', Ataque.colheita_curativa),
                Ataque('Campos Férteis', Ataque.campos_ferteis),
                Ataque('Terremoto Verde', Ataque.terremoto_verde),
                Ataque('Sementes Explosivas', Ataque.sementes_explosivas),
            ],
            'Dionisio': [
                Ataque('Brinde Caótico', Ataque.brinde_caotico),
                Ataque('Chuva de Vinho', Ataque.chuva_de_vinho),
                Ataque('Festa Explosiva', Ataque.festa_explosiva),
                Ataque('Névoa da Embriaguez', Ataque.nevoa_da_embriaguez),
                Ataque('Sopro Caótico', Ataque.sopro_caotico),
                Ataque('Ritual Selvagem', Ataque.ritual_selvagem),
            ],
            'Hades': [
                Ataque('Explosão Sombria', Ataque.explosao_sombria),
                Ataque('Correntes das Almas', Ataque.correntes_das_almas),
                Ataque('Chama do Submundo', Ataque.chama_do_submundo),
                Ataque('Exército de Espectros', Ataque.exercito_de_espectros),
                Ataque('Aura Sombria', Ataque.aura_sombria),
                Ataque('Portal das Trevas', Ataque.portal_das_trevas),
            ],
            'Poseidon': [
                Ataque('Tridente das Profundezas', Ataque.tridente_das_profundezas),
                Ataque('Tsunami Avassalador', Ataque.tsunami_avassalador),
                Ataque('Prisão de Água', Ataque.prisao_de_agua),
                Ataque('Redemoinho', Ataque.redemoinho),
                Ataque('Espíritos do Mar', Ataque.espiritos_do_mar),
                Ataque('Fúria dos Mares', Ataque.furia_dos_mares),
            ],
            'Hera': [
                Ataque('Olhar Imponente', Ataque.olhar_imponente),
                Ataque('Escudo Divino', Ataque.escudo_divino),
                Ataque('Chicote de Poder', Ataque.chicote_de_poder),
                Ataque('Fúria da Rainha', Ataque.furia_da_rainha),
                Ataque('Raio do Céu', Ataque.raio_do_ceu),
                Ataque('Aura de Comando', Ataque.aura_de_comando),
            ],


        }

        return ataques_por_personagem.get(nome_personagem, None)

    @staticmethod
    def lanca_divina(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Lança Divina!")
        for inimigo in inimigos:
            inimigo.vida -= 10  # Dano de exemplo

    @staticmethod
    def escudo_de_luz(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Escudo de Luz!")
        personagem_atual.defesa += 5  # Aumento de defesa de exemplo

    @staticmethod
    def flecha_sagrada(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Flecha Sagrada!")
        if inimigos:
            inimigo = inimigos[0]  # Ataca o primeiro inimigo
            inimigo.vida -= 15  # Dano de exemplo

    @staticmethod
    def ataque_solar(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Ataque Solar!")
        for inimigo in inimigos:
            inimigo.vida -= 12  # Dano de exemplo

    @staticmethod
    def chuva_de_luz(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Chuva de Luz!")
        for personagem in personagens_selecionados:
            personagem.vida = min(personagem.vida_max, personagem.vida + 10)  # Cura de exemplo

    @staticmethod
    def explosao_celestial(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Explosão Celestial!")
        for inimigo in inimigos:
            inimigo.vida -= 20  # Dano de exemplo

    # Ataques de Zeus
    @staticmethod
    def relampago(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Relâmpago!")
        for inimigo in inimigos:
            inimigo.vida -= 10

    @staticmethod
    def raio_divino(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Raio Divino!")
        for inimigo in inimigos:
            inimigo.vida -= 12

    @staticmethod
    def tempestade(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Tempestade!")
        for inimigo in inimigos:
            inimigo.vida -= 15

    @staticmethod
    def furia_do_olimpo(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Fúria do Olimpo!")
        for inimigo in inimigos:
            inimigo.vida -= 20

    @staticmethod
    def explosao_de_trovão(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Explosão de Trovão!")
        for inimigo in inimigos:
            inimigo.vida -= 25

    @staticmethod
    def chuva_de_raios(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Chuva de Raios!")
        for inimigo in inimigos:
            inimigo.vida -= 10
            
    @staticmethod
    def matador_de_chronos(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Matador de Chronos!")
        for inimigo in inimigos:
            inimigo.vida -= 90
            
    @staticmethod
    def tremores_da_alma(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Tremores da Alma!")
        for inimigo in inimigos:
            inimigo.vida -= 25

    def julgamento_divino(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Julgamento Divino!")
        
        pos_x = screen_width * 0.65
        pos_y += screen_height * 0.25
        
        Ataque.exibir_animacao(tela, 'images/poderes/julgamento_divino', pos_x, pos_y)
        
        for inimigo in inimigos:
            inimigo.vida -= 80
            
    @staticmethod
    def soco(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Punho Trovão!")
        for inimigo in inimigos:
            dano = personagem_atual.forca * 1.2 - inimigo.defesa
            inimigo.vida -= dano
    
    @staticmethod
    def relampago(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Relâmpago!")
        for inimigo in inimigos:
            inimigo.vida -= 10

    @staticmethod
    def criar_robos(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        # Limite de robôs em campo
        max_robos = 3
        
        # Verifica se o personagem já alcançou o limite de robôs
        if len(personagem_atual.robos_ativos) >= max_robos:
            print("Você já atingiu o limite de robôs em campo!")
            return []

        print(f"{personagem_atual.nome} usou Criação Divina!")
        
        # Lista de robôs com todos os atributos
        robos_disponiveis = {
            'ares': {'forca': 50, 'magia': 20, 'controle': 30, 'resistencia': 35, 'velocidade': 40, 'vigor': 45, 'vida': 100, 'imagem': 'images/poderes/robo-ares.png'},
            'zeus': {'forca': 60, 'magia': 50, 'controle': 40, 'resistencia': 45, 'velocidade': 50, 'vigor': 55, 'vida': 120, 'imagem': 'images/poderes/robo-zeus.png'},
            'afrodite': {'forca': 40, 'magia': 60, 'controle': 50, 'resistencia': 30, 'velocidade': 35, 'vigor': 40, 'vida': 80, 'imagem': 'images/poderes/robo-afrodite.png'},
            'apolo': {'forca': 45, 'magia': 35, 'controle': 50, 'resistencia': 40, 'velocidade': 45, 'vigor': 50, 'vida': 90, 'imagem': 'images/poderes/robo-apolo.png'},
            'artemis': {'forca': 40, 'magia': 45, 'controle': 50, 'resistencia': 30, 'velocidade': 60, 'vigor': 55, 'vida': 85, 'imagem': 'images/poderes/robo-artemis.png'},
            'atena': {'forca': 50, 'magia': 45, 'controle': 40, 'resistencia': 60, 'velocidade': 50, 'vigor': 55, 'vida': 110, 'imagem': 'images/poderes/robo-atena.png'},
            'poseidon': {'forca': 55, 'magia': 50, 'controle': 55, 'resistencia': 60, 'velocidade': 45, 'vigor': 50, 'vida': 130, 'imagem': 'images/poderes/robo-poseidon.png'},
            'hades': {'forca': 60, 'magia': 40, 'controle': 50, 'resistencia': 70, 'velocidade': 45, 'vigor': 60, 'vida': 150, 'imagem': 'images/poderes/robo-hades.png'},
            'demeter': {'forca': 40, 'magia': 35, 'controle': 40, 'resistencia': 50, 'velocidade': 45, 'vigor': 50, 'vida': 100, 'imagem': 'images/poderes/robo-demeter.png'},
            'dionisio': {'forca': 45, 'magia': 60, 'controle': 50, 'resistencia': 45, 'velocidade': 55, 'vigor': 50, 'vida': 110, 'imagem': 'images/poderes/robo-dionisio.png'},
            'hera': {'forca': 55, 'magia': 50, 'controle': 45, 'resistencia': 55, 'velocidade': 60, 'vigor': 50, 'vida': 120, 'imagem': 'images/poderes/robo-hera.png'},
            'hermes': {'forca': 45, 'magia': 35, 'controle': 45, 'resistencia': 40, 'velocidade': 65, 'vigor': 50, 'vida': 90, 'imagem': 'images/poderes/robo-hermes.png'},
        }

        ataques_especificos = {
            'ares': [Ataque('Golpe de Espada', Ataque.golpe_de_espada)],
            'zeus': [Ataque('Raio Divino', Ataque.raio_divino)],
            'afrodite': [Ataque('Flecha Sagrada', Ataque.flecha_sagrada)],
            'apolo': [Ataque('Flecha Solar', Ataque.flecha_solar)],
            'artemis': [Ataque('Flecha da Lua', Ataque.flecha_da_lua)],
            'atena': [Ataque('Lança da Justiça', Ataque.lanca_da_justica)],
            'poseidon': [Ataque('Tridente das Profundezas', Ataque.tridente_das_profundezas)],
            'hades': [Ataque('Explosão Sombria', Ataque.explosao_sombria)],
            'demeter': [Ataque('Crescimento Rápido', Ataque.crescimento_rapido)],
            'dionisio': [Ataque('Brinde Caótico', Ataque.brinde_caotico)],
            'hera': [Ataque('Olhar Imponente', Ataque.olhar_imponente)],
            'hermes': [Ataque('Velocidade Celestial', Ataque.velocidade_celestial)],
        }
        robos_restantes = [robo for robo in robos_disponiveis.keys() if robo not in [r.nome for r in personagem_atual.robos_ativos]]

        if not robos_restantes:
            print("Não há robôs disponíveis para criar.")
            return None

        # Seleciona um robô aleatório
        robo_nome = random.choice(robos_restantes)
        dados_robo = robos_disponiveis[robo_nome]
        caminho_imagem = dados_robo['imagem']
        if len(personagem_atual.robos_ativos) == 0:
            x = personagem_atual.x + 150
            y = personagem_atual.y - 50
        elif len(personagem_atual.robos_ativos) == 1:
            x = personagem_atual.x + 250
            y = personagem_atual.y + 0
        else:  
            x = personagem_atual.x + 150
            y = personagem_atual.y + 50
        
        robo = Ataque.Robo(
            robo_nome,
            dados_robo['forca'],
            dados_robo['magia'],
            dados_robo['controle'],
            dados_robo['resistencia'],
            dados_robo['velocidade'],
            dados_robo['vigor'],
            dados_robo['vida'],
            caminho_imagem,
            x, y
        )

        # Adiciona o robô à lista de robôs ativos do personagem
        personagem_atual.robos_ativos.append(robo)

        # Adiciona os ataques específicos do robô à lista de ataques do personagem
        personagem_atual.lista_ataques.extend(ataques_especificos[robo_nome])

        # Efeito nos inimigos (reduzindo vida)
        for inimigo in inimigos:
            inimigo.vida -= 15

        # Log do robô criado
        print(f"Robô gerado: {robo_nome}")
        return robo
        
    @staticmethod
    def destruir_pra_construir(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Destruir pra Construir!")
        for inimigo in inimigos:
            inimigo.vida -= 20
            
    @staticmethod
    def flecha_solar(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Flecha Solar!")
        for inimigo in inimigos:
            inimigo.vida -= 10
    
    @staticmethod
    def explosao_solar(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Explosão Solar!")
        for inimigo in inimigos:
            inimigo.vida -= 15
    
    @staticmethod
    def musica_curativa(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Música Curativa!")
        for personagem in personagens_selecionados:
            personagem.vida = min(personagem.vida_max, personagem.vida + 10)
            
    @staticmethod
    def luz_da_verdade(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Luz da Verdade!")
        for inimigo in inimigos:
            inimigo.vida -= 15
            
    @staticmethod
    def chuva_de_flechas(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Chuva de Flechas!")
        for inimigo in inimigos:
            inimigo.vida -= 20
            
    @staticmethod
    def aura_radiante(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Aura Radiante!")
        for inimigo in inimigos:
            inimigo.vida -= 25
            
    @staticmethod
    def flecha_da_lua(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Flecha da Lua!")
        for inimigo in inimigos:
            inimigo.vida -= 10
            
    @staticmethod
    def armadilha_da_floresta(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Armadilha da Floresta!")
        for inimigo in inimigos:
            inimigo.vida -= 15
    
    @staticmethod
    def invocacao_de_lobos(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Invocação de Lobos!")
        for inimigo in inimigos:
            inimigo.vida -= 20
            
    @staticmethod
    def tiro_multiplo(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Tiro Múltiplo!")
        for inimigo in inimigos:
            inimigo.vida -= 25
            
    @staticmethod
    def sombra_da_noite(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Sombra da Noite!")
        for inimigo in inimigos:
            inimigo.vida -= 30
            
    @staticmethod
    def golpe_da_lua(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Golpe da Lua!")
        for inimigo in inimigos:
            inimigo.vida -= 35
            
    @staticmethod
    def lanca_da_justica(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Lança da Justiça!")
        for inimigo in inimigos:
            inimigo.vida -= 10
            
    @staticmethod
    def escudo_protetor(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Escudo Protetor!")
        personagem_atual.defesa += 5
        
    @staticmethod
    def estrategia_divina(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Estratégia Divina!")
        personagem_atual.defesa += 10
        
    @staticmethod
    def chama_da_sabedoria(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Chama da Sabedoria!")
        for inimigo in inimigos:
            inimigo.vida -= 15
            
    @staticmethod
    def olhar_de_coruja(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Olhar de Coruja!")
        for inimigo in inimigos:
            inimigo.vida -= 20
            
    @staticmethod
    def investida_da_lanca(tela, inimigos, personagens_selecionados, personagem_atual, screen_width, screen_height):
        print(f"{personagem_atual.nome} usou Investida da Lança!")
        for inimigo in inimigos:
            inimigo.vida -= 25
            
        # Funções dos ataques
    def crescimento_rapido(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Crescimento Rápido!")
        # Aumenta a defesa ou outro atributo
        personagem_atual.defesa += 10

    def chicote_de_videiras(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Chicote de Videiras!")
        for inimigo in inimigos:
            inimigo.vida -= 20

    def colheita_curativa(tela, personagem_atual):
        print(f"{personagem_atual.nome} usou Colheita Curativa!")
        personagem_atual.vida += 30

    def campos_ferteis(tela, personagem_atual):
        print(f"{personagem_atual.nome} usou Campos Férteis!")
        personagem_atual.recuperar_energia(20)

    def terremoto_verde(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Terremoto Verde!")
        for inimigo in inimigos:
            inimigo.vida -= 25

    def sementes_explosivas(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Sementes Explosivas!")
        for inimigo in inimigos:
            inimigo.vida -= 30


    # Dionísio
    def brinde_caotico(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Brinde Caótico!")
        for inimigo in inimigos:
            inimigo.ataque -= 5

    def chuva_de_vinho(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Chuva de Vinho!")
        for inimigo in inimigos:
            inimigo.vida -= 15

    def festa_explosiva(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Festa Explosiva!")
        for inimigo in inimigos:
            inimigo.vida -= 25

    def nevoa_da_embriaguez(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Névoa da Embriaguez!")
        for inimigo in inimigos:
            inimigo.precisao -= 10

    def sopro_caotico(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Sopro Caótico!")
        for inimigo in inimigos:
            inimigo.velocidade -= 10

    def ritual_selvagem(tela, personagem_atual):
        print(f"{personagem_atual.nome} usou Ritual Selvagem!")
        personagem_atual.ataque += 15


    # Hades
    def explosao_sombria(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Explosão Sombria!")
        for inimigo in inimigos:
            inimigo.vida -= 40

    def correntes_das_almas(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Correntes das Almas!")
        for inimigo in inimigos:
            inimigo.movimento -= 15

    def chama_do_submundo(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Chama do Submundo!")
        for inimigo in inimigos:
            inimigo.vida -= 20

    def exercito_de_espectros(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Exército de Espectros!")
        for inimigo in inimigos:
            inimigo.vida -= 25

    def aura_sombria(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Aura Sombria!")
        for inimigo in inimigos:
            inimigo.ataque -= 10

    def portal_das_trevas(tela, personagem_atual):
        print(f"{personagem_atual.nome} usou Portal das Trevas!")
        personagem_atual.vida += 25


    # Poseidon
    def tridente_das_profundezas(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Tridente das Profundezas!")
        for inimigo in inimigos:
            inimigo.vida -= 35

    def tsunami_avassalador(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Tsunami Avassalador!")
        for inimigo in inimigos:
            inimigo.movimento -= 20

    def prisao_de_agua(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Prisão de Água!")
        for inimigo in inimigos:
            inimigo.movimento -= 15

    def redemoinho(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Redemoinho!")
        for inimigo in inimigos:
            inimigo.vida -= 20

    def espiritos_do_mar(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Espíritos do Mar!")
        for inimigo in inimigos:
            inimigo.ataque -= 10

    def furia_dos_mares(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Fúria dos Mares!")
        for inimigo in inimigos:
            inimigo.vida -= 50


    # Hera
    def olhar_imponente(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Olhar Imponente!")
        for inimigo in inimigos:
            inimigo.ataque -= 10

    def escudo_divino(tela, personagem_atual):
        print(f"{personagem_atual.nome} usou Escudo Divino!")
        personagem_atual.defesa += 20

    def chicote_de_poder(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Chicote de Poder!")
        for inimigo in inimigos:
            inimigo.vida -= 30

    def furia_da_rainha(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Fúria da Rainha!")
        for inimigo in inimigos:
            inimigo.vida -= 40

    def raio_do_ceu(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Raio do Céu!")
        for inimigo in inimigos:
            inimigo.vida -= 25

    def aura_de_comando(tela, personagem_atual):
        print(f"{personagem_atual.nome} usou Aura de Comando!")
        personagem_atual.ataque += 10
        
    def golpe_de_espada(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Golpe de Espada!")
        for inimigo in inimigos:
            inimigo.vida -= 10
    
    def carga_violenta(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Carga Violenta!")
        for inimigo in inimigos:
            inimigo.vida -= 15
            
    def bandeira_da_guerra(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Bandeira da Guerra!")
        for inimigo in inimigos:
            inimigo.vida -= 20

    def rugido_de_guerra(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Rugido de Guerra!")
        for inimigo in inimigos:
            inimigo.vida -= 25
            
    def furia_do_campo(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Fúria do Campo de Batalha!")
        for inimigo in inimigos:
            inimigo.vida -= 30
            
    def chamas_da_guerra(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Chamas da Guerra!")
        for inimigo in inimigos:
            inimigo.vida -= 35
    
    def velocidade_celestial(tela, personagem_atual, inimigos):
        print(f"{personagem_atual.nome} usou Velocidade Celestial!")
        for inimigo in inimigos:
            inimigo.vida += 30
    

            
