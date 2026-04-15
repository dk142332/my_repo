X = int(input("총계"))
N = int(input())
total = 0

for i in range(N):
    p, q = map(int, input().split())
    total += p * q

if total == X:
    print("Yes")
else:
    print("No")
    