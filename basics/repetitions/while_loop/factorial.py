num = int(input("Please enter a number: "))
factorial = 1

while num:
	factorial *= num
	num -= 1

print("The factorial is", str(factorial) + ".")
