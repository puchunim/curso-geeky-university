def ex001():
    """
    Faça um programa que determine e mostre
    os cinco primeiros múltiplos de 3, con-
    siderando números maiores que 0.
    """

    print('Primeiros 5 múltiplos de 3:')
    for n in range(1, 6):
        print(f'3 x {n} = {3 * n}')

def ex002():
    """
    Escreva um programa que escreva na tela,
    de 1 até 100, de 1 em 1, 3 vezes. A primeira
    vez deve usar a estrutura de repetição for,
    a segunda while, e a terceira while infinito. 
    """

    print('1 a 100 com for:')
    for n in range(1, 101):
        print(n)
    print('\n\n')

    print('1 a 100 com while finito')
    n = 1
    while n <= 100:
        print(n)
        n += 1
    print('\n\n')
    
    print('1 a 100 com while infinito')
    n = 1
    while True:
        print(n)
        if n == 100:
            break
        n += 1

def ex003():
    """
    Faça um algoritmo utilizando o comando while
    que mostra a contagem regressiva na tela, ini-
    ciando em 10 e terminando em 0. Mostrar a mensagem:
    "FIM!" após a contagem.
    """

    print('Contagem regressiva!')
    cont = 10
    while cont >= 0:
        print(f'{cont}!')
        cont -= 1
    print('FIM!')

def ex004():
    """
    Escreva um programa que declare um inteiro,
    inicialize-o com 0, e incremente-o de 1000 em 100,
    imprimindo seu valor na tela, até que seu valor seja
    100_000 (cem mil)
    """

    print('Indo de 0 a 100_000, de 1000 em 1000:')
    for n in range(0, 100_001, 1000):
        print(n)

def ex005():
    """
    Faça um programa que peça ao usuário
    para digitar 10 valores e some-os.
    """

    val = 0
    for v in range(0, 10):
        val += int(input(f'Digite o {v+1}° número: '))
    
    print(f'A soma total dos 10 valores é: {val}')

def ex006():
    """
    Faça um programa que leia 10 inteiros e imprima
    sua média.
    """

    val = 0
    for v in range(0, 10):
        val += int(input(f'Digite o {v+1}° valor: '))
    print(f'A média entre os 10 números é: {val / 10}')

def ex007():
    """
    Faça um programa que leia 10 inteiros positivos,
    ignorando não positivos, e imprima sua média.
    """

    val = 0
    for v in range(0, 10):
        while True:
            tmp = int(input(f'Digite o {v+1}° número positivo: '))
            if tmp > 0:
                val += tmp
                break
    
    print(f'A média da soma dos 10 números é: {val / 10}')

def ex008():
    """
    Escreva um programa que leia 10 números
    e escreva o menor valor lido e maior valor lido
    """

    maior = 0
    for v in range(0, 5):
        tmp = int(input(f'Digite o {v+1}° número: '))
        if v == 0:
            menor = tmp
            maior = tmp

        else:
            if tmp < menor:
                menor = tmp

            if tmp > maior:
                maior = tmp

    print(f'O maior número é {maior} e o menor é {menor}!') 

def ex009(): # pulado pq nume tnendi
    """
    Faça um programa que leia um número
    inteiro N e depois imprima os N primeiros
    números naturais ímpares
    """
    pass

def ex010():
    """
    Faça um programa que calcule
    e mostre a soma dos 50 primeiros números pares
    """

    val = 0
    for n in range(0, 52, 2):
        val += n
    print(f'A soma dos primeiros 50 números pares é: {val}')
