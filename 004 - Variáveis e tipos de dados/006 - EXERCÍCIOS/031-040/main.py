# 31 - Leia um número inteiro e imprima o seu antecessor e o seu sucessor
print('# EX 031')
n = int(input('Digite um número inteiro: '))
print(f'O antecessor e o sucessor de {n} são, respectivamente, {n - 1} e {n + 1}')
print('===+===\n\n')


# 32 - Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro
print('# EX 032')
n = int(input('Digite um número inteiro: '))
print(f'A soma do sucessor do triplo de {n} ({(n * 3) + 1}) e o antecessor do seu dobro ({(n * 2) - 1}) é igual a {((n * 3) + 1) + ((n * 2) - 1)}')
print('===+===\n\n')


# 33 - Leia o tamanho do lado de um quadrado e imprima como resultado a sua área
print('# EX 033')
l = float(input('Digite o valor do lado de um quadradol: '))
print(f'A área de um quadrado com {l} de lado é {l**2}m²')
print('===+===\n\n')


# 34 - Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente (3.141592 * raio²)
print('# EX 034')
raio = float(input('Digite o valor do raio de um círculo: '))
print(f'A circunferência de um círculo com o raio de {raio} é: {3.141592 * (raio**2)}')
print('===+===\n\n')


# 35 - Sejam 'a' e 'b' os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = sqrt(a² + b²). Faça um programa que receba os valores de 'a' e 'b' e calcule o valor da hipotenusa através da equação
print('# EX 035')
a = float(input('Digite o valor para o "a": '))
b = float(input('Digite o valor para o "b": '))
print(f'A hipotenusa formada por a ({a}) e b ({b}), teria o valor de {(a**2 + b**2)**(1/2)}')
print('===+===\n\n')


# 36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro (V = 3.141592 * raio² * altura)
print('# EX 036')
altura = float(input('Digite a altura de um cilindro circular: '))
raio = float(input('Digite o raio de um cilindro circular: '))
print(f'Um cilindro circular de altura {altura} e raio {raio} tem {3.141592 * (raio**2) * altura} como volume')
print('===+===\n\n')


# 37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
print('# EX 037')
val = float(input('Digite o valor em R$ de um produto: '))
print(f'Com um desconto de 12% o valor do produto passaria de {val}R$ para {val - (val * (20/100))}R$')
print('===+===\n\n')


# 38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%
print('# EX 038')
sal = float(input('Digite o salário de um funcionário em R$: '))
print(f'Com um reajuste de 25%, o salário de {sal}R$ passaria a valer {sal + (sal * (25/100))}R$')
print('===+===\n\n')


# 39 - A importância de R$780.000,00 será dividida entre três ganhadores de um concurso. Sendo a quantia total:
    # O primeiro ganhador receberá 46%
    # O segundo 32%
    # O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores
premio = 780_000.00
print(rf'''No concurso X, com o prêmio valendo 780.000,00R$, as seguintes posições ganharão:
    1° Lugar - 46% do dinheiro ({premio * (46/100)}R$)
    2° Lugar - 32% do prêmio ({premio * (32/100)}R$)
    3° Lugar - O restante do prêmio ({premio * (22/100)}R$)
''')


# 40 - Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda
print('# EX 000')
dias = int(input('Sabendo que a o salário é 30R$/Dia, digite a quantidade de dias trabalhados: '))
print(f'Descontando %8 de imposto de renda, o salário obtido em {dias} dias é de: {(30 * dias) - ((30 * dias) * (8/100))}')
print('===+===')
