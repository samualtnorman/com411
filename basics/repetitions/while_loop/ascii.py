toChargeCount = int(input("How many bars should be charged? "))

barsChargedCount = 0

while barsChargedCount < toChargeCount:
	barsChargedCount += 1
	print("Charging:", "█ " * barsChargedCount)

print("\nThe battery is fully charged.")
