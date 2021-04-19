def ex031():
    """
    Faça um programa que leia dois vetores de 10 elementos.
    Crie um vetor que seja a união entre os 2 vetores anteriores,
    ou seja, contém os números dos dois vetores. Não deve conter
    números repetidos.
    """

    vet1 = []
    vet2 = []
    for n in range(0, 10):
        vet1.append(
            int(input(f'Digite o {n+1}° valor do vetor 1: '))
        )

        vet2.append(
            int(input(f'Digite o {n+1}° valor do vetor 2: '))
        )
    
    print(f'A união entre os dois vetores é: {list(set(vet1) | set(vet2))}')

def ex032():
    """
    Leia dois vetores inteiros x e y, cada um com 5 elementos (assuma
    que o usuário não informe elementos repetidos). Calcule e mostre
    os vetores resultantes em cada caso abaixo:
        - Soma entre x e y;
        - Produto entre x e y;
        - Diferença entre x e y;
        - Interseção entre x e y;
        - União entre x e y;
    """

    x = []
    y = []

    for n in range(0, 5):
        x.append(
            int(input(f'Digite o {n+1}° valor do vetor X: '))
        )

        y.append(
            int(input(f'Digite o {n+1}° valor do vetor Y: '))
        )
    
    soma = []
    produto = []
    for n in range(0, 5):
        soma.append(x[n] + y[n])
        produto.append(x[n] * y[n])

    print(f'A soma entre os dois vetores é {soma}')
    print(f'O produto entre os dois vetores é {produto}')
    print(f'A diferença entre os dois vetores é {list(set(x).difference(set(y)))}')
    print(f'A interseção entre os dois vetores é {list(set(x) | set(y))}')
    print(f'A união entre os dois vetores é {list(set(x) & set(y))}')

def ex033():
    """
    Faça um programa que leia um vetor de 15 posições
    e o compacte, ou seja, elimine posições com valor
    zero. Para isso, todos os elementos à frente do
    valor zero, devem ser movidos uma posição para
    trás no vetor.
    """

    vet = []
    for n in range(0, 15):
        vet.append(
            int(input(f'Digite o {n+1}° valor do vetor: '))
        )
    
    while 0 in vet:
        vet.pop(vet.index(0))
    
    print(vet)

def ex034():
    """
    Faça um programa para ler 10 números DIFERENTES
    a serem armazenados em um vetor. Os dados deverão
    ser armazenados no vetor na ordem que forem sendo
    lidos, sendo que caso o usuário digite um número
    já digitado anteriormente, o programa deverá pedir
    por outro número. Note que cada valor digitado pelo
    usuário deve ser pesquisado no vetor, verificando
    se ele existe entre os números que já foram forne-
    cidos. Exiba na tela o vetor final que foi digitado.
    """

    vet = []
    for n in range(0, 10):
        while True:
            tmp = int(input(f'Digite o {n+1}° valor do vetor (não repetido): '))
            if tmp not in vet:
                break
        vet.append(tmp)
    print(vet)

def ex035():
    """
    Faça um programa que leia dois números a e b (positivos menores qu 10000) e:
        - Crie um vetor onde cada posição é um algarismo do número.
        A primeira posição é o algarismo menos significativo;
        - Crie um vetor que seja a soma de a e b, mas faça-o usando
        apenas os vetores construídos anteriormente.
    """

    while True:
        n1 = str(input('Digite o 1° número (menor que 10000): '))
        if int(n1) < 10000:
            break
    
    while True:
        n2 = str(input('Digite o 2° número (menor que 10000): '))
        if int(n2) < 10000:
            break
    
    vet1 = [l for l in n1]
    vet2 = [l for l in n2]

    vet1.sort()
    vet2.sort()

    print(vet1)
    print(vet2)
    print([i for i in str((int(n1) + int(n2)))])

def ex036():
    """
    Leia um vetor com 10 números reais, ordene os elementos
    deste vetor, e no final escreva os elementos do vetor
    ordenado.
    """
    
    vet = []
    for n in range(0, 10):
        vet.append(
            float(input(f'Digite o {n+1}° valor real: '))
        )
    
    vet.sort()
    print(vet)

def ex037(): # pulado
    """
    Considere um vetor A com 11 elementos onde:
        A1 < A2 < ... < A6 > A7 > A8 > ... > A11,
    ou seja, est ordenado em ordem crescente até
    o sextos elemento, e a partir desse elemento
    está ordenado em ordem decrescente. Dado o
    vetor da questão anterior, proponha um algoritmo
    para ordenar os elementos.
    """

def ex038():
    """
    Peça ao usuário para digitar dez valores numéricos
    e ordene por ordem crescente esses valores, guardando-os
    num vetor. Ordene o valor assim que ele for digitado. Mostre
    ao final na tela os valores em ordem.
    """

    vet = []
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    vet.sort()
    print(vet)

def ex039(): # pulado
    """
    Escreva um programa que leia um número inteiro
    positivo n e em seguida imprima n linhas do chamado
    Triangulo de Pascal.
    """
