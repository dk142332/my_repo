import random
# 오답 기회
cnt = 3
#점수 초기화
score = 0
#시작
print("문제풀이를 시작하려면 Enter키를 치세요")
input()
#이름 입력
name = input("이름 입력 =>")
#반복 게임
while True:
    #덧셈 재료들
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    #문제 출력
    print(f"{x} + {y} = ", end="")
    #답 입력 받기
    try:
        answer = int(input())
    except Exception as e:
        print(f"유효하지 않은 입력입니다: {e}. 정수를 입력하세요.")
        continue
    #답 비교하기
    if answer == x + y:
        print("정답")
        score = score + 10
    #오답이면 기회 - 1, 오답 3번이면 break
    else:
        print(f"오답, 남은 기회 {cnt - 1}")
        cnt = cnt -1
        if cnt == 0:
            break
#점수 출력
print(f"{name}님의 점수는 => {score}")