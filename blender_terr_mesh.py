# import bpy, bmesh
import csv, os, math

# filepath = bpy.data.filepath
# directory = os.path.dirname(filepath)

verts = []

height_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File HEIGHT.csv"
latitude_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File LATITUDE.csv"
longitude_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File LONGITUDE.csv"

#put csv into readable object stuff
height_reader = list(csv.reader(open(height_file), delimiter=','))
latitude_reader = list(csv.reader(open(latitude_file), delimiter=','))
longitude_reader = list(csv.reader(open(longitude_file), delimiter=','))

x_init = float(longitude_reader[0][0])
y_init = float(latitude_reader[0][0])

# creating vertices/points on mesh
for rowIdx, uselessRowElem in enumerate(height_reader):
    for colIdx, uselessColElem in enumerate(uselessRowElem):
        x = longitude_reader[rowIdx][colIdx]
        y = latitude_reader[rowIdx][colIdx]
        z = height_reader[rowIdx][colIdx]
        vert = ((float(x) - x_init) * 100, (float(y) - y_init) * 10000, float(z))
        verts.append(vert)
for i in range(10):
    print(verts[i])