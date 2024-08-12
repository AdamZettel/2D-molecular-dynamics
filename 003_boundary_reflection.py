import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from celluloid import Camera

numpoints = 100
points = np.random.random((2, numpoints)) - 0.5 # make the points start between (-0.5, 0.5)
velocities = np.random.random((2, numpoints)) - 0.5
timestep = 0.1
steps = 100

x_max = 1.0
x_min = -1.0

y_max = 1.0
y_min = -1.0



def reflect_particle(coords, velocities, x_min, x_max, y_min, y_max):
	x = coords[0, :]
	y = coords[1, :]

	# Reflect x coordinates
	reflect_x = np.logical_or(x < x_min , x > x_max) 
	# Reflect y coordinates
	reflect_y = np.logical_or(y < y_min , y > y_max) 

	velocities[0, reflect_x] = -1.0*velocities[0, reflect_x]
	velocities[1, reflect_y] = -1.0*velocities[1, reflect_y]
	# Combine the reflected coordinates into a single array
	return velocities 


colors = cm.rainbow(np.linspace(0, 1, numpoints))
camera = Camera(plt.figure())
for _ in range(steps):
	points += velocities*timestep
	velocities = reflect_particle(points, velocities, x_min, x_max, y_min, y_max)
	plt.xlim((x_min, x_max))
	plt.ylim((y_min, y_max))
	plt.scatter(*points, c=colors, s=100)
	camera.snap()
anim = camera.animate(blit=True)
anim.save('003_boundary_reflection.gif')
