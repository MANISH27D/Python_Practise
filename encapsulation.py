#Encapsulation: hide in depth details
class Car:
	def __init__(self):
		self._speed = 50 

	def accelerate(self, amount):
		self._speed += amount

	def decelerate(self, amount):
		self._speed -= amount

	def get_speed(self):
		if self._speed < 0:
			return 0
		return self._speed

my_car = Car()
my_car.decelerate(100)
my_car.accelerate(10)
print(my_car.get_speed())