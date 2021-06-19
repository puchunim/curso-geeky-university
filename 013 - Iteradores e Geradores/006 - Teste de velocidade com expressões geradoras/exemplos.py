# Generators (Geradores)

def nums():
	for num in range(1, 10):
		yield num

ge1 = nums()
print(ge1) # <generator object>

# Generator Expression

ge2 = (num for num in range(1, 10))
print(ge2) # <generator object <genexpr>>


# Realizando o teste de velocidade
from time import time


# GenExpr
gen_ini = time()
print(sum(num for num in range(100_000_000)))
gen_tempo = time() - gen_ini


# List Comprehension
list_ini = time()
print(sum([num for num in range(100_000_000)]))
list_tempo = time() - list_ini

print(f'Generator Expr levou {gen_tempo}')
print(f'List comprehension levou {list_tempo}')