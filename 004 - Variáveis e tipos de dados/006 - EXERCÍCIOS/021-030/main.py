# 21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas (K = L * 0.45)
print('# EX 021')
lib = float(input('Digite um valor em libras: '))
print(f'{lib} libras equivalem a {lib * 0.45}kg')
print('===+===\n\n')


# 22 - Leia um valor de comprimento em jardas e apresente-o convertido em metros (M = 0.91 * J)
print('# EX 022')
jar = float(input('Digite um comprimento em jardas: '))
print(f'{jar} jardas equivalem a {0.91 * jar} metros')
print('===+===\n\n')


# 23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas (J = M/0.91)
print('# EX 023')
me = float(input('Digite um comprimento em metros: '))
print(f'{me}m equivalem a {me / 0.91} jardas')
print('===+===\n\n')


# 24 - Leia um valor de área em metros quadrados e aprente-o convertido em acres (A = M * 0.000247)
print('# EX 024')
m2 = float(input('Digite uma área em metros quadrados: '))
print(f'{m2}m² equivalem a {m2 * 0.000247} acres')
print('===+===\n\n')


# 25 - Leia um valor de área em acres e apresente-o convertido em metros quadrados (M = A * 4048.58)
print('# EX 025')
ac = float(input('Digite uma área em acres: '))
print(f'{ac} acres equivalem a {ac * 4048.58}m²')
print('===+===\n\n')


# 26 - Leia um valor de área em metros quadrados e apresente-o convertido em hectares (H = M * 0.0001)
print('# EX 026')
m2 = float(input('Digite uma área em m²: '))
print(f'{m2}m² equivalem a {m2 * 0.0001}')
print('===+===\n\n')

# 27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados (M = H * 10000)
print('# EX 027')
hec = float(input('Digite uma área em hectares: '))
print(f'{hec} hectares equivalem a {hec * 10_000}m²')
print('===+===\n\n')


# 28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos
print('# EX 028')
val1 = float(input('Digite o 1° valor: '))
val2 = float(input('Digite o 2° valor: '))
val3 = float(input('Digite o 3° valor: '))
print(f'O quadrado de {val1} ({val1 * val1}), de {val2} ({val2 * val2}) e de {val3} ({val3 * val3}), somados, resultam no número {(val1 * val1) + (val2 * val2) + (val3 * val3)}')
print('===+===\n\n')


# 29 - Leia quatro notas, calcule a média aritmética e imprima o resultado
print('# EX 000')
n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))
n3 = float(input('Digite a 3° nota: '))
n4 = float(input('Digite a 4° nota: '))
print(f'A média aritmética dos números {n1}, {n2}, {n3} e {n4} resultam no número: {(n1 + n2 + n3 + n4) / 4}')
print('===+===\n\n')


# 30 - Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares
print('# EX 030')
real = float(input('Digite um valor em R$ (SOMENTE OS NÚMEROS): '))
cotacao = float(input('Digite o valor atual da cotação do dolar: '))
print(f'{real}R$ => {real / cotacao}U$')
print('===+===')
