import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import PIL.Image as Image
import matplotlib.image as img

# read an image and convert it to a binary pattern of size [Lx, Ly]:
# arguments = figurename, final size=[Lx, Ly]
def readPatterns(fname, size):
	this_img = Image.open(fname) # open colour image
	this_img = this_img.convert('1') # convert image to black and white
	this_img = this_img.resize(size=[size[0],size[1]]) # resize it to have the dimensions [Lx, Ly]
	this_img.save("%s_converted.png"%fname) # save converted image

	# plot the original and the converted file
	fig = plt.figure()

	# subplot on the left - original figure
	fig.add_subplot(1,2,1)
	original = img.imread(fname)
	plt.imshow(original)
	plt.title("original")
	plt.axis('off')

	# subplot on the right - converted figure
	matrix = img.imread("%s_converted.png"%fname) # re-read from the file and convert it to a matrix of [0.,1.]
	matrix = 2*matrix-1 # convert from [0.,1.] -> [-1,1]
	fig.add_subplot(1,2,2)
	plt.matshow(matrix, cmap=plt.cm.gray,fignum=0)
	plt.axis('off')
	plt.title("simplified")
	plt.show()

	# Return the pattern as a 1D vector (not as a 2D a matrix)
	return matrix.flatten()

#####################################################################################



class HopfieldNet:
	# initialize:
	# arguments = number of neurons, list of patterns (vector of M componens, each element of the pattern has to be an array of -1,+1 of size N)
	def __init__(self, N, patterns):
		self.N = N
		self.time_elapsed = 0.

		self.w = np.zeros([N,N]) # weights
		self.h = np.zeros(N) # threhold functions

		self.s = -np.ones(N) # default configuration = s[i]=-1

		# HEBBIAN RULE (h_i = 0., w_{ij} = sum_{k=1,...,M} s_i^k*s_j^k / M)
		print ("The network is learning...")
		self.M = len(patterns)
		for k in range(self.M):
			print ("pattern "), k
			# this is not efficient, but we could use it anyway:
#			for i in range(self.N):
#				for j in range(self.N):
#					self.w[i,j] += patterns[k][i]*patterns[k][j]/(1.*self.M)

			# it is more efficient to use built-in functions:
			self.w += np.outer(patterns[k],patterns[k])/(1.*self.M)


		print ("Done!")


#		# COMPUTE THE ENERGY - As before, I avoid loops and use efficient functions
		self.E = -0.5*np.sum(self.w) - np.sum(self.h) # energy for s_i = -1

		return

	# given and input s=[s_1,s_2,...,s_N], set the state of the network and recompute the energy
	def set_state(self, sinput):
		self.s = np.copy(sinput)

		# COMPUTE THE ENERGY - I use efficient functions rather than loops
		s2 = np.outer(self.s, self.s) # this retuns a matrix s2[i,j]=s[i]*s[j]
		self.E = -0.5*np.sum(self.w*s2) + np.sum(self.h*self.s)

		return

	# evolve the state of the networks doing a number "steps" of Monte Carlo steps
	def evolve(self, steps):
		for t in range(steps):
			i = np.random.randint(self.N) # choose one node randomly

			sum_wijsj = np.sum(self.w[i,:]*self.s) # compute the argument of the activation function
			if sum_wijsj < self.h[i]: # below the threshold
				self.s[i] = -1
			else: # above the threshold
				self.s[i] = 1

		return
#######################################################################


# dimensions of the images
Lx = Ly = 80
N = Lx*Ly # number of neurons



## STEP 1: READ THE IMAGES AND CONVERT THEM TO BINARY PATTERNS

# list of images that I want to store in my network
files = ["stored/batman0.png", "stored/cat.jpg", "stored/aaaa.jpg"]

print ("Reading images and coverting to binary patterns...")
patterns = []
for fname in files:
	patterns.append(readPatterns(fname, size=[Lx,Ly]))
print ("Done!")

## STEP 2: CREATE THE NETWORK AND LEARN THE PREVIOUS PATTERNS
mynet = HopfieldNet(N, patterns)


## STEP 3: SET ANOTHER INPUT PATTERN AS INITIAL CONDITION
newinput = readPatterns("inputs/ssss.jpg", size=[Lx,Ly]) # read the pattern from a file
mynet.set_state(newinput) # set the pattern as the initial condition of the network
plt.matshow(np.resize(mynet.s,(Lx,Ly)), cmap=plt.cm.gray, fignum=0) # read the state (we reconvert it to a Lx*Ly matrix) and plot it
plt.title("Initial condition")
plt.axis('off')
plt.show()


## STEP 4: EVOLVE THE NETWORK!



#################### ANIMATION #################################
# animation
TOTAL_FRAMES = 1000000 # number of frames of the animation
DT_FRAMES = 100 # duration of each frame (ms): we can accelerate or slow down the animation changing this

fig = plt.figure()
fig_mat = plt.matshow(np.resize(mynet.s,(Lx,Ly)), cmap=plt.cm.gray, fignum=0) # see more colormaps in https://matplotlib.org/examples/color/colormaps_reference.html
plt.axis('off')

# functions used to produce the animation
def animation_init(): # how to initialize the animation (if we put things here they will be fix in the animation)
	fig_mat.set_data(np.resize(mynet.s,(Lx,Ly)))
	return fig_mat

def animation_update(i):
        mynet.evolve(int(N/10))
        fig_mat.set_data(np.resize(mynet.s,(Lx,Ly)))
        return fig_mat

# generate the animation
ani = animation.FuncAnimation(fig, animation_update, frames=TOTAL_FRAMES, interval=DT_FRAMES, blit=False, repeat=False) # blit is used to make simulation faster
plt.show()
#quit()
