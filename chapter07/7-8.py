def func1():
    a = 5
    print("func1()에서의 a값 %d"%a)

def func2():
    print("func2()에서의 a값 %d"%a)

a = 10 #전역변수

func1() #5
func2() #10

a = 3 #전역변수
func1() #5
func2() #3