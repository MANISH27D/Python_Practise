class Address: 
	def __init__(self,name,street,city):
		self.name = name
		self.street = street
		self.city = city

	def __str___(self):
		return f"{self.name}, {self.street}, {self.city}"

	def __eq__(self, other):
		return self.name == other.name	and self.street == other.street and self.city == other.city

my_address = Address(name="Manish Mishra", street="506 Block D", city="Delhi")
print(my_address.name)
print(my_address.__dict__)

my_address_duplicate = Address(name="Manish Mishra", street="506 Block D", city="Delhi")
myaddress1 = Address(name="Ravi Kishan", street="420 Gorakhpur", city="Uttar Pradesh")
print(myaddress1.name)
print(my_address == myaddress1)
print(my_address == my_address_duplicate)


class Bicycle:
	def number_of_gears(self):
		print(f"Has 12 gears")

class Mountainbike(Bicycle):
	pass

class Roadbike(Bicycle):
	def number_of_gears(self):
		print(f"Has 2 times 11 gears")

my_mountainbike = Mountainbike()
my_mountainbike.number_of_gears()
my_roadbike = Roadbike()
my_roadbike.number_of_gears()


