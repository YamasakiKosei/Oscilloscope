import matplotlib.pyplot as plt
import numpy as np
import math

'''
発信周波数がわかっている
ダイヤルを調整した　　　　
計測【前】　　　　　　　　　のとき

理想の波形　
理想の計測値　を出力する

指定のDIV数(1周期のDIV数が8以内)で表示できるか
シミュレーションする
'''


f = input('周波数 = ') # 発信周波数
print('\n')
# アッテネータ比
attenuator = float(input('アッテネータ比 = 1：'))
print('\n')
volts_div = input('VOLTS/DIV = ') # VOLTS/DIV
time_div = input('TIME/DIV = ') # SEC/DIV
print('\n')
vertical = float(input('ピーク・デイップ間のDIV数 = ')) 
#print('ピーク・デイップ間のDIV数 =' + str(vertical) + 'のとき')
print('\n')



print('周波数 =', f, '[Hz]')
k = list(f)
if k[-1] == 'k' :
	k.pop(-1)
	f2 = float(''.join(k)) * 1000
	print('　　　 =', f2, '[Hz]')
else :
	f2 = float(f)

print('VOLTS/DIV =', volts_div, '[V]')
l = list(volts_div)
if l[-1] == 'm' :
	l.pop(-1)
	volts_div2 = float(''.join(l)) / 1000
	print('　　　　　　=', volts_div2, '[V]')
else :
	volts_div2 = float(volts_div)

print('TIME/DIV =', time_div, '[s]')
j = list(time_div)
if j[-1] == 'm' :
	j.pop(-1)
	time_div2 = float(''.join(j)) / 1000
	print('　　 　   =', format(time_div2, '.8f').rstrip('0'), '[s]')
elif j[-1] == 'μ' :
	j.pop(-1)
	time_div2 = float(''.join(j)) / 1000000
	print('　　 　   =', format(time_div2, '.8f').rstrip('0'), '[s]')
else :
	time_div2 = float(time_div)



t = 1 / f2
d = t / time_div2
if 1 <= d and d <= 8 :
	q = '　〇'
else:
	q = '　×'
print('\n')
print('1周期のDIV数 =', d, q)



print('\n')
v_pp = volts_div2 * attenuator  * vertical
print('Vp-p =', v_pp, '[V]')
print('　　　=', v_pp * 1000, '[mV]')

print('\n')
vm = v_pp / 2
print('Vm =', vm, '[V]')
print('　　=', vm * 1000, '[mV]')

print('\n')
print('T =', format(t, '.8f').rstrip('0'), '[s]')
print('　=', t * 1000, '[ms]')
print('　=', t * 1000000, '[μs]' )

print('\n')
ve = vm / math.sqrt(2)
print('理想の計測値 =', format(ve, '.5f'), '[V]')
print('　　　　　　 =', format(ve * 1000, '.2f'), '[mV]')




w = 2 * np.pi * f2 # 角周波数

d = t # 周期

d2 = str(format(d, '.8f')).split('.')
d3 = d2[-1].strip('0')
d4 = float(list(d3)[0])
d5 = d / (10 * d4) # 計測間隔

range = [-5*time_div2, 5*time_div2+d5] # 範囲

t = np.arange(range[0], range[1], d5) # 周期（配列）

y = vm * np.sin(w * t + 0)


plt.plot(t, y)
plt.xlabel('T[s]')
plt.ylabel('V[V]')
plt.xticks(np.arange(range[0], range[1], time_div2)) # TIME/DIV
plt.yticks(np.arange(-2*vm, 2.1*vm, volts_div2*attenuator))
plt.axvline(x = 0, color = 'k')
plt.axvline(x = 5*time_div2, color = 'k')
plt.axvline(x = -5*time_div2, color = 'k')
plt.axhline(y = 0, color = 'k')
plt.grid()
plt.show()