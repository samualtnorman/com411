where0 = input("Where should I look? ")
where1 = input("Where " + where0 + " should I look? ")

if where0 == "in the bedroom":
	if where1 == "under the bed":
		print("Found some shoes but no battery")
	else:
		print("Found some mess but no battery.")
elif where0 == "in the bathroom":
	if where1 == "in the bathtub":
		print("Found a rubber duck but no battery")
	else:
		print("Found a wet surface but no battery.")
elif where0 == "in the lab":
	if where1 == "on the table":
		print("Yes! I found my battery!")
	else:
		print("Found some tools but no battery.")
else:
	print("I do not know where that is but I will keep looking.")
