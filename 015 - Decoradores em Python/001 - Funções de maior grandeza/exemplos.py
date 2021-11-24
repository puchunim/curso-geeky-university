"""
Funções de maior grandeza - Higher Order Functions - HOF

O que significa?

- Quando uma linguagem de programação suporta HOF, indica que
podemos ter funções que retornam outras funções, passar funções 
para argumentos de outras funções e criar variáveis do tipo de
funções nos programas.

OBS: Na seção de funções, foi usado HOF

Em Python, as funções são Cidadãos de Primeira Classe (First Class Citizen)
"""

# Exemplo - Definindo funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, func):
    return func(num1, num2)

# Testando funções (passando elas como parâmetros)
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

print('\n\n==+==\n\n')

"""
Nested Functions - Funções aninhadas

Em Python, também podemos ter funções dentro de funções, que são
conhecidas por Nested Functions ou Inner Functions.
"""

# Exemplo de Nested Function

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('Fala aí fi, ', 'Bom dia só se for pra tu mesmo, '))

    return humor() + pessoa

print(cumprimento('Pedro'))

print('\n\n==+==\n\n')

# Retornando funções de outras funções

def me_faz_rir():
    def rir():
        return choice(('kkkkkkkkkk', 'ksigjwkgjwelkjghw', 'ksksksksk'))

    return rir

rir = me_faz_rir()
print(rir())
