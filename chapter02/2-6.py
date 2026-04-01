money = int(input("지불할 돈 입력:"))
price = int(input("커피 값:"))

change = money - price

c1000 = change//1000 #1000의 자리수 c1000에
change %= 1000 #100의 자리수 빼기

c500 = change//500 #500으로 나눈 몫
change %= 500 #500으로 나눈 후 나머지

c100 = change//100
change %= 100

c50 = change//50
change %= 50

c10 = change//10
change %= 10

print(f"거스름돈은 {money - price}입니다.")
print(f"1000원 지폐의 수 ▷{c1000}")
print(f"500원 동전의 수 ▷{c500}")
print(f"100원 동전의 수 ▷{c100}")
