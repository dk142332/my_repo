nums = list(map(int, input().split()))
a = nums[0]
b = nums[1]

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")