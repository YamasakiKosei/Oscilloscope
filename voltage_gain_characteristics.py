import numpy as np
import math

f = float(input('周波数 = '))

vi = 3 # Vi

r1 = 10000
r2 = 1000
c = 0.015 / 1000000

# コンデンサのインピーダンス
rc = 1 / (2 * np.pi * f * c)

vo = vi * rc / (r1 + rc) # Vo

db = 20 * math.log10(vo/vi)

print(db, 'dB')