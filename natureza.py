class Elemento:
    def __init__(self, nome, efeito_base, aplicar_efeito_func):
        """
        Classe base para definir um elemento natural.
        :param nome: Nome do elemento.
        :param efeito_base: Descrição básica do efeito do elemento.
        :param aplicar_efeito_func: Função para aplicar o efeito.
        """
        self.nome = nome
        self.efeito_base = efeito_base
        self.aplicar_efeito = aplicar_efeito_func

    def calcular_efeito(self, atacante, alvo, acumulado=False):
        """
        Aplica o efeito básico do elemento, com bônus para acumulação.
        :param atacante: O personagem que ataca.
        :param alvo: O personagem que é atacado.
        :param acumulado: Se True, aumenta a intensidade do efeito.
        """
        dano_base = atacante.magia
        multiplicador = 1.5 if acumulado else 1.0
        dano_total = dano_base * multiplicador
        alvo.vida -= dano_total
        # Aplica o efeito do elemento no alvo
        self.aplicar_efeito(atacante, alvo, acumulado)


# Funções para aplicar os efeitos
def efeito_fogo(atacante, alvo, acumulado):
    if acumulado:
        alvo.status["queimando"] += 2  # Acúmulo de dano
    else:
        alvo.status["queimando"] = 1  # Primeiro acerto
    # Aplica dano contínuo por queimadura
    if alvo.status["queimando"] > 0:
        alvo.vida -= 10 * alvo.status["queimando"]
        alvo.status["queimando"] -= 1  # Diminui a queimadura a cada turno


def efeito_agua(atacante, alvo, acumulado):
    alvo.status["molhado"] = True
    # Se acumulado, aumenta a vulnerabilidade a fogo e eletricidade
    if acumulado:
        alvo.status["vulnerabilidade_fogo"] = True
        alvo.status["vulnerabilidade_eletricidade"] = True


def efeito_vento(atacante, alvo, acumulado):
    # Diminui a velocidade do alvo por um turno
    if acumulado:
        alvo.velocidade -= 20
    else:
        alvo.velocidade -= 10
    if alvo.velocidade < 0:
        alvo.velocidade = 0  # Impede velocidade negativa


def efeito_gelo(atacante, alvo, acumulado):
    if acumulado:
        alvo.velocidade -= 20  # Maior penalidade
    else:
        alvo.velocidade -= 10  # Penalidade normal
    if alvo.velocidade < 0:
        alvo.velocidade = 0  # Impede velocidade negativa


def efeito_terra(atacante, alvo, acumulado):
    if acumulado:
        alvo.status["atordoado"] = 2  # Atordoamento prolongado
    else:
        alvo.status["atordoado"] = 1  # Atordoamento normal


def efeito_metal(atacante, alvo, acumulado):
    # Aumenta chance de crítico do atacante
    if acumulado:
        atacante.chance_critico += 20  # Maior bônus
    else:
        atacante.chance_critico += 10  # Bônus normal


def efeito_eletricidade(atacante, alvo, acumulado):
    if acumulado:
        alvo.status["paralisado"] = 3  # Paralisia maior
    else:
        alvo.status["paralisado"] = 2  # Paralisia normal


def efeito_luz(atacante, alvo, acumulado):
    # Dano adicional contra inimigos das sombras
    if alvo.status.get("sombras", False):
        dano_extra = 15
        alvo.vida -= dano_extra  # Aumenta dano se o alvo for vulnerável à luz


def efeito_lava(atacante, alvo, acumulado):
    if acumulado:
        alvo.status["queimando"] = 3  # Queimadura mais forte
    else:
        alvo.status["queimando"] = 2  # Queimadura normal
    # Aplica dano contínuo por lava
    if alvo.status["queimando"] > 0:
        alvo.vida -= 15 * alvo.status["queimando"]
        alvo.status["queimando"] -= 1  # Diminui a queimadura a cada turno


def efeito_sombras(atacante, alvo, acumulado):
    # Diminui a precisão e resistência mágica do alvo
    if acumulado:
        alvo.precisao -= 20
        alvo.resistencia_magica -= 20
    else:
        alvo.precisao -= 10
        alvo.resistencia_magica -= 10
    if alvo.precisao < 0:
        alvo.precisao = 0  # Impede precisão negativa
    if alvo.resistencia_magica < 0:
        alvo.resistencia_magica = 0  # Impede resistência negativa


def efeito_madeira(atacante, alvo, acumulado):
    alvo.status["enraizado"] = True
    # Impede o movimento do alvo por 1 turno
    alvo.velocidade = 0  # O alvo não pode se mover


def efeito_veneno(atacante, alvo, acumulado):
    if acumulado:
        alvo.status["envenenado"] = 3  # Envenenamento maior
    else:
        alvo.status["envenenado"] = 2  # Envenenamento normal
    # Aplica dano contínuo por veneno
    if alvo.status["envenenado"] > 0:
        alvo.vida -= 5 * alvo.status["envenenado"]
        alvo.status["envenenado"] -= 1  # Diminui a toxicidade a cada turno


def efeito_vapor(atacante, alvo, acumulado):
    alvo.status["visibilidade_reduzida"] = True
    # Reduz a precisão do alvo devido ao vapor
    alvo.precisao -= 10
    if alvo.precisao < 0:
        alvo.precisao = 0  # Impede precisão negativa


def efeito_areia(atacante, alvo, acumulado):
    alvo.status["cego"] = True
    # Reduz drasticamente a precisão do alvo
    alvo.precisao = 0
    if alvo.precisao < 0:
        alvo.precisao = 0  # Impede precisão negativa


# Definição dos elementos com as funções de efeitos
FOGO = Elemento("Fogo", "Causa queimaduras progressivas.", efeito_fogo)
AGUA = Elemento("Água", "Deixa o alvo molhado, reduzindo resistência ao calor e eletricidade.", efeito_agua)
VENTO = Elemento("Vento", "Empurra o alvo, podendo interromper ações.", efeito_vento)
GELO = Elemento("Gelo", "Ralentiza o alvo, reduzindo velocidade.", efeito_gelo)
TERRA = Elemento("Terra", "Reduz a mobilidade e pode causar atordoamento.", efeito_terra)
METAL = Elemento("Metal", "Aumenta a chance de dano crítico em ataques físicos.", efeito_metal)
ELETRICIDADE = Elemento("Eletricidade", "Paralisa o alvo temporariamente.", efeito_eletricidade)
LUZ = Elemento("Luz", "Causa dano adicional contra criaturas das sombras.", efeito_luz)
LAVA = Elemento("Lava", "Combina calor e impacto, causando dano contínuo.", efeito_lava)
SOMBRAS = Elemento("Sombras", "Reduz a precisão e resistência mágica do alvo.", efeito_sombras)
MADEIRA = Elemento("Madeira", "Enraíza o alvo, impedindo movimentação.", efeito_madeira)
VENENO = Elemento("Veneno", "Causa dano contínuo e reduz atributos.", efeito_veneno)
VAPOR = Elemento("Vapor", "Reduz a visibilidade e aumenta a vulnerabilidade ao calor.", efeito_vapor)
AREIA = Elemento("Areia", "Causa cegueira temporária, reduzindo a precisão do alvo.", efeito_areia)


# Exemplo de aplicação de efeitos
def aplicar_efeito_atual(atacante, alvo, elemento, acumulado=False):
    """
    Função para aplicar o efeito atual de um elemento.
    :param atacante: O personagem que ataca.
    :param alvo: O personagem que é atacado.
    :param elemento: O elemento a ser aplicado (ex: Fogo, Água).
    :param acumulado: Se True, aumenta a intensidade do efeito.
    """
    elemento.calcular_efeito(atacante, alvo, acumulado)


# Exemplos de chamada (substitua com seus objetos de personagem)
# Aplicando um ataque de Fogo e acumulando o efeito de queimar
# Aplicando o efeito diretamente
# aplicar_efeito_atual(atacante, alvo, FOGO, acumulado=True)
