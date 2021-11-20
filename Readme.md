# 전산응용수학 PBL1 - 숫자야구
## 숫자야구 규칙
다음은 숫자야구의 규칙이다.
- 동국이는 0-9사이의 수 중에서 4개를 중복없이 선택하여 배열한다.

- 수학이는 동국이가 생성한 수열을 예측하여 질문한다. 

- 동국이는 수학이의 질문을 받아서 평가하게 된다. 숫자와 위치를 모두 맞춘 개수만큼 스트라이크, 숫자를 맞췄지만 위치가 틀린 개수만큼 볼을 계산한다. 동국이는 스트라이크와 볼의 정보를 수학이에게 제공한다.

## 목표
큰 목표는 수학이를 프로그램으로 대체하는 것이다. 이 프로그램은 다음 2가지의 세부 목표를 바탕으로 만들어진다. 
- 적은 횟수로 정답을 맞춰야한다.
- 적은 시간으로 다음 질문을 판단해야한다.

## 사전 준비와 문제해결
문제를 해결하기 위해 우선 숫자야구 게임 자체를 프로그래밍으로 구현하였다. 크게 세 종류의 프로그램을 구현하였다.
1. 동국이와 수학이 사이의 정보 전달을 매개하는 프로그램
2. 동국이의 역할을 수행하는 모듈
3. 수학이의 역할을 수행하는 모듈

먼저 1번과 2번의 구현을 사전 준비과정으로 보고, 3번의 구현을 문제해결 과정으로 분류하였다. 

### 동국이와 수학이 사이의 정보 전달을 매개하는 프로그램(Baseballgame.py)
숫자야구 게임이 이뤄지는 경기장이다. 코드로 만들어낸 2개의 프로그램 동국이와 수학이 모듈을 임포트하여 서로 문답을 시키는 기능을 한다.

### 동국이의 역할을 수행하는 모듈(Baseball동국.py)
동국이는 문제를 내는 프로그램이다. 이 안에는 Dongguk이라는 클래스가 구현되어있다. Dongguk의 인스턴스가 생성될 때 0~9중 중복되지 않고 순서에 상관없이 4개의 숫자를 뽑아 리스트의 형태로 self.number라는 이름으로 저장한다. 

self.evaluate은 리스트 하나를 입력으로 받아서 strike와 ball을 계산한다. 이 각각의 값들은 self.strike, self.ball에 저장되며, 다음 질문을 받으면 값이 바뀐다.

### 수학이의 역할을 수행하는 모듈1(Baseball수학.py)
문제를 해결하기 위해 가장 먼저 생각해본 해결 방법이다. 기본적으로 가능한 답안 중에서 랜덤하게 선택해 질문을 던지는 기능이 self.randguess라는 함수에 구현되어있다. 
더 효율적인 정답을 찾기 위해 조금씩 살을 붙일 예정이다.

수학이는 과거에 했던 질문에 스트라이크(s)와 볼(b)이라는 정보를 받은 것을 바탕으로 앞으로 할 질문을 판단해야한다. 여기서 의미를 부여할 수 있는 것은 s와 s+b라고 생각했다. 

따라서 이 수학이는 클래스 guess를 가지고 있는데, 이 클래스의 인스턴스가 생성될 때 [[0-9],[0-9],[0-9],[0-9]]형태의 2차원 리스트를 self.numbers라는 이름으로 떠올리게 된다. 초기 상태는 각 자리에 0에서 9 모두 들어갈 수 있다는 의미를 가지고 있다. s와 s+b의 정보를 바탕으로 각 자릿수에 들어갈 만한 숫자를 추려서 self.numbers의 데이터의 크기를 줄여나가는 방식으로 구현했다.

- s는 숫자가 어떤 자리에 들어가야하는지에 관한 정보

    - 질문에 대한 답이 s=0이면 질문에 들어있던 숫자들은 다시 같은 자리에 오지 않게 한다.
- s+b는 어떤 숫자를 사용해야하는지에 관한 정보
    - 질문에 대한 답이 s+b=0이면 질문에 들어있던 숫자들은 다시 사용하지 않게 한다.
    - 질문에 대한 답이 s+b=4이면 질문에 들어있던 숫자들만 사용하게 된다.
    - 과거의 문답 기록에서 s+b개수만큼 현재의 질문을 생각 (예: 과거에 [1,2,3,4]가 1s 2b로 나왔다면 [1,2,3,4]중에서 1+2=3개를 뽑도록 한다.)

10000번 돌려본 결과 평균 8.6064번만에 정답을 찾는다. 표준편차는 3.049734
![질문횟수 분포](./img/method1_performance.png)

### 수학이의 역할을 수행하는 모듈2(Baseball수학2.py)
아이디어를 설명하기 위해 하나의 예시를 들어보자. 만약 [1,2,3,4]가 정답이라고 하고 여기에 질문이 [3,4,5,6]으로 던져진다면 0strike 2ball이 출력될 것이다. 그런데 이는 [3,4,5,6]이 정답이고 [1,2,3,4]가 질문으로 던져진 상황과 동일하다. 스트라이크와 볼은 두 리스트 사이의 대칭적인 관계를 만들어낸다고 생각할 수 있는 것이다. 

Baseball수학2는 이 성질을 이용하게된다. 어떤 질문(예:[3,4,5,6])을 하고 그에대한 답변(0strike 2ball)을 받게 되면 [3,4,5,6]과 0strike 2ball관계에 있는 모든 리스트들을 떠올리는 것이다. 즉, 모든 가능한 답변을 떠올린다.이후 그 다음 질문에 대한 답변을 받게 되면 이전에 떠올렸던 정답의 후보들에서 겹치는 것들만 남기고 나머지는 제거하는 방식으로 알고리즘이 이루어진다.

이 성질에 따라 생각해낸 아이디어는 상당한 노가다성을 필요로 하지만 이론상 가장 적은  질문 횟수로 정확하게 답을 알아낼 수 있다. 대략 11~13번의 질문이면 정답을 찾아냈다.

### 수학이의 역할을 수행하는 모듈(Baseball수학3)
처음에 [0,1,2,3]부터 질문하기 시작하여 한 칸씩 옆으로 옮겨서 질문하게 된다. [0,1,2,3] 다음에는 [1,2,3,4] 다음에는 [2,3,4,5]...[9,0,1,2]까지 총 10번의 질문을 하게 된다. 각 구간마다의 결과(strike, ball)를 받아서 어느 구간에 어느 숫자가 쓰일 지 예측한다.

이 모듈에 들어있는 클래스는 observe라는 이름을 가지고 있다. 이 클래스의 인스턴스가 생성될 때 10개의 0이 나열된 리스트인 self.distrib를 생각하게 된다. 이 self.dstrib의 숫자들이 조정되면서 가장 높은 값의 인덱스의 숫자들을 사용하여 정답을 찾게 된다.

이 self.distrib을 어떤 식으로 업데이트 할 것인지가 관건이다. 다음과 같은 예시를 보자.

3번째 자리에 5가 오는, [X,X,5,X]의 형태에 5가 오는지 판별하려고 한다. 수학이는 [0,1,2,3]을 질문하고 그 다음은 [1,2,3,4], 그 다음은 [2,3,4,5]... 이런 식으로 [9,0,1,2]까지 10번의 질문을 할 것이다. s+b가 0이 아니라면 질문에 있던 숫자들을 인덱스로 가지는 self.distrib의 원소들에 1을 더하게 된다. 10번의 질문이 모두 끝나면 self.distrib는 [0,0,1,2,3,4,3,2,1,0]의 형태를 가질 것이다. 인덱스가 5인 곳의 값이 4로 가장 높으므로 정답에는 5가 들어있다고 판단할 수 있다.

이 방식은 사실 문제점이 있다. 예측할 숫자가 하나라면 괜찮지만 둘 이상이라면 문제가 생길 수 있다. 5와 7이 정답에 포함되어있다고 가정하자. 그러면 self.distrib는 [1,0,1,2,3,4,4,4,3,2]로 나올 것이다. 5와 7인 곳은 값이 4가 되어서 정답의 후보로 들어가지만, 6은 정답에 있거나 없거나 상관없이 값이 4가 되는 문제점이 생긴다. 4가 연속되어 나타나면 4가 시작되는 인덱스와 4가 끝나는 인덱스는 반드시 정답에 포함된다. 그러나 그 사이의 인덱스들이 정답에 포함되는지 판단하기 위해서는 s+b가 아닌 다른 정보를 필요로 한다.

self.distrib를 업데이트 하기 위해 사용하는 정보를 s라고 해보자. 이 경우는 위치에 대한 정보를 주어야 하기 때문에 다음과 같은 방법을 생각해보았다. 만약 [3,4,5,6]에서 s가 0이 아니라면 각각 1,10,100,1000을 더하는 것이다. 만약 [2,5,3,6]이 정답이라면 self.distrib은 
[0,1,*11,***111,1111,**1110,****1100,1000,0,0]가 된다. 인덱스가 2인 곳의 값이 11인데, 이는 2가 첫째 또는 둘째 자리에 온다는 의미이다. 인덱스 6인 곳은 값이 1100이다. 이는 6이 넷째자리 또는 셋째 자리에 온다는 의미이다. 

하지만 이 방식 역시 문제가 있다. 인덱스 4인 곳의 경우 값이 1111이라 어느 자리에든 들어갈 수 있다고 예측이 되는데 사실 4는 정답에 포함되지 않는다. s+b로 걸러낼 수 있을까 싶지만 양 옆의 3과 5가 모두 정답에 포함되기 때문에 4가 걸러지지 않는다. 따라서 뭔가 다른 방법이 필수적이다.

### (번외.)머신러닝을 이용한 문제해결
동국이와 수학이의 문답과정 데이터를 모아서 RNN을 통해 학습을 시켜준다. 컴퓨터는 학습된 데이터를 바탕으로 문제를 풀기 위한 최적의 가중치 행렬들을 만들게 될 것이다. (발표일 전까지 되면 하고 아님말고...)

