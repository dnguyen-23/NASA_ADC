import matplotlib.pyplot as plt
import numpy as np
import csv
import math

height_file = "/home/danielnguyen/NASA_ADC/NASA_ADC_height.csv"
latitude_file = "/home/danielnguyen/NASA_ADC/NASA_ADC_latitude.csv"
longitude_file = "/home/danielnguyen/NASA_ADC/NASA_ADC_longitude.csv"

# height_reader = list(csv.reader(open(height_file), delimiter=','))
# latitude_reader = list(csv.reader(open(latitude_file), delimiter=','))
# longitude_reader = list(csv.reader(open(longitude_file), delimiter=','))

height = np.genfromtxt(height_file, delimiter=',', dtype=None)
latitude = np.genfromtxt(latitude_file, delimiter=',', dtype=None)
longitude = np.genfromtxt(longitude_file, delimiter=',', dtype=None)
def graph(x, y, z):
    plt.scatter(x,y,1,z)
    plt.colorbar(label='Elevation above sea level [m]')
    plt.xlabel('Longitude [°]')
    plt.ylabel('Latitude [°]')
    plt.show()

radius = 1737.4 * 10**3 #put everything in meters
height = height.flatten()
latitude = latitude.flatten()
longitude = longitude.flatten()
x = []
y = []
z = []

for i in range(len(height)):
    x.append(radius * math.cos(math.radians(latitude[i])) * math.cos(math.radians(longitude[i])))
    y.append(radius * math.cos(math.radians(latitude[i])) * math.sin(math.radians(longitude[i])))
    z.append(radius * math.sin(math.radians(latitude[i])))
    # z.append(height[i])

graph(x, y, z)

