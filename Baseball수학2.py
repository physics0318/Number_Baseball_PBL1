import numpy as np
import random

class guess():
    def __init__(self):
        self.iter = 0
        self.index = [i for i in range(5040)]

        Data = np.load('strike_ball_datasets.npy')
        self.Data = Data.tolist()

        self.total = []
        for h in range(10):
            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        if h!=i and h!=j and h!=k and i!=j and i!=k and j!=k:
                            self.total.append([h,i,j,k])

    def eliminate(self, l, s, b):
        index = self.total.index(l)
        self.index.remove(index)
        n = []
        for i in range(len(self.Data[index])):
            if self.Data[index][i] == [s, b]:
                n.append(i)
        for i in self.index:
            if i in n:
                pass
            else:
                self.index.remove(i)

    def guess(self):
        self.iter += 1
        if self.iter == 1:
            return [0,1,2,3]
        else:
            return self.total[random.choice(self.index)]

if __name__ == "__main__":
    b = guess()
    x = [3,2,5,7]
    y = [9,4,8,2]
    X = b.total.index(x)
    Y = b.total.index(y)
    print(b.Data[X][Y])
    print(b.Data[Y][X])
