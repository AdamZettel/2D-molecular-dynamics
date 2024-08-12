import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from celluloid import Camera

numpoints = 100
points = np.random.random((2, numpoints)) # make the points start between (-0.5, 0.5)
velocities = np.random.random((2, numpoints)) - 0.5
timestep = 0.1
steps = 100

max_val = 1.0
min_val = 0.0

x_max = max_val 
x_min = min_val 
y_max = max_val 
y_min = min_val 

def euclid_distance_2d(a, b):
	return (np.linalg.norm(a-b)) 

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

camera = Camera(fig)
for _ in range(steps):
	distances = []
	for i in range(points.shape[0]):
		for j in range(points.shape[1]):
			if points[i][j] < min_val or points[i][j] > max_val:
				velocities[i][j] = -1.0*velocities[i][j]
			points[i][j] += velocities[i][j]*timestep
	for p in range(points.shape[1]):
		for q in range(points.shape[1]):
			if p < q:
				dist = euclid_distance_2d(points[:, p], points[:, q])
				distances.append(dist)


	axs[0].scatter(*points, c='blue', s=100)
	# Scatter plot
	axs[0].set_title('Particles')
	axs[0].set_xlabel('X-axis')
	axs[0].set_ylabel('Y-axis')
	axs[0].set_xlim((x_min, x_max))
	axs[0].set_ylim((y_min, y_max))

	# Histogram
	axs[1].hist(distances, bins=20, alpha=0.7, label='X-axis', color='blue')
	axs[1].set_title('Pairwise Distance Distribution')
	axs[1].set_xlabel('Distance')
	axs[1].set_ylabel('Frequency')

	camera.snap()
anim = camera.animate(blit=True)
anim.save('004_pairwise_distances.gif')
