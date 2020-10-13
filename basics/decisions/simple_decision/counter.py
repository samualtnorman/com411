odd = 0
even = 0

places = [ "first", "second", "third" ]

for i in range(0, 3):
	if int(input("Please enter the " + places[i] + " whole number: ")) % 2:
		odd += 1
	else:
		even += 1

print("There were", even, "even and", odd, "odd numbers.")
