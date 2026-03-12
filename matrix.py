matrix = []

for j in range(5):
	sub_list = []
	for i in range(4):
		sub_list.append([0]*(i+j))
		matrix.append(sub_list)

print(matrix,sep='/n')

#using zip
a = [1,2,3]
b = [4,5,6]
output = list(zip(a,b))
print(output, sep='/n')

#dictionary
recipes = {}
recipes["Samosa"] = ["Potato", "Flour", "Garam Masala", "Salt", "Peas", "Oil", "Paneer"]
print(recipes, sep='/n')

for i in recipes:
	print(recipes[i])

#Word count
text = "Saitama aka Calped Baldly is strongest anime character. Saitama is friend of King aka strongest men on earth."

word_count = {}

repeated_char =""
for word in text.split():
	if word in word_count:
		word_count[word] += 1
	else:
		word_count[word] = 1

print(word_count)

#Exception Handling
def div(dividend, divisor):
	return dividend / divisor

def main():
	dividend = int(input("Enter dividend: "))
	divisor = int(input("Enter divisor: "))
	try:
		result = div(dividend, divisor)
		print(f"result: {result}")
	except ZeroDivisionError as e:
		print("You cannot divide by zero!")
	except ValueError as e:
		print("Invalid input. Please enter a number.")

