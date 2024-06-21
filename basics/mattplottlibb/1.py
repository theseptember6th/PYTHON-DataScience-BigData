"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/22/2024
PURPOSE:learning matplotlib
"""

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')
plt.plot([1,2,3],[2,5,7])
plt.title("KRISTAL GRAPH")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

x=[1,5,4]
y=[23,45,89]
x2=[3,7,3]
y2=[5,8,9]
plt.plot(x,y,label="Firstline",linewidth=4)
plt.plot(x2,y2,label="Secondline")
plt.legend()
plt.show()