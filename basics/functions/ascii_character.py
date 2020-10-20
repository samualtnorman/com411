asciiCode = abs(int(input("Program Started!\nPlease enter an ASCII code: ")))

if (asciiCode not in range(32, 127)):
	raise Exception("asciiCode must be inclusively between 32 and 126, got '" + str(asciiCode) + "'")

print("The character represented by the ASCII code {code} is {character}.\nProgram Ended!".format(code = asciiCode, character = chr(asciiCode)))
