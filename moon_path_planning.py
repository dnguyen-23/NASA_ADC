import csv, os, math
import numpy as np
import matplotlib.pyplot as plt


# #linux
# #height_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File HEIGHT.csv"
# #latitude_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File LATITUDE.csv"
# #longitude_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File LONGITUDE.csv"


#windows
height_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_height.csv"
latitude_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_latitude.csv"
longitude_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_longitude.csv"
slope_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_slope.csv"

#put csv into readable object stuff
# height_reader = list(csv.reader(open(height_file), delimiter=','))
# latitude_reader = list(csv.reader(open(latitude_file), delimiter=','))
# longitude_reader = list(csv.reader(open(longitude_file), delimiter=','))

x = np.genfromtxt(longitude_file, delimiter=',', dtype=None)
y = np.genfromtxt(latitude_file, delimiter=',', dtype=None)

radius = 1737.4
X = np.cos(np.deg2rad(y)) * np.cos(np.deg2rad(x)) * radius
Y = np.cos(np.deg2rad(y)) * np.sin(np.deg2rad(x)) * radius

z = np.genfromtxt(slope_file, delimiter=',', dtype=None)
# z = np.genfromtxt(height_file, delimiter=',', dtype=None)
# X, Y = np.meshgrid(x, y)
# z = griddata((x, y), height_reader, (X, Y))
for row in range(1277):
    for col in range(1277):
        if (z[row][col] < 15):
            z[row][col] = 100 
plt.scatter(X, Y, 1, z.flatten())
plt.xlabel('longitude')
plt.ylabel('latitude')

plt.show()










# verts = []
# # edges = []
# # faces = []

# # creating vertices/points on mesh
# # x_init = float(longitude_reader[0][0])
# #x_scale = 100
# # x_max = float(max(list(map(max, longitude_reader))))

# # y_init = float(latitude_reader[0][0])
# #y_scale = 10000
# # y_max = float(max(list(map(max, latitude_reader))))

# #crater is literally at the south pole
# #have to plot using polar coordinate system except angles are different in gps
# #think of physics ramps; longitude tells you the angle from the axis, 

# #sin theta = y and cos theta = x; 
# #multiply by lat = hyp

# dim = 1277 #equal to the number of rows and the number of cols because the data is a square
# for rowIdx, uselessRowElem in enumerate(height_reader[0: dim]):
#     for colIdx, uselessColElem in enumerate(uselessRowElem):
# #        rowIdx = 0
#         long = float(longitude_reader[rowIdx][colIdx])
#         lat = float(latitude_reader[rowIdx][colIdx])
#         z = float(height_reader[rowIdx][colIdx])
#     #        vert = ((float(x) + x_init), (float(y) + 88) * 40, float(z) / 10)
#     #        vert = (rowIdx, colIdx, float(z) / 10)
#         latitudeAngle = (lat + 90) * math.pi / 180
#         hypotenuseDistance = 1.7374 * 10**6 * 2 * math.sin(latitudeAngle) / 2 / math.pi
#         coordAngle = (90 - long) * math.pi / 180
#         x = hypotenuseDistance * math.cos(coordAngle) 
#         y = hypotenuseDistance * math.sin(coordAngle)
        
#         curVertIdx = colIdx + 1277 * rowIdx
#         # if ((rowIdx != dim - 1) and (colIdx != dim - 1)): #order of vertices matters; vertices have to go in order and cannot skip diagonally
#         #     faces.append([curVertIdx, curVertIdx + 1, curVertIdx + 1277 + 1, curVertIdx + 1277]) 
#         #     edges.append([curVertIdx, curVertIdx + 1])
#         #     edges.append([curVertIdx, curVertIdx + 1277])
        
#         # if ((colIdx == dim - 1) and (rowIdx != dim - 1)): #meaning that you are at the last column
#         #     edges.append([curVertIdx, curVertIdx + 1277])
#         # if ((rowIdx == dim - 1) and (colIdx != dim - 1)):
#         #     edges.append([curVertIdx, curVertIdx + 1])    
            
#         vert = (x, y, z)
#         verts.append(vert)