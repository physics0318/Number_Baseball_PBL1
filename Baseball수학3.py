"""
과제
1. 어떤 자리에 들어가야하는지? s를 이용해서 자리수를 완벽히 찾을 수 있나?
"""

class observe():
    def __init__(self):
        self.iter = 1
        self.check = [0,1,2,3]
        self.pos = [0 for i in range(10)]
        self.s = []
        self.b = []

    def cycle(self):
        for i in range(4):
            self.check[i] += 1
            if self.check[i] > 9:
                self.check[i] -= 10
        self.iter += 1

    def update(self, strike, ball):
        if strike == 4:
            return
        if strike != 0:
            for i in range(4):
                self.pos[(self.check[0]+i)%10] += 10**i
        
        self.s.append(strike)
        self.b.append(strike+ball)
        self.cycle()

    def question(self):
        if self.iter == 10:
            self.calculate()
            return self.ans
        elif self.iter == 11:
            pass##############################################
        else:
            return self.check

    def calculate(self):
        self.update(4-sum(self.s),12-sum(self.b)+sum(self.s))
        
        #어떤 숫자가 들어가야할지를 s+b를 통해 알아내는 기능(구현완료)
        self.d = []
        for i in range(10):
            self.d.append(self.b[(4+i)%10]+self.b[(8+i)%10]+self.b[(0+i)%10])

        self.nums = []
        self.nonums = []
        for i in range(10):
            if self.d[i] == 6:
                self.nums.append(i)
                self.nums.append((i+1)%10)
            elif self.d[i] == 4:
                self.nonums.append(i)
                self.nonums.append((i+1)%10)
        for i in range(10):
            for j in range(10):
                if self.d[j] == 5 and (j+1)%10 in self.nums and j not in self.nonums:
                    self.nonums.append(j)
                elif self.d[j] == 5 and (j+1)%10 in self.nonums and j not in self.nums:
                    self.nums.append(j)
        print(self.nums)

        #어떤 자리에 들어가야되는지 판별하는 기능(미흡)
        l = [self.pos[i] for i in self.nums]
        ans = [[],[],[],[]]
        for i in range(4):
            for j in range(4):
                if l[j]//(10**i)%10 == 1:
                    ans[i].append(self.nums[j])
        print(ans)

        self.ans = [10,10,10,10]
        for i in ans:
            if len(i) > 0:
                self.decision(ans)

    def decision(self, ans):
        for i in range(4):
            if len(ans[i]) == 1:
                self.ans[i] = ans[i][0]
                for j in range(4):
                    if i != j:
                        if ans[i][0] in ans[j]:
                            ans[j].remove(ans[i][0])
        #수정필요
        for j in range(4):
            if len(ans[i]) > 1:
                self.ans[i] = ans[i][0]
                for j in range(4):
                    if i != j:
                        if ans[i][0] in ans[j]:
                            ans[j].remove(ans[i][0])

if __name__ == '__main__':
    b = observe()
    print(b.s)