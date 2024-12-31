import numpy as np
import math

g = 45 # 位相差[°]

r = g * np.pi / 180 # ラジアン

a_b = np.sin(r) # a/b



for a in range(1, 5):
	b = a / a_b
	print(str(a) + 'のとき：' + str(b))
