# 1 - Faça um programa que leia um número inteiro e o imprima
print('# EX 001')
n = int(input('Digite um número inteiro: '))
print(f'O número digitado foi: {n}!')
print('===+===\n\n')


# 2 - Faça um programa que leia um número real e o imprima
print('# EX 002')
n = float(input('Digite um número real: '))
print(f'O número digitado foi: {n}!')
print('===+===\n\n')


# 3 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles
print('# EX 003')
n1 = int(input('Digite o 1° valor inteiro: '))
n2 = int(input('Digite o 2° valor inteiro: '))
n3 = int(input('Digite o 3° valor inteiro: '))
print(f'A soma dos valores {n1}, {n2} e {n3} é igual a: {n1 + n2 + n3}!')
print('===+===\n\n')

# 4 - Leia um número real e imprima o resultado do quadrado desse número
print('# EX 004')
n = float(input('Digite um número real: '))
print(f'O qudrado de {n} é igual a: {n * n}')
print('===+===\n\n')


# 5 - Leia um número real e imprima a quinta parte deste número
print('# EX 005')
n = float(input('Digite um número real: '))
print(f'A quinta parte de {n} é igual a: {n / 5}')
print('===+===\n\n')


# 6 - Leia uma temperatura em graus Celsius e aprente-a convertida em graus Fahreinheit (F = C * (9/5)+32)
print('# EX 006')
cel = float(input('Digite uma temperatura em Celsius: '))
print(f'A temperatura {cel} em Celsius, para Fahrenheit, equivale a {cel * ((9/5) + 32)}')
print('===+===\n\n')


# 7 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius (C = 5 * (F - 32) / 9)
print('# EX 007')
fah = float(input('Digite uma temperatura em Fahrenheit: '))
print(f'A temperatura {fah} em Fahrenheit, para Celsius, equivale a {5 * (fah - 32) / 9}')
print('===+===\n\n')


# 8 - Leia uma temperatura em graus Kelvin e aprente-a convertida em graus Celsius (C = K - 273.15)
print('# EX 008')
kel = float(input('Digite uma temperatura em graus Kelvin: '))
print(f'A temperatura {kel} em Kelvin, para Celsius, equivale a {kel - 273.15}')
print('===+===\n\n')


# 9 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin (K = C + 273.15)
print('# EX 009')
cel = float(input('Digite uma temperatura em Celsius: '))
print(f'A temperatura {cel} em Celsius, para Kelvin, equivale a {cel + 273.15}')
print('===+===\n\n')


# 10 - Leia uma velocidade em km/h e aprente-a convertida em m/s (M = K/3.6)
print('# EX 010')
vel = float(input('Digite uma velocidade em km/h: '))
print(f'A velocidade de {vel}km/h, para m/s, equivale a {vel / 3.6}')
print('===+===')
