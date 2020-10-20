phrase = input("What phrase do you see? ")
phraseLength = len(phrase)

o = ""

print("\nReversing...")

for i in range(phraseLength):
	o += phrase[phraseLength - i - 1]

print("\nThe phrase is:", o)
