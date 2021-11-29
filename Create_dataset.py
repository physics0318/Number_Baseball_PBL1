import numpy as np

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
