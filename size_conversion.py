import matplotlib.pyplot as plt
import numpy as np
import math

'''
周波数がわかっている
電圧の最大値がわかっている　とき

ちょうどいいダイヤル位置とDIV数　を出力する
'''


f = input('周波数 = ') # 発信周波数
print('\n')
waveform = input('波形 = ') # 全波・半波
print('\n')
vm = input('Vm = ') # 電圧の最大値
print('\n')
# アッテネータ比
attenuator = float(input('アッテネータ比 = 1：'))
print('\n')

#volts_div = input('VOLTS/DIV = ') # VOLTS/DIV
#time_div = input('TIME/DIV = ') # SEC/DIV
volts_div = [0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10]
time_div = [0.0000001, 0.0000002, 0.0000005, 0.000001, 0.000002, 0.000005, 0.00001, 0.00002, 0.00005, 0.0001, 0.0002, 0.0005, 0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2]



print('周波数 =', f, '[Hz]')
k = list(f)
if k[-1] == 'k' :
	k.pop(-1)
	f2 = float(''.join(k)) * 1000
	print('　　　 =', f2, '[Hz]')
else :
	f2 = float(f)
	
print('Vm =', vm, '[V]')
h = list(vm)
if h[-1] == 'm' :
	h.pop(-1)
	vm = float(''.join(h)) / 1000
	print('　　　　　　=', vm2, '[V]')
else :
	vm = float(vm)



def conversion_v(v):
	if v < 0.1:
		n = v * 1000
		n = f'{n:4.01f}'
		return str(n) + ' [mV]'
	else:
		n = v
		n = f'{n:4.01f}'
		return str(n) + '  [V]'

def conversion_s(s):
	if s < 0.0001:
		n = s * 1000000
		n = f'{n:4.01f}'
		return str(n)+ ' [μs]'
	elif 0.0001 <= s and s < 0.1:
		n = s * 1000
		n = f'{n:4.01f}'
		return str(n)+ ' [ms]'
	else:
		n = s
		n = f'{n:4.01f}'
		return str(n)+ '  [s]'



if waveform == '全波' or waveform == '半波':
	h = 1
	m = 4
else:
	h = 2
	m = 8


volts_div_list = []
vertical_list= []
# ピーク・デイップ間のDIV数
print('\n')
print('○ピーク・デイップ間のDIV数')
v_pp = h * vm
for i in volts_div:
	vertical = v_pp / (i * attenuator)
	if 1 <= vertical and vertical < m:
		volts_div_list.append(i)
		vertical_list.append(float(format(vertical, '4.01f')))
		print('VOLTS/DIV =', conversion_v(i), f'{vertical:4.02f}', 'DIV')

time_div_list = []
beside_list = []
# 1周期のDIV数
print('\n')
print('○1周期のDIV数')
t = 1 / f2
for l in time_div:
	beside = t / l
	if 1 <= beside and beside < 10:
		time_div_list.append(l)
		beside_list.append(float(format(beside, '4.01f')))
		tt = format(10 / float(beside), '.01f')
		print('TIME/DIV  =', conversion_s(l), f'{beside:4.02f}', 'DIV ', tt, '周期')







print('\n' * 5)

'''
print('Vp-p = VOLTS/DIV × アッテネータ比 × ピーク・デイップ間のDIV数')
print('　　　= ' + str(conversion_v(volts_div_list[0]))) + ' × ' + str(attenuator) + ' × ' + str(vertical_list[0])
v_pp
print('     = ' + )
'''


number = 0

time_div2 = time_div_list[number]
volts_div2 = volts_div_list[number]
beside = beside_list[number]



t = time_div2 * beside
f = 1 / t

w = 2 * np.pi * f # 角周波数
d = t # 周期

d2 = str(format(d, '.8f')).split('.')
d3 = d2[-1].strip('0')
d4 = float(list(d3)[0])
d5 = d / (10 * d4)

range = [-6*time_div2, 6*time_div2+d5] # 範囲

t = np.arange(range[0], range[1], d5) # 周期（配列）

y = []
list = vm * np.sin(w * t + 0)
if waveform == '全波':
	for i in list:
		if i < 0:
			i = math.fabs(i)
		y.append(i)
elif waveform == '半波':
	for i in list:
		if i < 0:
			i = 0
		y.append(i)	
else:
	y = list
	


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