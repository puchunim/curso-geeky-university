"""
Forçando tipos de dados com decoradores

"""

def forca_tipo(*tipos):
    def decorador(func):
        def converte(*args, **kwargs):
            novo_args = []
            for (valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return func(*novo_args, **kwargs)
        return converte
    return decorador

@forca_tipo(str, int)
def repete(msg, vezes):
    for vez in range(vezes):
        print(msg)

repete('pica', 30)     