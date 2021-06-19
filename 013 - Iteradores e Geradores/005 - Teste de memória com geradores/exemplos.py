
# Uma função que gera uma sequência de Fibonacci (usando listas)
def fib(_max):
	nums = []
	a, b = 0, 1
	while len(nums) < _max:
		nums.append(b)
		a, b, = b, a+b
	return nums

'''for n in fib(100000): # 449.9mb de memória
	print(n)'''

# Uma função geradora para a sequência Fibonacci
def fib2(_max):
	a, b, contador = 0, 1, 0
	while contador < _max:
		a, b = b, a+b
		yield a
		contador += 1

'''for n in fib2(100000): # 3mb de memória
	print(n)'''

