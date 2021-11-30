import Baseball동국
import Baseball수학
import math
import matplotlib.pyplot as plt

score = []
s = 0
V = 0
iter = 10000


for i in range(iter):
    b = Baseball수학.guess()
    Dgu = Baseball동국.Dongguk()
    print(Dgu.number)
    #b.iter = 0
    # b.index = [j for j in range(5040)]

    while Dgu.strike < 4:
        num = b.guess()
        print(num)
        Dgu.evaluate(num)
        b.eliminate(num, Dgu.strike, Dgu.ball)
    
    score.append(Dgu.iteration)
    s += Dgu.iteration

avg = s/iter
for i in score:
    V += (avg - i)**2
d = math.sqrt(V/iter)
print("average: %f, standard deviation: %f"%(avg, d))

bin = max(score)-min(score)

plt.hist(score, bins=bin)
plt.show()