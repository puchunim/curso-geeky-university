"""
Preservando metadatas com wraps

Metadados => São dados intrísecos em arquivos.

Dados de uma imagem:
- Nome;
- Tipo de arquivo (extenção);

Metadados de uma imagem:
- Tamanho;
- Largura;
- Altura;
- Data de criação;
- Data de modificação;

Wraps => São funções que envolvem elementos com diversas finalidades.
"""

# Problema

def ver_log(func):
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {func.__name__}')
        print(f'Aqui a documentação: {func.__doc__}')
        
        return func(*args, **kwargs)

    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    
    return a + b

print(soma(10, 30))

print(soma.__name__) # O nome vai ser o nome da função que o decorador retorna
print(soma.__doc__) # A documentação vai ser dela também

# Resolução

from functools import wraps

def ver_log_arrumado(func):
    @wraps(func)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando {func.__name__}')
        print(f'Aqui a documentação: {func.__doc__}')
        
        return func(*args, **kwargs)

    return logar

@ver_log_arrumado
def soma_arrumada(a, b):
    """Soma dois números"""
    return a + b

print(soma_arrumada.__name__)
print(soma_arrumada.__doc__)

