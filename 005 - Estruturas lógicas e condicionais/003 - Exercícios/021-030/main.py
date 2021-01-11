from statistics import harmonic_mean
from random import randint

# 21 - Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida
print('# EX 021')
# [+] COMEÇO DO CÓDIGO
menu = int(input("""Escolha a opção:
[1] Somar 2 números
[2] Diferença entre 2 números (maior pelo menor)
[3] Produto entre 2 números
[4] Divisão entre 2 números (o denominador não pode ser zero)

SUA RESPOSTA ==> """))
print('==>x<==')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if menu == 1:
    print(f'A soma entre {n1} e {n2} é: {n1 + n2}!')

elif menu == 2:
    if n1 > n2:
        print(f'A diferença entre os números {n1} e {n2} é: {n1 - n2}')
    
    else:
        print(f'A diferença entre os números {n2} e {n1} é: {n2 - n1}')

elif menu == 3:
    print(f'O produto entre {n1} e {n2} é: {n1 * n2}')

elif menu == 4:
    if n2 == 0:
        print('O numerador não pode ser zero!')
    
    else:
        print(f'O quociente entre {n1} e {n2} é: {n1 / n2}!')

# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 22 - Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são:
# - Ter pelo menos 65 anos,
# - Ou ter trabalhado pelo menos 30 anos,
# - Ou ter pelo menos 60 anos e trabalhando pelo menos 25.
print('# EX 022')
# [+] COMEÇO DO CÓDIGO
idade = int(input('Digite a sua idade: '))
tempo = float(input('Digite o seu tempo de contribuição com trabalho: '))
if idade >= 60 and tempo >= 25:
    print('Parabéns, você já pode se aposentar')

elif idade >= 65:
    print('Parabéns, você já pode se aposentar')

elif tempo >= 30:
    print('Parabéns, você já pode se aposentar')

else:
    print('Você não pode se aposentar')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 23 - Determine se um determinado ano lido é bissexto. Sendo que um ano é bissexto se for divísvel por 400 ou se for divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996
print('# EX 023')
# [+] COMEÇO DO CÓDIGO
ano = int(input('Digite um ano: '))
if ano % 400 == 0:
    print(f'{ano} é um ano bissexto!')

elif ano % 4 == 0 and ano % 100 != 0:
    print(f'{ano} é um ano bissexto!')

else:
    print(f'{ano} não é um ano bissexto!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 24 - Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%, SP 12%, RJ 15%, MS 8%). Faça um programa em que o usuário entre com o valor e o estado destino do produto e o programa retorn o preço final do produto acrescido do imposto do estado em que ele será vendido. Se o estado não for válido, mostrar uma mensagem de erro
print('# EX 024')
# [+] COMEÇO DO CÓDIGO
sigla = str(input('Para começar, digite a sigla do estado que quer calcular.\n\nAs siglas disponíveis são:\n- MG => 7% de imposto\n- SP => 12% de imposto\n- RJ => 15% de imposto\n- MS => 8% de imposto\n\nSua resosta ==> ')).upper()
preco = float(input('Digite o preço que será convertido: '))

if sigla == 'MG':
    print(f'O reajuste do valor será: {(preco * (7/100))}')

elif sigla == 'SP':
    print(f'O reajuste do valor será: {(preco * (12/100))}')

elif sigla == 'RJ':
    print(f'O reajuste do valor será: {(preco * (15/100))}')

elif sigla == 'MS':
    print(f'O reajuste do valor será: {(preco * (8/100))}')

else:
    print('Sigla inválida!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# \/\/\/ PULADO \/\/\/
# 25 - Calcule as raízes da equação de 2° grau, lembrando que:

# x = -b +- sqrt(delta), onde
# delta = b² - 4ac

# A variável 'a' tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".

# - Se delta < 0, não existe real. Imprima a mensagem: Não existe raiz.
# - Se delta = 0, existe uma raiz real. Imprima a raiz e a mensagem: Raiz única
# - Se delta > 0, existem duas raizes reais. Imprima as duas raizes.
print('# EX 025')
# [+] COMEÇO DO CÓDIGO
a = float(input('Digite o valor da variável "a": '))
if a == 0:
    print('Desculpe, "a" não pode ser igual a zero, isso não é uma equação de segundo grau!')
b = float(input('Digite o valor da variável "b": '))
c = float(input('Digite o valor da variável "c": '))
delta = b**2 + (4*a*c)
if delta < 0:
    print('Não existe raíz')

elif delta == 0:
    print('Existe uma raíz, e ela é: vsfd')

else:
    raiz_delta = delta**(1/5)
    b_negativo = -b
    dxa = 2 * a 
    raiz_positiva = (b_negativo + raiz_delta) / dxa
    raiz_negativa = (b_negativo - raiz_delta) / dxa
    print(f'RP => {raiz_positiva}, RN => {raiz_negativa}')

# [-] FIM DO CÓDIGO
print('===+===\n\n')
# /\/\/\ PULADO /\/\/\


# 26 - Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma mensagem de acordo com a tabela abaixo:
# [CONSUMO   |KM/L|         MENSAGEM]
# menor que |  8     | VENDA O CARRO!
# entre     | 8 e 14 |     ECONÔMICO!
# maior que|   14   |SUPER ECONOMICO!

print('# EX 026')
# [+] COMEÇO DO CÓDIGO
dist = float(input('Digite a distância percorrida em Km: '))
lit = float(input('Digite a litragem gasta: '))
kml = dist/lit
if kml < 8:
    print('Venda o carro!')

elif kml >= 8 and kml <= 14:
    print('Econômico!')

else:
    print('Super econômico!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 27 - Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
# Categoria ||| Idade
# Infantil A - 5 a 7
# Infantil B - 8 a 10
# Juvenil A - 11 a 13
# Juvenil B - 14 a 17
# Sênior - maiores de 18
print('# EX 027')
# [+] COMEÇO DO CÓDIGO
idade = int(input('Digite a idade de um nadador: '))
if idade < 5:
    print('O nadador não tem idade o suficiente!')

elif idade >= 5 and idade <= 7:
    print('O nadador está no Infantil A!')

elif idade >=8 and idade <= 10:
    print('O nadador está no Infantil B!')

elif idade >= 11 and idade <= 13:
    print('O nadador está no Juvenil A!')

elif idade >= 14 and idade <= 17:
    print('O nadador está no Juvenil B!')

else:
    print('O nadador está no sênior!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 28 - Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de acordo com um valor numérico digitado pelo usuário:
# (a) Geométrica => (F = cubic_rt(x * y * z))
# (b) Ponderada => (F = (x + y*2 + z*3) / 6) 
# (c) Harmônica => (F = 1/(1/x + 1/y + 1/z))
# (d) Aritmética => (F = x+y+z/3)
print('# EX 028')
# [+] COMEÇO DO CÓDIGO
n1 = int(input('Digite o primeiro número inteiro positivo: '))
n2 = int(input('Digite o segundo número inteiro positivo: '))
n3 = int(input('Digite o terceiro número inteiro positivo: '))
if n1 < 0 or n2 < 0 or n3 < 0:
    print('Um dos números digitados é negativo, encerrando o programa..')

else:
    menu = int(input("""[Menu de médias]
    Digite abaixo a média que quer calcular:
        [1] Aritmética,
        [2] Ponderada,
        [3] Geométrica,
        [4] Harmônica.
Sua resposta  ==> """))
    if menu == 1:
        print(f'A média aritmética dos valores é: {(n1 + n2 + n3) / 3}')
    
    elif menu == 2:
        print(f'A média ponderada dos valores é: {(n1 + (n2 * 2) + (n3 * 3)) / 6}')
    
    elif menu == 3:
        print(f'A média geométrica dos valores é: {(n1 * n2 * n3)**(1./3)}')
    
    elif menu == 4:
        print(f'A média harmônica dos valores é: {harmonic_mean([n1, n2, n3])}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 29 - Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100. Escolha números aleatórios entre 1 e 100 e, mostre na tela a pergunta: Qual é a soma de a + b, onde a e b são os números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno e, mostre pra ele as perguntas e as respostas corretas, além de quantas vezes o aluno acertou.
print('# EX 029')
# [+] COMEÇO DO CÓDIGO
acertos = 0
print('===[Provinha de matemática')
print('>>> Olá amiguinhos! Ansiosos para a prova? Vão ser 5 perguntinhas de adição com numeros de 1 a 100 e no final vamos ver quantas vocês acertaram! Muito bem, vamos nessa!\n\n')
# PERGUNTA 1
p1v1 = randint(1, 100)
p1v2 = randint(1, 100)
p1s = p1v1 + p1v2
p1r = int(input(f'P1) Qual é a soma de {p1v1} + {p1v2}? => '))
if p1r == p1s:
    acertos += 1
# </1>

# PERGUNTA 2
p2v1 = randint(1, 100)
p2v2 = randint(1, 100)
p2s = p2v1 + p2v2
p2r = int(input(f'P2) Qual é a soma de {p2v1} + {p2v2}? => '))
if p2r == p2s:
    acertos +=1
# </2>

# PERGUNTA 3
p3v1 = randint(1, 100)
p3v2 = randint(1, 100)
p3s = p3v1 + p3v2
p3r = int(input(f'P3) Qual é a soma de {p3v1} + {p3v2}? => '))
if p3r == p3s:
    acertos +=1
# </3>

# PERGUNTA 4
p4v1 = randint(1, 100)
p4v2 = randint(1, 100)
p4s = p2v1 + p2v2
p4r = int(input(f'P4) Qual é a soma de {p4v1} + {p4v2}? => '))
if p4r == p4s:
    acertos +=1
# </4>

# PERGUNTA 5
p5v1 = randint(1, 100)
p5v2 = randint(1, 100)
p5s = p5v1 + p5v2
p5r = int(input(f'P5) Qual é a soma de {p5v1} + {p5v2}? => '))
if p5r == p5s:
    acertos +=1
# </5>
print('\n\nMuito bem! Agora vamos ver se você acertou!\n')
print(f'''Coluna 1 => Sua resposta
Coluna 2 => Resposta correta

[RESPOSTAS]
P1) {p1r} || {p1s}
P2) {p2r} || {p2s}
P3) {p3r} || {p3s}
P4) {p4r} || {p4s}
P5) {p5r} || {p5s}

Você acertou {acertos} perguntas!''')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 30 - Faça um programa que receba três números e mostre-os em ordem crescente
print('# EX 030')
# [+] COMEÇO DO CÓDIGO
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
arrumadinho = sorted((n1, n2, n3))
print(f'Os números digitados, em ordem crescente, são: {arrumadinho}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')