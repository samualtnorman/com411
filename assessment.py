# import sys
# import matplotlib
import matplotlib.pyplot as plt

# matplotlib.use("Agg")

def combined():
	plt.figure("Combined")
	plt.subplot(111)
	plt.triplot(
		[ 3, 5, 7 ], [ 3, 5, 3 ], "r--o",
		[ 3, 5, 7 ], [ 5, 3, 5 ], "b--s",
		[ 3, 3, 7 ], [ 3, 5, 4 ], "g-.*",
		[ 7, 7, 3 ], [ 3, 5, 4 ], "y-p"
	)
	plt.show()

combined()

def seperated():
	plt.figure("Seperated")
	plt.subplot(221)
	plt.triplot([ 3, 5, 7 ], [ 3, 5, 3 ], "r--o")
	plt.subplot(222)
	plt.triplot([ 3, 5, 7 ], [ 5, 3, 5 ], "b--s")
	plt.subplot(223)
	plt.triplot([ 3, 3, 7 ], [ 3, 5, 4 ], "g-.*")
	plt.subplot(224)
	plt.triplot([ 7, 7, 3 ], [ 3, 5, 4 ], "y-p")
	plt.show()

seperated()

def data():
	return [
		{
			"x": [ 3, 5, 7 ],
			"y": [ 3, 5, 3 ],
			"format": "r--o"
		},
		{
			"x": [ 3, 5, 7 ],
			"y": [ 5, 3, 5 ],
			"format": "b--s"
		},
		{
			"x": [ 3, 3, 7 ],
			"y": [ 3, 5, 4 ],
			"format": "g-.*"
		},
		{
			"x": [ 7, 7, 3 ],
			"y": [ 3, 5, 4 ],
			"format": "y-p"
		}
	]

def improved_separated():
	plt.figure("Improved Seperated")
	i = 1

	for tri in data():
		plt.subplot(220 + i)
		i += 1
		plt.triplot(tri["x"], tri["y"], tri["format"], )

	plt.show()

improved_separated()

# plt.savefig(sys.stdout.buffer)
# sys.stdout.flush()
