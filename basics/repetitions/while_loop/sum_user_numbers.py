toSumCount = int(input("How many numbers should I sum up? "))

# Ugh I hate that we're using while loops here for something that was clearly meant for for loops

i = 1
sumCountStr = str(toSumCount)
userSum = 0

while i <= toSumCount:
	userSum += int(input("Please enter number " + str(i) + " of " + sumCountStr + ": "))
	i += 1

print("The answer is ", userSum)
