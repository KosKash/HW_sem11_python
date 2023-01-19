import numpy as np
import matplotlib.pyplot as plt



limit = 50
step = 0.01
in_hi = True
color = 'r'
line_style = '-.'

x_ch = {-limit: 'inc'}

x = np.arange(-limit, limit, step)

a,b,c,d,e = -12, -18, 5, 10, -30

def f(x):
    return a*(x ** 4) * np.sin(np.cos(x)) + b*(x ** 3) + c*(x**2) + d*x + e


def switch_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color

def switch_line():
    global line_style
    if line_style == '-':
        line_style = '-.'
    else:
        line_style = '-'
    return line_style

x_min = -limit
f_min = f(-limit)

for x_cur in x:
    if f(x_cur) < f_min:
        f_min = np.round(f(x_cur),2)
        x_min = np.round(x_cur,2)
# print(x_min, f_min)

for i in range(len(x)-1):
    if f(x[i])>0 and f(x[i+1])<0 or (f(x[i])<0 and f(x[i+1])>0):
        x_ch[x[i]] = 'zero'
    if in_hi:
        if f(x[i]) > f(x[i+1]):
            in_hi = False
            x_ch[x[i]] = 'inc'
    else:
        if f(x[i]) < f(x[i+1]):
            in_hi = True
            x_ch[x[i]] = 'inc'

x_ch[limit] = 'inc'
# print(x_ch)

x_keys = [x for x in x_ch]
x_keys.sort()
# print(x_keys)

for i in range(len(x_keys)-1):
    x_cur = np.arange(x_keys[i], x_keys[i+1] + step, step)
    if x_ch.get(x_keys[i]) == 'zero':
        switch_line()
    else:
        switch_color()
    plt.rcParams['lines.linestyle'] = line_style
    plt.plot(x_cur, f(x_cur), color)


root = []
for i in range(len(x)-1):
    if f(x[i])>0 and f(x[i+1])<0 or (f(x[i])<0 and f(x[i+1])>0):
        root.append(x[i])
for i in range(len(root)):
    plt.plot(root[i],0, 'rx')


    
plt.title('Функция')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')



plt.show()
