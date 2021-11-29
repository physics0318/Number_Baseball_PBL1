import random

class guess():
    def __init__(self):
        self.history = []                                               #[지금까지 추측한 답, 스트라이크, 볼]형태의 데이터
        self.numbers = [list(i for i in range(10)) for j in range(4)]   #각 자릿수에 올 수 있는 숫자들을 정리한 2차원 배열.
        self.iter = 0                                                   #문답한 횟수
        self.must = []

    def eliminate(self, l, strike, ball):                               #strike, ball의 입력에 따라 각 자릿수에 올만한 숫자를 정리하는 함수
        self.history.append([l,strike,ball])                            #과거에 했던 대답과 그에 따른 strike, ball을 기억
        if self.iter == 2:
            sum = 0
            for i in self.history:
                sum += i[1]+i[2]
            if sum == 4:
                for j in self.numbers:
                    if 8 in j:
                        j.remove(8)
                    if 9 in j:
                        j.remove(9)
            elif sum == 5:
                self.must.append(8)
                self.must.append(9)
        
        if strike == 4:
            return
        if strike == 0:                                                 #strike가 0일 경우
            for i in range(4):
                if l[i] in self.numbers[i]:                             #그 자릿수에 올만한 숫자들에서 방금 찍었던 답과 같은자리의 숫자를 제거
                    self.numbers[i].remove(l[i])

        if strike + ball == 0:                                          #s+b = 0 이면  
            for i in range(4):
                for j in l:
                    if j in self.numbers[i]:
                        self.numbers[i].remove(j)                       #그 자릿수에 올만한 숫자들중 방금 찍었던 답에있는 숫자를 모두 제거

        if strike + ball == 4:                                          #s+b = 4 이면
            for i in range(4):
                for j in self.numbers[i]:                                     #방금 찍었던 답안의 숫자들만 사용
                    if j not in l:
                        self.numbers[i].remove(j)

    def randGuess(self):
        self.iter += 1
        if self.iter == 1:
            return [0,1,2,3]
        elif self.iter == 2:
            return [4,5,6,7]
        else:
            l = []
            while len(l)<4:
                for i in self.numbers:
                    n = random.choice(i)
                    if n in l:
                        l=[]
                        break
                    else:
                        l.append(n)

                if len(l) == 4:
                    for i in self.must:
                        if i not in l:
                            l=[]
                            break
                    for i in self.history:
                        cnt = 0
                        for j in range(4):
                            if l[j] == i[0][j]:
                                cnt += 1
                        if cnt != i[1]:
                            l=[]
                            break
                    for i in self.history:                              #과거 기록을 참고하여 랜덤으로 뽑을 숫자를 한정 (예: [1,2,3,4]가 0s 2b였다면 1~4중에서는 2개만 뽑도록 함)
                        cnt = 0
                        for j in l:
                            if j in i[0]:
                                cnt += 1
                        if cnt != i[1]+i[2]:
                            l=[]
                            break
                
                if len(l) > 4:                                          #리스트 원소 개수가 5개 이상이 되는 것을 방지.
                    l = []
                    continue
            return l

if __name__ == '__main__':
    b = guess()
    b.guess
