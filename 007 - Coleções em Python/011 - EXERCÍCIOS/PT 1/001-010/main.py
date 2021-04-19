def ex001():
    """
    Faça um programa que possua um vetor denominado A,
    que armazene 6 números inteiros. O programa deve
    executar os seguintes passos:
        (A) Atribua os seguintes valores pro vetor: 1, 0, 5, -2, -5, 7.
        (B) Armazene em uma variável inteira (simples) a soma entre os valores
        dsa posições A[0], A[1] e A[5] do vetor e mostre na tela essa soma.
        (C) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100
        (D) Mostre na tela cada valor do vetor A, um em cada linha.
    """

    a = [1, 0, 5, -2, -5, 7]
    soma = a[0] + a[1] + a[5]
    print(f'A soma das posições 0, 1 e 5 é igual a: {soma}')
    
    a[4] = 100
    print('mostrando todos os valores do vetor A')
    for n in a:
        print(n)

def ex002():
    """
    Crie um programa que lê 6 valores inteiros,
    e em seguida mostre na tela os valores lidos.
    """

    val = []
    for _ in range(0, 6):
        val.append(
            input(f'Digite o {_+1}° valor: ')
        )

    print(f'Os valore digitados foram: {val}')

def ex003():
    """
    Ler um conjunto de números reais, armazenando-o
    em vetor e calcular o quadrado dos componanetes,
    armazenando o resultado em outro vetor. Os conjuntos
    tem 10 elementos cada. Imprimir todos os conjuntos. 
    """

    floats = []
    sqr_floats = []
    for n in range(0, 10):
        floats.append(
            float(input(f'Digite o {n+1}° valor: '))
        )

    for f in floats:
        sqr_floats.append(f**2)
    
    print(f'Valores flutuantes originais: {floats}')
    print(f'Quadrado dos valores flutuantes: {sqr_floats}')

def ex004():
    """
    Faça um programa que leia um vetor de 8 posições e,
    ems eguida, leia também dois valores X e Y quaisquer
    correspondentes a duas posições no vetor. Ao final seu
    programa deverá escrever a soma dos valores encontrados
    nas respectivas posições X e Y.
    """

    vet = []
    for n in range(0, 8):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )

    while True:
        x = int(input('Digite um número de 0 a 7 para a variável X: '))
        if x >= 0 and x <= 7:
            break
    
    while True:
        y = int(input('Digite um número de 0 a 7 para a variável Y: '))
        if y >= 0 and y <= 7:
            break
    
    print(f'A soma de vet[{x}] + vet[{y}] é igual a: {vet[x] + vet[y]}')

def ex005():
    """
    Leia um vetor de 10 posições. Contar e escrever quantos valores
    pares ele possui.
    """

    vet = []
    pares = []
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    for n in vet:
        if n % 2 == 0:
            pares.append(n)
    
    print(f'Foram encontrados {len(pares)} números pares, e esses são: {pares}')

def ex006():
    """
    Faça um programa que receba do usuário um vetor
    com 10 posições. Em seguida deverá ser impresso
    o maior e o menor elemento do vetor.
    """

    vet = []
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    print(f'O maior elemento do vetor é {max(vet)}, o menor é {min(vet)}')

def ex007():
    """
    Escreva um programa que leia 10 números inteiros e os
    armazene em um vetor. Imprima o vetor, o maior elemento
    e a posição que ele se encontra.
    """

    vet = []
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    print(f'No vetor {vet}, o maios número é {max(vet)} e sua primeira aparição é na posição {vet.index(max(vet))}')

def ex008():
    """
    Crie um programa que leia 6 valores inteiros e, em seguida,
    mostre na tela os valores lidos na ordem inversa.
    """

    vet = []
    for n in range(0, 6):
        vet.append(
            int(input(f'Digite o {n+1}° número: '))
        )

    vet.reverse()
    print(f'O vetor digitado, ao contrário, ficaria: {vet}')

def ex009():
    """
    Crie um programa que leia 6 valores inteiros pares e,
    em seguida, mostre na tela os valores lidos na ordem
    inversa.
    """

    vet = []
    for n in range(0, 6):
        while True:
            tmp = int(input(f'Digite o {n+1}° valor par: '))
            if tmp % 2 == 0:
                break
        vet.append(tmp)
    
    vet.reverse()
    print(f'O reverso do vetor apresentado é: {vet}')

def ex010():
    """
    Faça um programa para ler a nota da prova de 15 alunos
    e armazene num vetor, calcule e imprima a média geral.
    """

    notas = []
    for n in range(0, 15):
        notas.append(
            float(input(f'Digite a nota do {n+1}° aluno: '))
        )

    print(f'A média dos valores de todas as notas é: {sum(notas) / len(notas)}')
