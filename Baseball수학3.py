import random

class observe():
    def __init__(self):
        self.check = [0,1,2,3]
        self.iter = 0
        self.distrib = [0,0,0,0,0,0,0,0,0,0]

    def cycle(self):
        for i in range(4):
            self.check[i] += 1
            if self.check[i] > 9:
                self.check[i] -= 10

    def update(self, strike, ball):
        self.iter += 1
        if strike + ball != 0:
            for i in self.check:
                self.distrib[i] += strike+ball
        self.cycle()

if __name__ == '__main__':
    b = observe()
    for i in range(10):
        print(b.guess())