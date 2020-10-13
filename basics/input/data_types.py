name = input("What is your name human? ")
age = input("How old are you (in years)? ")
height = float(input("How tall are you (in meters)? "))
weight = float(input("How much do you weigh (in kilograms)? "))

print(name, "you are", age, "years old and your bmi is", weight / height ** 2, ".")
