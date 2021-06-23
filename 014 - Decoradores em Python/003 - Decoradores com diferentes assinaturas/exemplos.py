"""
Decorators com diferentes assinaturas

Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e
parâmetros de entrada
"""

# Decorator Pattern

def gritar(f):
    def aumentar(*args, **kwargs):
        return f(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return(f'Olá, eu sou o/a {nome}')

print(saudacao('Pedro'))

@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} com {acompanhamento}'

# print(ordenar('bife', 'batatas'))

# Nomeando parâmetros

# print(ordenar(principal='bife', acompanhamento='batatas'))

print(ordenar.__name__) # O nome vai ser o nome da função retornada pelo decorador
