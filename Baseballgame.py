import Baseball동국
import Baseball수학

givenumber = input("숫자를 입력하시오: ")
Dgu = Baseball동국.Dongguk(givenumber)
b = Baseball수학.guess()

# print(b.total.index(list(map(int, givenumber))))

while Dgu.strike < 4:
    num = b.randGuess()
    print(num)
    Dgu.evaluate(num)
    b.eliminate(num, Dgu.strike, Dgu.ball)


