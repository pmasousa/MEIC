import numpy as np
import time

A = np.random.rand(1000,1)
B = np.random.rand(1000,1)
C = np.zeros((1000,1))

time1 = time.time()

for el,i in enumerate(A):
    C[el] = A[el] + B[el]
    
time2 = time.time() - time1

time1 = time.time()

C = A + B

time3 = time.time() - time1

print("Time with loop (in seconds):", time2)
print("Time with numpy operation (in seconds):", time3)


import numpy as np
import math


p0 = -math.pi/3 + 0.6
v0 = 0
P1 = np.zeros(1000)
V1 = np.zeros(1000)

def u(t):
    return 1;

def v(t):
    if t == 0:
        return v0
    vT1 = V1[t-1] - 1/400 * math.cos(3*P1[t-1]) + u(t-1)/1000
    return vT1

def p(t):
    if t == 0:
        return p0
    pT1 = P1[t-1] + V1[t]
    return pT1

for i in range(1000):
    V1[i] = v(i)
    P1[i] = p(i)

print("Final position:", P1[-1])
print("Final velocity:", V1[-1])

import numpy as np
import math


p0 = -math.pi/3 + 0.6
v0 = 0
P2 = np.zeros(1000)
V2 = np.zeros(1000)

def u(t):
    return np.random.choice([1,0,-1], p=[0.7,0.2,0.1]);

def v(t):
    if t == 0:
        return v0
    vT1 = V2[t-1] - 1/400 * math.cos(3*P2[t-1]) + u(t-1)/1000
    return vT1

def p(t):
    if t == 0:
        return p0
    pT1 = P2[t-1] + V2[t]
    return pT1

for i in range(1000):
    V2[i] = v(i)
    P2[i] = p(i)

print("Final position:", P2[-1])
print("Final velocity:", V2[-1])

import numpy as np
import math

p0 = -math.pi/3 + 0.6
v0 = 0
P3 = np.zeros(1000)
V3 = np.zeros(1000)

def u(t):
    if P3[t] >= -0.85:
        return -1
    return 1;

def v(t):
    if t == 0:
        return v0
    vT1 = V3[t-1] - 1/400 * math.cos(3*P3[t-1]) + u(t-1)/1000
    return vT1

def p(t):
    if t == 0:
        return p0
    pT1 = P3[t-1] + V3[t]
    return pT1

for i in range(1000):
    V3[i] = v(i)
    P3[i] = p(i)

print("Final position:", P3[-1])
print("Final velocity:", V3[-1])

import matplotlib.pyplot as plt

plt.figure()
plt.plot(P1)
plt.plot(P2)
plt.plot(P3)

plt.xlabel('Time');
plt.ylabel('Position');

plt.legend(['U constant','U varying', 'U = -1 if P > -0.85 else +1'])

plt.title('Mountain car problem');
plt.show()


