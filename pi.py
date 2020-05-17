from __future__ import unicode_literals
from __future__ import division
from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt

##############################################################
# pi.py AKA very easy monte-carlo /
# monte-carlo-coding example for demonstration
# by kai benning (march 2018)
##############################################################

def circle_function(radius):
    x = np.linspace(0,radius,1e6)
    y = np.zeros(np.size(x))
    for index,x_val in enumerate(x):
        y[index] = np.sqrt(radius**2 - x_val**2)
    return x,y

#get random points in x,y
#type in number of points:

length_of_sample = 1e3
length_of_sample = int(length_of_sample)
#np.random.seed()
x_coord = np.random.uniform(low=0, high=1, size=(length_of_sample,))
y_coord = np.random.uniform(low=0, high=1, size=(length_of_sample,))
radius = 1

#draw the random points
plt.scatter(x_coord,y_coord,label = "random dots")

#draw circle
x_circle,y_circle = circle_function(radius)
plt.plot(x_circle,y_circle,color = "r",label = "circle")

#count point inside circle
inside_circle_counter = 0
for x_index,x_val in enumerate(x_coord):
    if x_val**2 + y_coord[x_index]**2 <= radius**2:
        inside_circle_counter += 1

#estimate pi
pi_approx = inside_circle_counter/length_of_sample*4

#compare with np.pi
accordance = (np.pi - abs(np.pi - pi_approx)) / np.pi * 100

print("")
print("points inside circle:")
print(inside_circle_counter)
print("points in total:")
print(length_of_sample)
print("so pi_approx is calculated as follows:")
print("pi_monte_carlo = inside / total * 4:")
print(pi_approx)
print("accordance with build_in pi value:")
print(np.round(accordance,3),"%")
print("build_in pi:")
print(np.pi)
print("")

plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("x-values")
plt.ylabel("y-values")
plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1), ncol=2)
plt.gca().set_aspect('equal', adjustable='box')
plt.tight_layout()
plt.show()
