import random   
class Dongguk:
    def __init__(self, giveNumber=None):#giveNumber는 list로 주어짐. 만약 주어지지 않는다면 랜덤으로 생성함.
        self.iteration = 0
        self.strike = 0
        self.ball = 0

        if giveNumber:#giveNumber가 주어졌다면 그것을 답으로 한다.
            self.number = list(map(int, giveNumber))
        else:  #giveNumber가 주어지지 않았다면 랜덤하게 답을 만든다.
            self.number = []
            while len(self.number) < 4:
                n = random.randint(0, 9)
                if n not in self.number:
                    self.number.append(n)

    def evaluate(self, list):
        self.iteration += 1
        self.strike = 0
        self.ball = 0
        for i in range(4):
            if list[i] == self.number[i]:
                self.strike += 1
            else:
                for j in range(4):
                    if i == j:
                        pass
                    elif list[i] == self.number[j]:
                        self.ball += 1
        if self.strike == 4:
            print("You are correct!")
        else:
            print('%s-th iteration: %s Strike %s Ball'%(self.iteration,self.strike,self.ball))

if __name__ == '__main__':
    Dgu = Dongguk()
    while Dgu.strike < 4:
        number = list(map(int, input("무엇: ")))
        Dgu.evaluate(number)
