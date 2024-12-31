import matplotlib.pyplot as plt
import numpy as np
import math

'''
振幅 A
周波数 f
位相差
'''


a1 = 1 # 振幅
a2 = 1 

f1 = 60 # 周波数
f2 = 60

w1 = 2 * np.pi * f1 # 角周波数
w2 = 2 * np.pi * f2 


t = np.arange(0, 0.021, 0.001) # 時間（横軸）



x = a1 * np.sin(w1 * t) # 縦軸


g = 0 # 位相差[°]

r = g * np.pi / 180 # ラジアン

y = a2 * np.sin(w2 * t + r) # 縦軸





Figure = plt.figure() #全体のグラフを作成
ax1 = Figure.add_subplot(2,2,1) #1つ目のAxを作成
ax2 = Figure.add_subplot(2,2,2) #2つ目のAxを作成
ax3 = Figure.add_subplot(2,2,3) #3つ目のAxを作成
ax4 = Figure.add_subplot(2,2,4) #4つ目のAxを作成

ax1.plot(x, y, color='purple', label='Lissage')
ax2.plot(t, x, color='red', label='sin')
ax3.plot(t, y, color='blue', label= 'sin - ' +str(g) + '°')
ax4.plot(t, x, color='red', label='sin')
ax4.plot(t, y, color='blue', label='sin - ' +str(g) + '°')

ax1.legend(loc = 'upper right')
ax2.legend(loc = 'upper right')
ax3.legend(loc = 'upper right')
ax4.legend(loc = 'upper right')

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

plt.show()