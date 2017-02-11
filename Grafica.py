import numpy as np
import math as mt
from scipy import constants as cts
import matplotlib.pyplot as plt

#Read File

f=open("Data_Simulation.txt","r")
l=[]
L=[]
v=[]
P=[]
for x in f.readlines():
    m=x.split(" ")
    m=[y.rstrip() for y in m]
    m=[y.replace("\\"," ") for y in m]
    for z in m:
        try:
            l.append(float(z))
        except:
            pass
f.close()
plt.plot(l)
plt.show()
