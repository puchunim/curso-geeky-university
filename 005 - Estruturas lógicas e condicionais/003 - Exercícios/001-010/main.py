# 1 - Faça um programa que receba dois números e mostre qual deles é o maior
print('# EX 001')
# [+] COMEÇO DO CÓDIGO
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O primeiro número é maior!')

else:
    print('O segundo número é maior!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido
print('# EX 002')
# [+] COMEÇO DO CÓDIGO
n = float(input('Digite um número: '))
if n % 2 == 0:
    print(f'A raíz quadrada de {n:.2f} é {n**(1/2):.2f}')

else:
    print(f'Número inválido: {n:.2f} é um número ímpar, portanto não pode ser operado')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 3 - Leia um número real. Se o número for positivo, imprima a raiz quadrada. Do contrário, imprima o número ao quadrado
print('# EX 003')
# [+] COMEÇO DO CÓDIGO
n = float(input('Digite um número real: '))
if n % 2 == 0:
    print(f'A raiz quadrada de {n:.2f} é {n**(1/2):.2f}')

else:
    print(f'O quadrado de {n:.2f} é {n**2:.2f}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 4 - Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
print('# EX 004')
# [+] COMEÇO DO CÓDIGO
n = float(input('Digite um número: '))
if n % 2 == 0:
    print(f'{n:.2f}² => {n**2:.2f}²')
    print(f'²√{n:.2f} => {n**(1/2):.2f}')

else:
    print(f'Operação inválida: {n:.2f} é ímpar, por isso será desconsiderado..')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 5 - Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar
print('# EX 005')
# [+] COMEÇO DO CÓDIGO
n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print(f'{n} é um número PAR!')

else:
    print(f'{n} é um número IMPAR!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 6 - Escreva um programa que, dado dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos
print('# EX 006')
# [+] COMEÇO DO CÓDIGO
n1 = int(input('Digite o 1° número inteiro: '))
n2 = int(input('Digite o 2° número inteiro: '))
maior = n1
menor = n2

if n2 > n1:
    maior = n2
    menor = n1

print(f'Entre os números {n1} e {n2}, o maior número é {maior}, assim sendo, a diferença dos dois é de {maior - menor}!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 7 - Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "números iguais"
print('# EX 007')
# [+] COMEÇO DO CÓDIGO
n1 = int(input('Digite o 1° número inteiro: '))
n2 = int(input('Digite o 2° número inteiro: '))
if n1 > n2:
    print(f'O maior número digitado foi: {n1}!')

elif n1 == n2:
    print(f'Os dois números são iguais!')

else:
    print(f'O maior número digitado foi: {n2}!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina
print('# EX 008')
# [+] COMEÇO DO CÓDIGO
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
if n1 < 0.0 or n1 > 10.0:
    print(f'O número {n1} não atende aos requisitos de nota. Desligando...')

elif n2 < 0.0 or n2 > 10.0:
    print(f'O número {n2} não atende aos requisitos de nota. Desligando...')

else:
    print(f'A média entre os números {n1} e {n2} é {(n1 + n2) / 2}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 9 - Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário, imprima: "Empréstimo não concedido", caso contrário, imprima: "Empréstimo concedido"
print('# EX 009')
# [+] COMEÇO DO CÓDIGO
salario = float(input('Digite o valor do salário: '))
prest = float(input('Digite o valor de uma prestação do empréstimo: '))
if prest > (salario * (20/100)):
    print('EMPRÉSTIMO NEGADO: a prestação é maior do que 20% do salário!')

else:
    print('EMPRÉSTIMO CONCEDIDO: a prestação é menor do que 20% do salário!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 10 - Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h = altura):
# - Homens: (72.7 * h) - 58
# - Mulheres (62, 1 * h) - 44,7
print('# EX 010')
# [+] COMEÇO DO CÓDIGO
sexo = str(input('Digite seu sexo [M/F]: '))
altura = float(input('Digite sua altura: '))
if sexo == 'M':
    print(f'O seu peso ideal é de: {(72.7 * altura) - 58}kg')

elif sexo == 'F':
    print(f'O seu peso ideal é de: {(62.1 * altura) - 44.7}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')