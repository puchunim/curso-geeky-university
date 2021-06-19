class Contador:
	"""
	Classe que funciona como um range()
	"""

	def __init__(self, menor, maior):
		self.menor = menor
		self.maior = maior

	def __iter__(self):
		"""
		Retorna o próprio objeto quando é usada a função
		iter()
		"""
		return self

	def __next__(self):
		"""
		Se o número atual for menor ou igual ao maior,
		o número será retornado e self.menor receberá
		+1. Caso o número for maior do que self.maior,
		um erro será levantado.
		"""

		if self.menor <= self.maior:
			numero = self.menor
			self.menor += 1
			return numero

		raise StopIteration

for n in Contador(1, 10):
	print(n)
