score = int(input("점수를 입력하세요:"))
hakjum = int(input("학점을 입력하세요"))

if score >= 90:
    print("A학점")
elif score >= 80:
    print("B학점")
elif score >= 70:
    print("C학점")
elif score >= 60:
    print("D학점")
else:
    print("F학점")
print("수고하셨습니다.")

# if hakjum = "A":
#     print("장학금대상자입니다")
# else:
#     print("아님")