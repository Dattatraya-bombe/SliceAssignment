#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Install numpy-stl library
import numpy
get_ipython().system('pip3 install numpy-stl')


# ### Q.1)

# In[6]:


import numpy as np
from stl import mesh
import sys
import math

# Read the stl file
create_mesh = mesh.Mesh.from_file('assignment.STL.stl')
info = create_mesh.__dict__["data"] #extract datatypes(normals, triangle coordinates) from mesh

#create array of vertices of triangles v0,v1 and v2 and concatenate into single array
v0=create_mesh.v0
v1=create_mesh.v1
v2=create_mesh.v2
vertices = np.concatenate((v0,v1,v2),axis=0)

#for defining slicing plane dimension calculate the length and width of the object
#slicing plane dimensions should be greater than limit values
xmin = sys.float_info.max
ymin = sys.float_info.max
xmax = sys.float_info.min
ymax = sys.float_info.min
for vertice in vertices:
    xmin = min(xmin, vertice[0])
    ymin = min(ymin, vertice[1])
    xmax = max(xmax, vertice[0])
    ymax = max(ymax, vertice[1])

print('xmax=',xmax, 'xmin=',xmin,'ymax=', ymax,'ymin=', ymin)

#find the intersection vertices of triangle facets with slicing plane
def filterPoints(z, vertices):
    points=[]
    for vertice in vertices:
        if math.isclose(vertice[2], z, rel_tol=1e-8):
            if -5<vertice[0]<75 and -5<vertice[1]<75:
                points.append(vertice)
    return points

intersect = filterPoints(34.236008, vertices)
print('intersect vertices=',np.array(intersect))


# In[ ]:




