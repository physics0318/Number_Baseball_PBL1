import random
import numpy as np

def switch(l,a,b):      #두 숫자의 위치를 바꿈
    x, y = l[a], l[b]
    l[b] = x
    l[a] = y
    return l

def change(l,*args):    #리스트에 없는 다른 숫자로 바꿈
    n = random.sample([i for i in range(10) if i not in l], len(args))
    for i in range(len(args)):
        l[args[i]] = n[i]
    return l

total = []
li = []
for h in range(10):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if h!=i and h!=j and h!=k and i!=j and i!=k and j!=k:
                    total.append([h,i,j,k])

D = []
for i in total:
    sb = []
    for j in total:
        s = 0
        b = 0
        for n in range(4):
            if i[n] == j[n]:
                s += 1
            elif i[n] in j:
                b += 1
        sb.append([s, b])
    D.append(sb)
Data = np.array(D)
np.save("strike_ball_datasets",Data)
