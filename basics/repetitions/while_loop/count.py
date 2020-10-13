toAvoid = int(input("How many live cables must I avoid? "))
avoided = 0

# Why a while loop???

while avoided < toAvoid:
	print("Avoiding...", end = "") # I'm not a fan of this hackery either
	avoided += 1
	print("Done", avoided, "live cables avoided.")

print("All live cables have been avoided.")
