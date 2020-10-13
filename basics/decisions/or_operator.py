adventureType = input("Enter the type of adventure: ")

if adventureType == "scary" or adventureType == "short":
	print("Entering the dark forest!")
elif adventureType == "safe" or adventureType == "long":
	print("Taking the safe route!")
else:
	print("Not sure which route to take.")
