# Exemplo de Generator Function
# - A maio diferença entre uma função geradora
# e uma função normal é que a execução da função
# pausa na palavra yield, então pode ser executada
# mais vezes usando next().
def conta_ate(valor_maximo):
	contador = 1
	while contador <= valor_maximo:
		yield contador
		contador += 1

a = conta_ate(3)
print(next(a))
print(next(a))
print(next(a))
