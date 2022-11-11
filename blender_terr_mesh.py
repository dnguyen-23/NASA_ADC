import bpy, bmesh
import csv, os, math
import numpy as np
filepath = bpy.data.filepath
directory = os.path.dirname(filepath)

verts = []
edges = []
faces = []
#linux
#height_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File HEIGHT.csv"
#latitude_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File LATITUDE.csv"
#longitude_file = "/home/danielnguyen/NASA_ADC/FY20 ADC Regional Data File LONGITUDE.csv"


#windows
height_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_height.csv"
latitude_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_latitude.csv"
longitude_file = r"C:\Users\danie\NASA_ADC\NASA_ADC_longitude.csv"


#put csv into readable object stuff
height_reader = list(csv.reader(open(height_file), delimiter=','))
latitude_reader = list(csv.reader(open(latitude_file), delimiter=','))
longitude_reader = list(csv.reader(open(longitude_file), delimiter=','))

# creating vertices/points on mesh
x_init = float(longitude_reader[0][0])
#x_scale = 100
x_max = float(max(list(map(max, longitude_reader))))

y_init = float(latitude_reader[0][0])
#y_scale = 10000
y_max = float(max(list(map(max, latitude_reader))))

#crater is literally at the south pole
#have to plot using polar coordinate system except angles are different in gps
#think of physics ramps; longitude tells you the angle from the axis, 

#sin theta = y and cos theta = x; 
#multiply by lat = hyp

dim = 1277 #equal to the number of rows and the number of cols because the data is a square
for rowIdx, uselessRowElem in enumerate(height_reader[0: dim]):
    for colIdx, uselessColElem in enumerate(uselessRowElem):
#        rowIdx = 0
        long = float(longitude_reader[rowIdx][colIdx])
        lat = float(latitude_reader[rowIdx][colIdx])
        z = float(height_reader[rowIdx][colIdx])
        radius = 1.7374 * 10**6
        x = math.cos(lat * math.pi / 180) * math.cos(long * math.pi / 180) * radius
        y = math.cos(lat * math.pi / 180) * math.sin(long * math.pi / 180) * radius
        
        curVertIdx = colIdx + 1277 * rowIdx
        if ((rowIdx != dim - 1) and (colIdx != dim - 1)): #order of vertices matters; vertices have to go in order and cannot skip diagonally
            faces.append([curVertIdx, curVertIdx + 1, curVertIdx + 1277 + 1, curVertIdx + 1277]) 
            edges.append([curVertIdx, curVertIdx + 1])
            edges.append([curVertIdx, curVertIdx + 1277])
        
        if ((colIdx == dim - 1) and (rowIdx != dim - 1)): #meaning that you are at the last column
            edges.append([curVertIdx, curVertIdx + 1277])
        if ((rowIdx == dim - 1) and (colIdx != dim - 1)):
            edges.append([curVertIdx, curVertIdx + 1])    
            
        vert = (x, y, z)
        verts.append(vert)
mesh = bpy.data.meshes.new("wave")
obj = bpy.data.objects.new("wave",mesh)


mesh.from_pydata(verts,edges,faces)
mesh.update(calc_edges=True)

#set mesh location
bpy.context.scene.cursor.location = [0,0,0]
obj.location = bpy.context.scene.cursor.location
bpy.data.collections["Collection"].objects.link(obj)

