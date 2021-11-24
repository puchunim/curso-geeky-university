from math import log

# 11 - Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número invalido"
print('# EX 011')
# [+] COMEÇO DO CÓDIGO
n = str(input('Digite um número inteiro [Maior de 0]: '))
if int(n) <= 0:
    print(f'O número {n} é menor ou igual a zero, por isso é inválido')

else:
    soma = sum(int(i) for i in n)
    print(f'A soma de todos os algarismos de {n} é {soma}!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 12 - Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "número inválido". Se o número for positivo, calcular o logaritmo deste número
print('# EX 012')
# [+] COMEÇO DO CÓDIGO
b = int(input('Digite um número inteiro: '))
if b <= 0:
    print('Número negativo ou zero não são válidos')

else:
    print(f'O logarítimo de {b} é: {log(b, 2.71828)}!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 13 - Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média
print('# EX 013')
# [+] COMEÇO DO CÓDIGO
n1 = float(input('Digite a nota da primeira prova (peso 1): '))
n2 = float(input('Digite a nota da segunda prova (peso 2): ')) * 2
n3 = float(input('Digite a nota da terceira prova (peso 3): ')) * 2
print(f'A média ponderada dos valores digitados é: {(n1 + n2 + n3) / 5}!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 14 - A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos:
# Trabalho de laboratório => 2
# Avaliação semestral => 3
# Exame final => 5
# De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias
print('# EX 014')
# [+] COMEÇO DO CÓDIGO
n1 = float(input('Digite a nota do trabalho de laboratório: ')) * 2
n2 = float(input('Digite a nota da avaliação semestral: ')) * 3
n3 = float(input('Digite a nota do exame final: ')) * 5
media = (n1 + n2 + n3) / 10
if media > 0 and media <= 2.9:
    print(f'Desculpe, você foi reprovado (média: {media})')

elif media > 3 and media <= 4.9:
    print(f'Você passou, mas está de recuperação (média: {media})')

else:
    print(f'Você passou, parabéns! (média: {media})')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2 e assim por diante
print('# EX 015')
# [+] COMEÇO DO CÓDIGO
dia = int(input('Digite um número de 1 a 7, assim lhe direi o dia correspondente: '))
if dia == 1:
    print('1° => Domingo!')

elif dia == 2:
    print('2° => Segunda-feira!')

elif dia == 3:
    print('3° => Terça-feira!')

elif dia == 4:
    print('4° => Quarta-feira!')

elif dia == 5:
    print('5° => Quinta-feira!')

elif dia == 6:
    print('6° => Sexta-feira!')

elif dia == 7:
    print('7° => Sábado!')

else:
    print('Digita direito, otário!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 16 - Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante
print('# EX 016')
# [+] COMEÇO DO CÓDIGO
mes = int(input('Digite um número inteiro de 1 a 12, então lhe direi a qual mês corresponde: '))
if mes == 1:
    print('1° => Janeiro')

elif mes == 2:
    print('2° => Fevereiro')

elif mes == 3:
    print('3° => Março')

elif mes == 4:
    print('4° => Abril')

elif mes == 5:
    print('5° => Maio')

elif mes == 6:
    print('6° => Junho')

elif mes == 7:
    print('7° => Julho')

elif mes == 8:
    print('8° => Agosto')

elif mes == 9:
    print('9° => Setembro')

elif mes == 10:
    print('10° => Outubro')

elif mes == 11:
    print('11° => Novembro')

elif mes == 12:
    print('12° => Dezembro')

else:
    print('Digita direito, otário!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 17 - Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
# A = ((basemaior + basemenor) * altura) / 2
print('# EX 017')
# [+] COMEÇO DO CÓDIGO
base_maior = float(input('Digite o valor da base maior de um trapézio: '))
if base_maior <= 0:
    print('Valores menores ou iguais a zero não são permitidos!')

base_menor = float(input('Digite o valor da base menor de um trapézio: ')
if base_menor <= 0:
    print('Valores menores ou iguais a zero não são permitidos!')

altura = float(input('Digite a altura de um trapézio: '))
print(f'A área de um trapézio com as medidas b={base_menor}, B={base_maior} e h={altura} é: {((base_menor + base_maior) * altura) / 2}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 18 - Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas. O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, mostrando o resultando e saindo
print('# EX 018')
# [+] COMEÇO DO CÓDIGO
menu = str(input("""Calculadorinha pica
    Para usar uma das funções, basta digitar o seu símbolo:
    [+] Adição
    [-] Subtração
    [*] Multiplicação
    [/] Divisão
Sua resposta ==> """))
v1 = float(input('Digite o primeiro valor: '))
v2 = float(input('Digite o segundo valor: '))
if menu == '+':
    print(f'A soma entre {v1} e {v2} é igual a: {v1 + v2}')

elif menu == '-':
    print(f'A subtração entre {v1} e {v2} é igual a: {v1 - v2}')

elif menu == '*':
    print(f'A multiplicação de {v1} por {v2} é igual a: {v1 * v2}')

elif menu == '/':
    print(f'A divisão de {v1} por {v2} é igual a: {v1 / v2}')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 19 - Faça um programa para verificar se determinado número inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois
print('# EX 019')
# [+] COMEÇO DO CÓDIGO
n = int(input('Digite um número inteiro: '))
print(f'O número {n}..')
if n % 3 == 0:
    print('É divisível por 3!')

else:
    print('Não é divisível por 3!')

if n % 5 == 0:
    print('É divisível por 5!')

else:
    print('Não é divisível por 5!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')


# 20 - Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
# - O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# - Chama-se equilátero o triângulo que tem três lados iguais.
# - Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
print('# EX 020')
# [+] COMEÇO DO CÓDIGO
a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Desculpe, os valores digitados acima não podem formar um triângulo.')

else:
    if a == b == c:
        print(f'O triângulo com os comprimentos {a}, {b} e {c} é um triângulo equilátero!')
    
    elif a == b or a == c or b == c :
        print(f'O triângulo com os comprimentos {a}, {b} e {c} é um triângulo isóscele!')
    
    else:
        print(f'O triângulo com os comprimentos {a}, {b} e {c} é um triângulo escaleno!')
# [-] FIM DO CÓDIGO
print('===+===\n\n')
