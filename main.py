'''
04/19/2021
Review
Function
def FunctionName(PARAMETERS):
	BODY
	return (optional)
_____________________________________________________

# Warm up 1
# list of user numbers
numbers = []
def getNumbers():
	userNumber = input("Enter a number or 'q' to quit: ")
	while (userNumber != 'q'):
		numbers.append(int(userNumber))
		userNumber = input("Enter a number or 'q' to quit: ")
getNumbers()

def sum(numberList):
	total = 0
	for i in numberList:
		total += i
	print ("The sum is " + str(total))
sum(numbers)

def product(numberList):
	total = 1
	for i in numberList:
		total *= i
	print ("The product is " + str(total))
product(numbers)


# Warm up 2 - Fahrenheit to Celcius Conversion
# (F - 32) * 5 / 9 = C
# Function w/ return
def tempConvert(F):
	return (F - 32) * 5 / 9
temp = float(input("Temperature in Fahrenheit: "))
# OUTPUT: #F = #C
print (str(temp) + " F = " + str(tempConvert(temp)) + " C")
def getInfo(name, age, school):
	print ("Name: " + name)
	print ("Age: " + age)
	print ("School: " + school)
getInfo(input("What is your name? "), input("How old are you? "), input("what is your school name? "))


Recursion
- A defined function can call itself. It is a common mathematical and programming concept. Every recursive function requires to have a parameter and a base condition.
Formula:
def functionName(parameter):
	if (CONDITION): 	# base condition
		return something
	else:
		return something
'''

# Recursion (Factorial)
def factorial(x):
	if (x == 1 or x == 0):
		return 1
	else:
		return x * factorial(x - 1)		# 5 * 4 * 3 * 2 * 1

print(factorial(5))	# 5! = 5 * 4 * 3 * 2 * 1 = 120
print (5 * 4 * 3 * 2 * 1)