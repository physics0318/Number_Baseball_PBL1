import Baseball동국
import Baseball수학
import math
import matplotlib.pyplot as plt

score = []
s = 0
V = 0
iter = 10000

for i in range(iter):
    Dgu = Baseball동국.Dongguk()
    b = Baseball수학.guess()

    while Dgu.strike < 4:
        num = b.randGuess()
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

bin = max(score)-min(score)+1

plt.hist(score, bins=bin)
plt.show()