import random
import time

words = ["wow","algorithm","code","mouse","시간모듈","컴퓨터","타자","대학교","파이썬","python","알고리즘","노트북","AI"]
n = 1
score = 0 # 점수
name = input("이름을 입력하세요=>")

print("타자 게임 준비되면 Enter~")
input()

start_time = time.time() # 시작시간

while n <=10:
    print(f"*round {n}") # 몇 라운드인지
    current_word = random.choice(words) # 이번라운드 단어
    
     
    print(f"*word : {current_word}") # 이번라운드 단어 알려주기
    user_input = input("*단어를 입력하세요:") # 단어 받기

    if user_input == current_word: # 단어가 같다면
        print("*correct")
        n += 1
        score += 10
        words.remove(current_word) # ***중복제거***
        
    else: #같지 않다면
        print("*re")
end_time = time.time()
es_time = end_time - start_time #끝난시간

print(f"{name}'s typing time : {es_time:.2f}secon, {score}score")
       