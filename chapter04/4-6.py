import random
number = random.randint(1,100)
count = 1

while True:
    try:
        my_number = int(input("1부터 ~ 100 사이의 숫자 입력 =>"))

        if my_number > number:
            print("다운")
            count += 1
        elif my_number < number:
            print("업")
            count += 1
        else:
            print(f"축하{count}번")
            break
    except:
        print("오류야임마")
        break