sequence = input("Please enter a sequence: ")
marker = input("Please enter the character for the marker: ")[0]

sequenceLength = len(sequence)

start = None

for i in range(sequenceLength):
	if sequence[i] == marker:
		if start == None:
			start = i
		else:
			print("The distance between the markers is", str(i - start - 1) + ".")
			break
