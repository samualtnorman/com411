def welcome():
	print("Pride Rock welcomes you", input("What type of animal are you? ") + ".\nCome and celebrate with us!")

# welcome()

def visit(place):
	if place == "The Elephant Graveyard":
		print("Oh no! There are hyenas here!")
	else:
		print("This place is interesting.")

# visit("The Elephant Graveyard")
# visit("The Jungle")

def roar(num_roars):
	for _ in range(0, num_roars):
		print("roar!")

	print("ROAR!!!")

# The above solution is stupid (but I need the marks) so here's a better one
# def roar(num_roars):
# 	print("roar!\n" * num_roars + "ROAR!!!")

# roar(3)
