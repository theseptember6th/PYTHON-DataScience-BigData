"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/22/2024
PURPOSE:Data Communication lab1
"""

import numpy as np
import matplotlib.pyplot as plt
#for increasing exponential continuous
a=1
t=np.arange(-6,6,1)
y=np.exp(a*t)
plt.suptitle("Exponential graph")
plt.subplot(2,2,1)
plt.xlabel('time')
plt.ylabel("x(t)")
plt.axhline(y=0,color='k')
plt.axvline(x=0,color='k')
plt.title("continuous increasing exponential")
plt.plot(t,y)


#for decreasing exponential continuous

a=-1
t=np.arange(-6,6,1)
y=np.exp(a*t)
plt.subplot(2,2,2)
plt.xlabel("time")
plt.ylabel("x(t)")
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')
plt.title("continuous decreasing exponential")
plt.plot(t,y)


#for increasing exponential signal discrete
a=1
t=np.arange(-6,6,1)
y=np.exp(a*t)
plt.subplot(2,2,3)
plt.xlabel("n")
plt.ylabel("x(n)")
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')
plt.title("increasing exponential discrete")
plt.stem(t,y)


#for decreasing exponential discrete
a=-1
t=np.arange(-6,6,1)
y=np.exp(a*t)
plt.subplot(2,2,4)
plt.xlabel("n")
plt.ylabel("x[n]")
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')
plt.title("decreasing exponential discrete")
plt.stem(t,y)


plt.tight_layout()
plt.show()