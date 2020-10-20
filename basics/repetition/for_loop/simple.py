mountainSplit = "           __       \n          /  \\_     \n         /^    \\    \n        /  ^    \\_  \n      _/ ^ ^     ^\\ \n     /  ^     ^    \\".split("\n")

mountainCount = int(input("How many mountains should I display? "))
print("\nDisplaying...")

for i in range(0, len(mountainSplit)):
	print(mountainSplit[i] * 3)

print("Done!")
