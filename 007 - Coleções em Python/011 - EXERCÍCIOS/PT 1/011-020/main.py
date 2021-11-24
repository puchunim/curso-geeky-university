def ex011():
    """
    Faça um programa que preencha um vetor com 10 números
    reais, calcule e mostre a quantidade de números negativos
    e a soma dos números positivos deste vetor.
    """

    vet = []
    pos = []
    neg = []
    for n in range(0, 10):
        vet.append(
            float(input(f'Digite o {n+1}° valor real: '))
        )
    for n in vet:
        if n < 0:
            neg.append(n)
        
        else:
            pos.append(n)

    print(f'Foram encontrados {len(neg)} números negativos no vetor e, a soma de todos os positivos é {sum(pos)}!')

def ex012():
    """
    Fazer um programa para ler 5 valores e, em seguida, mostrar
    todos os valores lidos juntamente com o maior, o menor e
    a média dos valores.
    """

    vet = []
    for n in range(0, 5):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    print(f'Os valores lidos foram {vet}, o maior número presente é {max(vet)} e a média dos valores é {sum(vet) / len(vet)}')

def ex013():
    """
    Fazer um programa para ler 5 valores e, em seguida
    mostrar a posição onde se encontram o maior e o
    menor valor.
    """

    vet = []
    for n in range(0, 5):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    print(f'{max(vet)} é o maior número e ele aparece primeiro na posição {vet.index(max(vet))}')
    print(f'{min(vet)} é o menor número e ele aparece primeiro na posição {vet.index(min(vet))}')

def ex014():
    """
    Faça um programa que leia um vetor de 10 posições
    e verifique se existem valores iguais e os escreva
    na tela.
    """

    vet = []
    dup = []
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    print(str(vet) + '\n\n')
    screen = ''
    for n in vet:
        if vet.count(n) > 1 and n not in dup:
            dup.append(n)
            screen += f'{n} se repete {vet.count(n)} vezes!\n'
    
    if screen == '':
        print('Não houveram repetições')
    
    else:
        print(screen)

def ex015():
    """
    Leia um vetor com 20 números inteiros. Escreva os elementos
    eliminando elementos repetidos.
    """

    vet = []
    for n in range(0, 20):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    print('Valor com repetições: ' + str(vet))
    print('Valor com repetições: ' + str(list(set(vet))))

def ex016():
    """
    Faça um programa que leia um vetor de 5 posições para
    números reais e, depois, um código inteiro. Se o código
    for zero, finalize o programa; se for 1, mostre o vetor
    na ordem certa; se for 2, mostre na inversa. Caso o código
    for diferente de 0, 1 ou 2, escreva um amensagem informando
    que o código é inválido.
    """

    vet = []
    for n in range(5):
        vet.append(
            float(input(f'Digite o {n+1}° valor real: '))
        )
    print('\n\n')
    while True:
        cod = int(
            input(
                """Digite um dos códigos abaixo, para:
    [0] Sair do programa
    [1] Mostrar vetor na ordem crescente
    [2] Mostrar o vetor ao contrário
    ====> """
            )
        )
        if cod >= 0 and cod <= 2:
            break
    
    if cod == 0:
        print('Bye, bye!')
    
    elif cod == 1:
        vet.sort()
        print(f'Vetor organizado => {vet}')
    
    else:
        print(F'Vetor ao contrário => {vet[::-1]}')

def ex017():
    """
    Leia um vetor de 10 posições e atribua valor 0
    para todos os elementos que possuírem valores
    negativos.
    """

    vet = []
    for n in range(10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    for v in vet:
        if v < 0:
            vet[vet.index(v)] = 0
    
    print(f'O vetor, colocando 0 no lugar dos números negativos, ficará: {vet}')

def ex018(): # pulado
    """
    Faça um programa que leia um vetor de 10 números.
    Leia um número X. Conte os múltiplos de um número
    inteiro X num vetor e mostre-os na tela.
    """

    pass

def ex019():
    """
    Faça um vetor de tamanho 50 preenchido com o seguinte valor:
    (i+5*i)%(i+1), sendo i a posição do elemento no vetor. Em seguida,
    imprima o vetor na tela.
    """

    vet = list(range(0, 50))
    print(vet)
    for n in range(0, 50):
        vet[n] = (n+5*n)%(n+1)
    print(vet)

def ex020():
    """
    Escreva um programa que leia números inteiros no
    intervalo [0, 50] e os armazene em um vetor de
    10 posições. Preencha um segundo vetor apenas com
    os números impares do primeiro vetor. Imprima os
    vetores, 2 elementos por linha.
    """

    vet = []
    impares = []
    for n in range(0, 10):
        while True:
            tmp = int(input(f'Digite o {n+1}° valor: [0 à 50] '))
            if tmp >= 0 and tmp <= 50:
                break
    
        vet.append(tmp)

    for n in vet:
        if n % 2 != 0:
            impares.append(n)
    
    print(f'Todos os valores: {vet}')
    print(f'Apenas valores ímpares: {impares}')
