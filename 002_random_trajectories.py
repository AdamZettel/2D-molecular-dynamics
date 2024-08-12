import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from celluloid import Camera

numpoints = 100
points = np.random.random((2, numpoints)) - 0.5 # make the points start between (-0.5, 0.5)
velocities = np.random.random((2, numpoints)) - 0.5
timestep = 0.1
steps = 100

colors = cm.rainbow(np.linspace(0, 1, numpoints))
camera = Camera(plt.figure())
for _ in range(steps):
	points += velocities*timestep
	plt.xlim((-2,2))
	plt.ylim((-2,2))
	plt.scatter(*points, c=colors, s=100)
	camera.snap()
anim = camera.animate(blit=True)
anim.save('002_random_trajectories.gif')
