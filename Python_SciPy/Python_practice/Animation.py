import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig = plt.figure()
camera = Camera(fig)
for i in range(20):
    t = plt.plot(range(i, i + 5))
    plt.legend(t, [f'line {i}'])
    camera.snap()
animation = camera.animate()
animation.save('celluloid_legends.gif')


fig, axes = plt.subplots(2)
camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 128)
for i in t:
    a = axes[0].plot(t, np.sin(t + i), color='orange', label =f'first {t}')
    b = axes[1].plot(t, np.sin(t - i), color='blue', label =f'second {t}')
    camera.snap()

animation = camera.animate()
animation.save('celluloid_subplots.gif')


import matplotlib.animation as animation
plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

# initialization function
def init():
	# creating an empty plot/frame
	line.set_data([], [])
	return line,

# lists to store x and y axis points
xdata, ydata = [], []

# animation function
def animate(i):
	# t is a parameter
	t = 0.1*i

	# x, y values to be plotted
	x = t*np.sin(t)
	y = t*np.cos(t)

	# appending new points to x, y axes points list
	xdata.append(x)
	ydata.append(y)
	line.set_data(xdata, ydata)
	return line,

# setting a title for the plot
plt.title('Creating a growing coil with matplotlib!')
# hiding the axis details
plt.axis('off')

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
							frames=500, interval=20, blit=True)
# save the animation as mp4 video file
anim.save('coil.gif')
plt.show()
