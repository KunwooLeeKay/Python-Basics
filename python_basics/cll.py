class Cafe:
	def __init__(self, order, people):
		self.order = str(order)
		self.people = int(people)
	def ordered(self):
		print(self.order + 'ordered! waiting : ' + str(self.people))

order1 = Cafe("Americano", 6)
print(order1.ordered())