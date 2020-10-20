phrase = input("What phrase do you see? ")
phraseLength = len(phrase)

o = ""

print("\nReversing...")

# I'm really not sure what this task wanted that was different to the last one, so here's what I got

for char in reversed(phrase):
	o += char

print("\nThe phrase is:", o)
