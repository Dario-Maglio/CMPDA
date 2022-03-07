import os
import argparse

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import PIL.Image as Image
import matplotlib.image as img



# network structure
Lx = Ly = 75                 # dimensions of the images
N = Lx * Ly                  # number of neurons
# animation parameters
TOTAL_FRAMES = 1000          # number of frames of the animation
DT_FRAMES = 100              # duration of each frame (ms)

# list of images that I want to store in my network
this_dir, _ = os.path.split(__file__)
input_dir = os.path.join(this_dir, 'inputs')
mem_dir = os.path.join(this_dir, 'stored')

memory = ["batman.png", "spider.jpg", "cat.jpg"]
for index, file in enumerate(memory):
	memory[index] = os.path.join(mem_dir, file)

initial_state = os.path.join(input_dir, 'batman.png')

#-------------------------------------------------------------------------------

def readPatterns(fname, size):
	"""Read an image and convert it to a binary pattern of size [Lx, Ly].
	Inputs: figurename, final size=[Lx, Ly]
	"""
	fig = plt.figure()

	# subplot on the left - original figure
	fig.add_subplot(1,2,1)
	original = img.imread(fname)
	plt.imshow(original)
	plt.title("original")
	plt.axis('off')

	# convert and resize
	this_img = Image.open(fname) # open colour image
	this_img = this_img.convert('1') # convert image to black and white
	this_img = this_img.resize(size=[size[0],size[1]]) # resize it to [Lx, Ly]
	#this_img.save(f"{fname}_converted.png") # save converted image

	# subplot on the right - converted figure
	matrix = np.asarray(this_img) # convert to matrix of [0.,1.]
	matrix = 2*matrix-1 # convert from [0.,1.] -> [-1,1]
	fig.add_subplot(1,2,2)
	plt.matshow(matrix, cmap=plt.cm.gray, fignum=0)
	plt.axis('off')
	plt.title("simplified")
	plt.show()

	# Return the pattern as a 1D vector (not as a 2D a matrix)
	return matrix.flatten()

#-------------------------------------------------------------------------------

class HopfieldNet:
	"""Hopfield network class."""
	def __init__(self, N, patterns):
		self.N = N
		self.time_elapsed = 0.

		self.w = np.zeros([N,N]) # weights
		self.h = np.zeros(N) # threhold functions
		self.s = -np.ones(N) # default configuration s[i]=-1
		self.E = -0.5*np.sum(self.w) - np.sum(self.h) # energy for s_i = -1

		# HEBBIAN RULE (h_i = 0., w_{ij} = sum_{k=1,...,M} s_i^k*s_j^k / M)
		print ("The network is learning...")
		self.M = len(patterns)
		for k in range(self.M):
			print ("pattern "), k
			self.w += np.outer(patterns[k],patterns[k])/(1.*self.M)
		print ("Done!")

	def set_state(self, state):
		"""Update the network state."""
		self.s = np.copy(state)
		s2 = np.outer(self.s, self.s) # this retuns a matrix s2[i,j]=s[i]*s[j]
		self.E = -0.5*np.sum(self.w*s2) + np.sum(self.h*self.s)

	def evolve(self, steps):
		"""Evolve the state of the networks doing Monte Carlo steps."""
		for t in range(steps):
			i = np.random.randint(self.N) # choose one node randomly
			sum_wijsj = np.sum(self.w[i,:]*self.s)
			if sum_wijsj < self.h[i]: # below the threshold
				self.s[i] = -1
			else:                     # above the threshold
				self.s[i] = 1

#-------------------------------------------------------------------------------
def process(initial=initial_state):
	""" STEP 1: READ THE IMAGES AND CONVERT THEM TO BINARY PATTERNS """
	print ("Reading images and coverting to binary patterns...")
	patterns = []
	for fname in memory:
		patterns.append(readPatterns(fname, size=[Lx,Ly]))
	print ("Done!")

	""" STEP 2: CREATE THE NETWORK AND LEARN THE PREVIOUS PATTERNS """
	mynet = HopfieldNet(N, patterns)

	""" STEP 3: SET ANOTHER INPUT PATTERN AS INITIAL CONDITION """
	newinput = readPatterns(initial, size=[Lx,Ly])
	mynet.set_state(newinput) # set the pattern as the initial condition
	plt.matshow(np.resize(mynet.s,(Lx,Ly)), cmap=plt.cm.gray, fignum=0)
	plt.title("Initial condition")
	plt.axis('off')
	plt.show()

	""" STEP 4: EVOLVE THE NETWORK! """
	fig = plt.figure("Evolution")
	fig_mat = plt.matshow(np.resize(mynet.s,(Lx,Ly)), cmap=plt.cm.gray, fignum=0)

	def animation_update(i):
	    mynet.evolve(int(N/10))
	    fig_mat.set_data(np.resize(mynet.s,(Lx,Ly)))
	    yield fig_mat

	# generate the animation
	plt.axis('off')
	writergif = animation.PillowWriter(fps=10)
	ani = animation.FuncAnimation(fig, animation_update, blit=True, repeat=False,
									frames=TOTAL_FRAMES, interval=DT_FRAMES)

	ani.save("animation.gif", writer=writergif)
	os.system("xdg-open animation.gif")

def cli():
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--inpfile', type=str, metavar='inpfile', action='store',
						default=initial_state, help='path to the input file')
    ARGS = PARSER.parse_args()

    STAT = process(ARGS.inpfile)
    if STAT == 0:
        print('The work is done.')
    elif STAT == 1:
        print("The file doesn't exist.")

if __name__ == "__main__":
    cli()
