import numpy as np
import math


a = 2.2
b = 4

r = np.arcsin(a / b) # ラジアン

g = r / np.pi * 180 # 位相差[°]

print(g)
