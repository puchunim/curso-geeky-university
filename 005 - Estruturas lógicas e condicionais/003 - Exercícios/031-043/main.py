# 31 - Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e mostre qual a clissificação dessa pessoa
# [Altura       ] [Peso                     ]
#                   60 | Entre 60 e 90 | +90
# Menor que 1,20 |  A  |      D        |  G
# De 1,20 a 1,70 |  B  |      E        |  H
# Maior que 1,70 |  C  |      F        |  I
print('# EX 031')
# [+] COMEÇO DO CÓDIGO
altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso: '))
if altura < 1.20:
    if peso < 60:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação A')
    
    elif peso >= 60 and peso <= 90:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação D')
    
    else:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação G')

elif altura >= 1.20 and altura <= 1.70:
    if peso < 60:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação B')
    
    elif peso >= 60 and peso <= 90:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação E')
    
    else:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação H')

else:
    if peso < 60:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação C')
    
    elif peso >= 60 and peso <= 90:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação F')

    else:
        print(f'Você tem {altura} de altura e {peso} de peso, portanto está na classificação I')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 32 - Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um pedido. O cardápio da lanchonete segue o padrão abaixo:
# [Especificação] [Código] [Preço]
# Cachorro quente   100     1.20
# Bauru Simples     101     1.30
# Bauro com Ovo     102     1.50
# Hamburguer        103     1.20
# Cheeseburguer     104     1.70
# Suco              105     2.20
# Refrigerante      106     1.00
print('# EX 032')
# [+] COMEÇO DO CÓDIGO
codigo = int(input('''>>> Digite o código do produto seguindo a tabela abaixo.

# [Especificação] [Código] [Preço]
# Cachorro quente   100     1.20
# Bauru Simples     101     1.30
# Bauro com Ovo     102     1.50
# Hamburguer        103     1.20
# Cheeseburguer     104     1.70
# Suco              105     2.20
# Refrigerante      106     1.00
===> '''))
if 100 > codigo < 106:
    print('Código errado. Verifique se o código consta na tabela.')

else:
    quantidade = int(input(f'Digite a quantidade que vai pedir do produto {codigo}: '))
    if codigo == 100:
        print(f'Você terá que pagar {1.20 * quantidade:.2f}R$ para o(s) x{quantidade} Cachorro(s) Quente(s)!')
    
    elif codigo == 101:
        print(f'Você terá que pagar {1.30 * quantidade:.2f}R$ para o(s) x{quantidade} Bauru(s) Simples!')
    
    elif codigo == 102:
        print(f'Você terá que pagar {1.50 * quantidade:.2f}R$ para o(s) x{quantidade} Bauru(s) com ovo!')

    elif codigo == 103:
        print(f'Você terá que pagar {1.20 * quantidade:.2f}R$ para o(s) x{quantidade} Hamburguer(es)!')
    
    elif codigo == 104:
        print(f'Você terá que pagar {1.70 * quantidade:.2f}R$ para o(s) x{quantidade} Cheeseburguer(es)!')

    elif codigo == 105:
        print(f'Você terá que pagar {2.20 * quantidade:.2f}R$ para o(s) x{quantidade} Suco(s)!')

    else:
        print(f'Você terá que pagar {1.00 * quantidade:.2f}R$ para o(s) x{quantidade} Refrigetante(s)!')    
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 33 - Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço novo, em seguida escreva uma mensagem em função do preço novo (de acordo com a segnda tabela)

# TABELA 1
# [Preço antigo ] [Percentual de aumento]
# até R$ 50                5%
# entre 50 e 100          10%
# acima de 100            15%

# TABELA 2
# [Preço novo    ] [Mensagem]
# até 80            Barato
# entre 80 e 120    Normal
# entre 120 e 200   Caro
# acima de 200     Muito caro
print('# EX 033')
# [+] COMEÇO DO CÓDIGO
preco = float(input('''[Digite o preço de um produto e reajustaremos pra você, seguindo a tabela abaixo]

[Preço antigo ] [Percentual de aumento]
 até R$ 50                5%
 entre 50 e 100          10%
 acima de 100            15%
==> '''))

if preco < 50:
    preco = preco + (preco * (5/100))

elif 50 >= preco <= 100:
    preco = preco + (preco * (10/100))

else:
    preco = preco + (preco * (15/100))

print(f'O reajuste ficou em {preco}R$ para o preço do produto,', end='')
if preco < 80:
    print(' e é considerado um produto BARATO')

elif 80 >= preco <= 120:
    print(' e é considerado um produto NORMAL')

elif 120 > preco <= 200:
    print(' e é considerado um produto CARO')

else:
    print(' e é considerado um produto MUITO CARO')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 34 - Leia a nota e o número de faltas de um aluno e, esreva seu conceito. De acordo com a tabela abaixo, quando o alo tem mais de 20 faltas, ocorre uma redução de conceito.

#[Nota      ] [Faltas -20] [Faltas +20]
# 9.0 a 10.0       A            B
# 7.5 a 8.9        B            C
# 5.0 a 7.4        C            D
# 4.0 a 4.9        D            E
# 0.0 a 3.9        E            E
print('# EX 034')
# [+] COMEÇO DO CÓDIGO
nota = float(input('Digite a nota do aluno: '))
faltas = int(input('Digite a quantidade de faltas: '))
if 0.0 >= nota <= 3.9:
    print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: E.')

elif 4.0 >= nota <= 4.9:
    if faltas < 20:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: D.')
    
    else:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: E.')

elif 5.0 >= nota <= 7.4:
    if faltas < 20:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: C.')

    else:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: D.')

elif 7.5 >= nota <= 8.9:
    if faltas < 20:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: B.')

    else:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: C.')  

elif 9.0 >= nota <= 10.0:
    if faltas < 20:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: A.')
    
    else:
        print(f'Com a nota {nota} e com {faltas} faltas, seu conceito é: B.')

else:
    print('Nota inválida.')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 35 - Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
print('# EX 035')
# [+] COMEÇO DO CÓDIGO
valido = True
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
if not 1 >= mes <= 12:
    print('Mês inválido!')
    valido = False


if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
    if mes == 2:
        if not 1 >= dia <= 29:
            print('Dia inválido!')
            valido = False

    else:
        if not 1 >= dia <= 31:
            print('Dia inválido!')
            valido = False

else:
    if mes == 2:
        if not 1 >= dia <= 28:
            print('Dia inválido!')
            valido = False

    else:
        if not 1 >= dia <= 31:
            print('Dia inválido!')
            valido = False          

if valido:
    print(f'A data {dia}/{mes}/{ano} é válida!')

else:
    print(f'A data {dia}/{mes}/{ano} não é válida!')
        


# [-] FIM DO CÓDIGO
print('===+===\n\n')