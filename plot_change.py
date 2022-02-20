from locale import ABMON_10
from turtle import shape
import matplotlib.pyplot as plt
import numpy as np

def c(t: np.ndarray):
    return i * np.power((r1 / (1 + np.exp(a1 - b1 * t))), j) * np.power((r2 / (1 + np.exp(a2 - b2 * t))), k) * wd * cf


plt.figure(figsize=(10, 5))
t0 = 10
dim = 300
t = np.linspace(0, dim, dim)
a1 = 1.60731
b1 = 0.30196
r1 = 27.4
a2 = 2.02546
b2 = 0.27923
r2 = 48.3
i = 5.000666e-5
j = 1.912099
k = 0.9363676
wd = 0.386 #t/m^3
cf = 0.44
kk = np.log(2) / 35
y = c(t0)
ii = t0
while ii <= dim: 
    y += (t >= ii) * c(t0) * np.exp(-kk * (t - ii)) * (1 - np.exp(-kk)) / kk
    y += (t >= ii) * c(t0)
    ii += t0
    if ii < dim / 2 and ii + t0 > dim / 2:
        t0 = 20
plt.plot(t, y)
plt.show()