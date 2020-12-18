# 41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado
print('# EX 041')
valh = float(input('Digite o valor da hora trabalhada: '))
hs = float(input('Digite a quantidade de horas trabalhadas: '))
print(f'Trabalhando {hs} horas no mês inteiro, cada hora valendo {valh}R$, o salário final mais o reajuste de 10% é {(valh * hs) + ((valh * hs) * (10/100))}R$')
print('===+===\n\n')


# 42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base
print('# EX 042')
base = float(input('Digite o salário base de um funcionário: '))
print(f'O salário a receber no final do mês, com a gratificação de 5% e 7% de imposto, seria de {base - (base * (2/100))}R$')
print('===+===\n\n')


# 43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
    # O total a pagar com desconto de 10%
    # o valor de cada parcela, no parcelamento de 3x sem juros
    # a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
    # a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
print('# EX 043')
valor = float(input('Digite um valor em R$: '))
print(f'''Valor total: {valor}R$
    Com desconto de 10% => {valor - (valor * (10/100))}R$
    Valor de cada parcela, parcelado em 3x sem juros => {valor / 3}R$
    Comissão do vendedor para compra a vista (5% sobre valor com desconto) => {(valor - (valor * (10/100))) * (5/100)}R$
    Comissão do vendedor para compra parcelada (5% sobre valor) => {valor * (5/100)}R$
''')
print('===+===\n\n')


# 44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo
print('# EX 044')
deg = float(input('Digite a altura de cada degrau da escada: '))
max_alt = float(input('Digite a altura onde você quer chegar: '))
print(f'Para chegar até o topo da escada, você precisaria subir {round (max_alt / deg)} degrau(s)') # usei round só pq sim
print('===+===\n\n')


# 45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema
print('# EX 045')
letra = str(input('Digite uma letra: '))
print(f'A letra {letra} ficaria {letra.upper()} maiúscula')
print('===+===\n\n')


# 46 - Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999). Gere outro número formado pelos dígios invertidos do número lido
print('# EX 046')
numero = str(input('Digite um número de 100 a 999: '))
print(f'O número formado do inverso do anterior é: {numero[::-1]}')
print('===+===\n\n')


# 47 - Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 digito por linha
print('# EX 047')
numero = str(input('Digite um número inteiro de 1000 a 9999: '))
print(f'''1° Dígito: {numero[0]}
2° Dígito: {numero[1]}
3° Dígito: {numero[2]}
4° Dígito: {numero[3]}''')
print('===+===\n\n')


# 48 - Leia um valor inteiro em segundos e imprima-o em horas, minutos e segundos
print('# EX 048')
seg = float(input('Digite uma quantidade de segundos: '))
print(f'{seg}s, convertidos para horas e minutos, seriam, respectivamente: {seg / 3600} e {seg / 60}')
print('===+===\n\n')


# 49 - Faça um programa que leia o horário (hora, minuto e segundo) de inicio e duração em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do término da mesma
print('# EX 049')
ini = float(input('Digite quantos segundos vai começar o experimento: '))
dur = float(input('Digite quando vai acabar o experimento: '))
print(f'O exercício durou, respectivamente em horas e minutos, {(ini+dur) / 3600}h ou {(ini+dur) / 60}m')
print('===+===\n\n')


# 50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual
print('# EX 050')
idade = int(input('Digite sua idade atual: '))
print(f'Você nasceu em {2020 - idade}')
print('===+===\n\n')


# 51 - Escreva um programa que leia as coordenadas 'x' e 'y' de pontos no R² e calcule sua origem (0,0)
print('# EX 051')
x1 = 0.0
y1 = 0.0
 
x2 = float(input('Informe a coordenada X: '))
y2 = float(input('Informe a coordenada y: '))
 
r = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
 
print(f'A distância é {r}')
print('===+===\n\n')


# 52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, valor do prêmio e imprima quanto cada ganharia do prêmio com base no valor investido
print('# EX 052')
am1 = float(input('Digite o valor que o 1° amigo apostou: '))
am2 = float(input('Digite o valor que o 2° amigo apostou: '))
am3 = float(input('Digite o valor que o 3° amigo apostou: '))
total = float(input('Digite o valor total do prêmio: '))
print(f'''O 1° amigo irá ganhar: {am1 + (total / 3)}
O 2° amigo irá ganhar: {am2 + (total / 3)} 
O 3° amigo irá ganhar: {am3 + (total / 3)}''')
print('===+===\n\n')


# 53 - Faça um programa para ler as dimensões de um terreno (comprimento e largura), bem como o preço do metro de tela. Imprima o custo para cercar este mesmo terreno com a tela
print('# EX 053')
comp = float(input('Digite o comprimento do terreno: '))
larg = float(input('Digite a largura do terreno: '))
preco_tela = float(input('Digite o preço de cada metro de tela: '))
print(f'Serão precisos {comp * larg}m² de tela para circundar o terreno, o que custaria {(comp * larg) * preco_tela}R$')
print('===+===\n\n')
