class Animal:
	def __init__(self, species, name, age):
		self.species = species
		self.name = name
		self.age = age


bennett = Animal("Human", "Bennett", 20)
print(bennett.age)
bennett.age = 21
print(bennett.age)