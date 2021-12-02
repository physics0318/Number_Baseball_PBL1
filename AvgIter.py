import Baseball동국
import Baseball수학
import math
import matplotlib.pyplot as plt
import time

ptime = time.time()
score = []
s = 0
V = 0
nums = [i for i in range(10)]
iter = 10000

# for i in nums:
#     for j in nums:
#         for k in nums:
#             for l in nums:
#                 if i!=j and i!=k and i!=l and j!=k and j!=l and l!=k:
for i in range(iter):
    b = Baseball수학.guess()
    Dgu = Baseball동국.Dongguk()
    #b.iter = 0
    # b.index = [j for j in range(5040)]

    while Dgu.strike < 4:
        num = b.guess()
        print(num)
        Dgu.evaluate(num)
        b.eliminate(num, Dgu.strike, Dgu.ball)
    
    score.append(Dgu.iteration)
    s += Dgu.iteration
ctime=time.time()
T = ctime-ptime

avg = s/iter
for i in score:
    V += (avg - i)**2
d = math.sqrt(V/iter)
print("average: %f, standard deviation: %f, time: %f"%(avg, d, T))

bin = max(score)-min(score)

(n, bins, patches) = plt.hist(score, bins=bin, align='left')
x = [i for i in range(min(score),max(score))]
y = n
for i, v in enumerate(x):
    plt.text(v, y[i], int(y[i]), horizontalalignment='center', verticalalignment='bottom', fontsize=8)
plt.xlabel('iteration')
plt.text(0.5, max(y), "average: %f, standard deviation: %f, time: %f"%(avg, d, T), fontsize=6)
plt.title('Dgu-random, Mth-not random')
plt.show()