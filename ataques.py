class Ataque:
    """
    Classe para gerenciar os ataques de cada personagem.
    """

    def __init__(self, nome, funcao):
        self.nome = nome
        self.funcao = funcao

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
                Ataque('Relâmpago', Ataque.relampago),
                Ataque('Raio Divino', Ataque.raio_divino),
                Ataque('Tempestade', Ataque.tempestade),
                Ataque('Fúria do Olimpo', Ataque.furia_do_olimpo),
                Ataque('Explosão de Trovão', Ataque.explosao_de_trovão),
                Ataque('Chuva de Raios', Ataque.chuva_de_raios),
            ],
            'Alos': [
                Ataque('Relâmpago', Ataque.relampago),
                Ataque('Raio Divino', Ataque.raio_divino),
                Ataque('Tempestade', Ataque.tempestade),
                Ataque('Fúria do Olimpo', Ataque.furia_do_olimpo),
                Ataque('Explosão de Trovão', Ataque.explosao_de_trovão),
                Ataque('Chuva de Raios', Ataque.chuva_de_raios),
            ],
            'Apolo': None,
            'Ares': None,
            'Artemis': None,
            'Atena': None,
            'Celion': None,
            'Demeter': None,
            'Dionisio': None,
            'Draktel': None,
            'Hades': None,
            'Hefesto': None,
            'Hera': None,
            'Hercules': None,
            'Hermes': None,
            'Luna': None,
            'Pantheon': None,
            'Poseidon': None,
            'Shaya': None,
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
