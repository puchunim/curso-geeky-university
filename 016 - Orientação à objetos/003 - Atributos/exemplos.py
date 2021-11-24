"""
POO - Atributos

Atributos => Representam as características do objeto. Pelos atributos,
conseguimos representar computacionalmente os estados e características do mesmo.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos;

# Atributos de instância: São atributos declarados dentro do método
construtor.

    [Método construtor é um método especial utilizado para a construção
    do objeto]
    
    # Em Java, uma classe Lâmpada com atributos ficaria assim:
    public class Lampada(){
        private int voltagem;
        private String cor;
        private Boolean ligada;
        
        public Lampada(int voltagem, String cor){
            this.voltagem = voltagem;
            this.cor = cor;
        }
    }
    
    # A mesma classe em Python
    class Lampada:
    
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


OBS: "self" é uma forma genérica de se referir à variável. Se no código dizemos
"self.nome = 'Pedro' " e a variável é "pessoa", então é só substituir "self" por
"pessoa"; "pessoa.nome == 'Pedro'"

OBS¹: "self" não é um nome obrigatório, mas é um nome dado por convenção.


Em Python, por convenção, todo atributo de uma classe é público.
Ou seja, pode ser acessado em todo o projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado (utilizado apenas
dentro da classe onde foi declarado), utiliza-se __ (duplo underscore) no início de seu nome.
    self.__atributo
Isso é chamado de Name Mangling.


# Classe com atributos públicos
class Publicos:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Classe com atributos privados
class Privados:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai
# impedir que façamos acesso aos atributos sinalizados como privados.

p = Privados('pedro', 32)
print(p.__nome) # AttributeError
print(p._Privados__nome) # Acesso normal, apesar de não ser uma boa usar

# O que significa atributos de instância?

# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão
# esses atributos.
class Usuario:
    def __init__(self, name, id):
        self.name = name
        self.id = id

# As duas instâncias da classe Usuario tem os mesmos atributos de instância,
# 'name' e 'id', mas com valores diferentes.
user1 = Usuario('pedro', 1234)
user2 = Usuario('adalberto', 5678)
 

# O que são atributos de classe?

# São atributos ligados à classe em si, e não à instância. Ou seja, são definidos
# fora do construtor. Geralmente já é inicializado com um valor, e este valor é
# compartilhado entre todas as instâncias.
class Produto:
    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        
p1 = Produto('PlayStation 4', 'Video Game', 2200)
p2 = Produto('Xbox S', 'Video Game', 2400)

# O valor muda
print(p1.valor)
print(p2.valor)

# O valor do imposto não
print(p1.imposto)
print(p2.imposto)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(Produto.imposto)

# Criando uma classe com ID autoincrementável
class Auto:
    contador = 0
    
    def __init__(self, nome):
        self.id = Auto.contador + 1
        self.nome = nome
        Auto.contador = self.id

a1 = Auto('abc')
a2 = Auto('def')
a3 = Auto('ghi')
print(a1.id) # 1
print(a2.id) # 2
print(a3.id) # 3
"""

# Atributos dinâmicos

# São atributos de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.
class Exemplo:
    def __init__(self, nome):
        self.nome = nome

p1 = Exemplo('pedro')
p2 = Exemplo('caterina')

# Criando um atributo dinâmico em tempo execução
p1.peso = 32 # o atributo 'peso' não existia, até ter sido criado

# Deletando atributos
del p1.peso
