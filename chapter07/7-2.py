def hello(name = "", room = "미정", food = "덮밥"):
    print("Hello")
    print(f"{name}님 {room}호실 배정 {food}주문 완료")

hello("송현준","3", "알리오올리오")
hello("정우진","3", "돈까스")
hello("김상헌","3", "제육")
hello("신재윤", food = "소바")