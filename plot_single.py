from locale import ABMON_10
import matplotlib.pyplot as plt
import numpy as np

def c(t: np.ndarray):
    return i * np.power((r1 / (1 + np.exp(a1 - b1 * t))), j) * np.power((r2 / (1 + np.exp(a2 - b2 * t))), k) * wd * cf


plt.figure(figsize=(10, 5))
t0 = 14
t1 = np.linspace(0, 100, 100)
t2 = np.linspace(t0, 100, 100 - t0)
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
y1 = c(t1)
kk = np.log(2) / 35
y2 = c(t2 - t0) + c(t0) * np.exp(-kk * (t2 - t0)) * (1 - np.exp(-kk)) / kk
plt.plot(t1, y1, linewidth = 2, label = "No Deforestation")
plt.plot(t2, c(t2- t0), linewidth = 0.5)
plt.plot(t2, (y2 - c(t2 - t0)), linewidth = 0.5)
plt.plot(t2, y2, linewidth = 2, label = "Planting After Deforestation")
plt.legend()
plt.xlabel('Time / Year')
plt.ylabel('Carbon Storage / Mt')
plt.show()