class Defesa:
    """
    Classe para gerenciar os ataques de cada personagem.
    """

    @staticmethod
    def cria_defesas(nome_personagem):
        """
        Retorna uma lista de ataques com base no nome do personagem.
        Atualmente, os ataques estão como 'None' para preenchimento posterior.
        """
        ataques_por_personagem = {
            'Afrodite': None,
            'Alos': None,
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
            'Zeus': None
        }

        return ataques_por_personagem.get(nome_personagem, None)
