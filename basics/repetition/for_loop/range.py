brightnessGoal = int(input("What level of brightness is required? "))

print("\nAdjusting brightness...")

for i in range(2, brightnessGoal + 1, 2):
	art = "*" * i
	print("Beep's brightness level:", art, "\nBop's brightness level:", art, "\n")

print("Adjustments complete!")
