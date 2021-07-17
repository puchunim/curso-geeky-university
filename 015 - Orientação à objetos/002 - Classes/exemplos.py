"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real,
sendo representados computacionalmente, através da abstração.


[O que são classes?]

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.
Em Python e outras linguagens, não há um tipo de dado que represente algo como uma lâmpada, por isso
podemos criar uma classe que o represente.

    class Lampada:
        pass

    led = Lampada()


[Classes podem conter]
    - Atributos => As características de um objeto. No caso da lâmpada, podemos saber
    se ela é 110 ou 220v, sua cor, seu fabricante, luminosidade e afins.
    
    - Métodos => Funções ligadas ao objeto. Podem representar comportamentos do objeto. No
    caso da lâmpada, poderia haver um método que ligasse ou desligasse.

Para definir uma classe, utilizamos uma palavra reservada chamada "class".

OBS: Utilizamos a palavra 'pass' em Pyhton quando temos um bloco de código que ainda
não está implementado, então ele não vai dar erro se rodar.

OBS²: Quando nomeamos NOSSAS CLASSES em Python, utilizamos por convenção o nome com inicial
em maiúsculo. Se o nome for composto utiliza-se as inicias de ambas as palavras em maiúsculo,
todas juntas.

    class Lampada:
        pass
        
        
    class ContaCorrente:
        pass

OBS³: Quando estamos planejando um software, definimos quais classes teremos no sistema. Chamamos
os objetos gerados por essas classes de entidades.

Dica: Em computação não utilizamos acentuação, caracteres especiais, espaços ou similares, para
nomes de classes, atributos, métodos, arquivos, diretórios e etc.
"""

