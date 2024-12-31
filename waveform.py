import matplotlib.pyplot as plt
import numpy as np

vm = 10 / 1000 # 最大値

f = 30000 # 周波数

o = 180.5 # 位相

w = 2 * np.pi * f

d = 1 / f

d2 = str(format(d, '.8f')).split('.')
d3 = d2[-1].strip('0')
d4 = float(list(d3)[0])
d5 = d / (10 * d4)

t = np.arange(0, 2/f, d5)

y = vm * np.sin(w * t + o)


plt.plot(t, y)
plt.xlabel('T[s]')
plt.ylabel('V[V]')
plt.xticks(np.arange(0, 2/f, 20/1000000)) # TIME/DIV
plt.grid()
plt.show()