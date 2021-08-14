#숫자 맞히기 게임1
import random
correct = random.randint(1, 20)
cnt = 4

while cnt > 0:
    number = int(input(f'기회가 {cnt}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요.'))
    if number == correct:
        print(f'축하합니다. {5-cnt}번 만에 숫자를 맞히셨습니다.')
        break
    elif number < correct and 1 <= number <=20:
        print('up')
        cnt -= 11
    elif number > correct and 1 <= number <=20:
        print('down')
        cnt -= 1
    else:
        print('올바르지 않은 값입니다.1-20 사이의 정수를 입력하세요.')
    if cnt == 0:
        print(f'아쉽군요. 정답은 {correct}입니다. 다시 도전하세요.')

#숫자 맞히기 게임 2
import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요: ".format(NUM_TRIES - tries)))
    tries += 1    
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))