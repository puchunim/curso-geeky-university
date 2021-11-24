def ex021():
    """
    Faça um programa que receba do usuário dois vetores,
    A e B, com 10 números inteiros cada. Crie um novo
    vetor denominado C calculando C = A - B. Mostre na
    tela os dados do vetor C.
    """
    a = []
    b = []
    for n in range(0, 10):
        a.append(
            int(input(f'Digite o {n+1}° valor do vetor A: '))
        )
    
    for n in range(0, 10):
        b.append(
            int(input(f'Digite o {n+1}° valor do vetor B: '))
        )

    c = a.copy()
    for n in b:
        if n in c:
            c.remove(n)

    print(f'Vetor A: {a}')
    print(f'Vetor B: {b}')
    print(f'O vetor C (A - B), contém: {c}')

def ex022():
    """
    Faça um programa que leia dois vetores de
    10 posições e calcule outro valor contendo,
    nas posições pares os valores do primeiro
    e nas posições impares os valores do segundo.
    """

    vet1 = []
    vet2 = []
    vet3 = list(range(0, 20))

    for n in range(0, 10):
        vet1.append(
            int(input(f'Digite o {n+1}° valor para o Vetor 1: '))
        )
    
    for n in range(0, 10):
        vet2.append(
            int(input(f'Digite o {n+1}° valor para o Vetor 2: '))
        )
    
    for n in vet3:
        if n % 2 == 0:
            vet3[n] = vet1.pop(0)
        
        else:
            vet3[n] = vet2.pop(0)


    print(vet3)

def ex023():
    """
    Ler dois de números reais, armazenando-os em vetores
    e calcular o produto escalar entre eles. Os conjuntos
    têm 5 elementos cada. Imprimir os dois conjuntos e o
    produto escalar, sendo o produto escalar é dado por
        x1*y1 + x2*y2 + ... + xn*yn
    """

    x = []
    y = []
    p_escalar = 0
    for n in range(0, 5):
        x.append(
            int(input(f'Digite o {n+1}° valor para o vetor X: '))
        )
    
    for n in range(0, 5):
        y.append(
            int(input(f'Digite o {n+1}° valor para o vetor Y: '))
        )
    
    for n in range(1, 6):
        p_escalar += (x[n-1] * n) * (y[n-1] * n)
    
    print(x)
    print(y)
    print(p_escalar)

def ex024(): # n ta funfando :eyes:
    """
    Faça um programa que leia dez conjuntos de dois valores,
    o primeiro representado o número do aluno e o segundo
    representando a sua altura em metros. Encontre o aluno
    mais baixo e o mais alto. Mostre o número do aluno mais
    baixo e do mais alto, juntamente com suas alturas
    """

    alunos = []
    for n in range(0, 10):
        tmp_number = int(input(f'Digite o número do {n+1}° aluno: '))
        tmp_height = int(input(f'Digite a altura do {n+1}° aluno: '))
        alunos.append((tmp_number, tmp_height))

    print(f'O {max(alunos)[0]}° aluno é o mais alto, ele tem {max(alunos)[1]}cm!')
    print(f'O {min(alunos)[0]}° aluno é o mais baixo, ele tem {min(alunos)[1]}cm!')

def ex025(): # pulado
    """
    Faça um programa que preencha um vetor
    de tamanho 100 com os 100 primeiros naturais
    que não são múltiplos de 7 ou que terminam com 7
    """

    pass

def ex026(): # KKKKKKKKK pulado dnv
    """
    Faça um programa que calcule o desvio padrão de um vetor
    v contendo n = 10 números, onde m é a média do vetor
    """

def ex027(): # FKLEWGKJLGKJEWKJGEKJ hoje n é meu dia
    """
    Leia 10 números inteiros e armazene em um vetor.
    Em seguida, escreva os elementos que são primos
    e suas respectivas posições no vetor.
    """

    vet = []
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )

    for i in vet:
        for n in range(1, i):
            if not i % n == 0:
                print(f'{i} => pos {vet.index(i)}')

def ex028():
    """
    Leia 10 números inteiros e armazene em um vetor v.
    Crie dois novos vetores v1 e v2, copie os valores
    impares de v para v1, e os valores pares de v para
    v2. Note que cada um dos vetores v1 e v2 tem no máximo
    10 elementos, mas nem todos os elementos são utilizados.
    No final escreva os elementos UTILIZADOS de v1 e v2.
    """

    vet = []
    vet1 = []
    vet2 = []
    
    for n in range(0, 10):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    for n in vet:
        if n % 2 == 0:
            vet2.append(n)

        else:
            vet1.append(n)

    print(f'Vetor: {vet}')
    print(f'Pares: {vet2}')
    print(f'Impares: {vet1}')

def ex029():
    """
    Faça um programa que receba 6 números inteiros e mostre:
        - Os números pares digitados;
        - A soma dos números pares digitados;
        - Os números ímpares digitados;
        - A quantidade de números ímpares digitados;
    """

    vet = []
    for n in range(0, 6):
        vet.append(
            int(input(f'Digite o {n+1}° valor: '))
        )
    
    pares = []
    impares = []
    for n in vet:
        if n % 2 == 0:
            pares.append(n)
        
        else:
            impares.append(n)
    
    print(vet)
    print(f'Números pares digitados: {pares}')
    print(f'Números impares digitados: {impares}')
    print(f'Soma dos números pares: {sum(pares)}')
    print(f'Quantidade de números impares: {len(impares)}')

def ex030():
    """
    Faça um programa que leia dois vetores de 10 elementos.
    Crie um vetor que seja a intersecção entre os 2 vetores
    anteriores, ou seja, que contém apenas os números que
    estão em ambos os vetore. Não deve conter números repetidos
    """

    vet1 = []
    vet2 = []
    for n in range(0, 10):
        vet1.append(
            int(input(f'Digite o {n+1}° valor para o vetor 1: '))
        )

        vet2.append(
            int(input(f'Digite o {n+1}° valor para o vetor 2: '))
        )
    
    vet1.extend(vet2)
    print(f'A intersecção entre o primeiro e o segundo vetor é: {list(set(vet1) & set(vet2))}')
