"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e 
  aprimoram seus comportamentos;

    [Função decoradora]
    
    [Função comum]
    
    Função decoradora[
      [Função comum]
    ] => Função decorada
- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando "@" (Syntact Sugar)

OBS: DECORAR de deixar "mais bonito", não de lembrar algo;
"""

# Decorators como funções (Sintaxe não recomendada)

def seja_educado(func):
    def sendo():
        print('Foi um prazer conhecer você!')
        func()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Saudação sem aprimoramento
# saudacao()

# Saudação com aprimoramento
teste = seja_educado(saudacao) # A função saudacao foi decorada e modificada
# teste()

def raiva():
    print('EU TE ODEIO!')
 
# Raiva sem aprimoramento
# raiva()

# Raiva com aprimoramento
raiva_educada = seja_educado(raiva)
# raiva_educada()

print('\n\n==+==\n\n')

# Decorators (Sintaxe correta)

def seja_educado_mesmo(func):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        func()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo # Sintact Sugar
def apresentando():
    print('Meu nome é Pedro!')

apresentando()