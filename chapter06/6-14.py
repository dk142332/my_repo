print("\n" + "=" * 60)
print("편의점 장바구니 계산기")
print("=" * 60)

store = {
    "삼각김밥" : (1200, "식품"),
    "컵라면" : (1500, "식품"),
    "참이슬" : (1800, "음료"),
    "코카콜라" : (1600, "음료"),
    "초코파이" : (3500, "과자"),
    "새우깡" : (1500, "과자"),
    "바나나우유" : (1300, "음료"),
    "도시락" : (4200, "식품"),
}

cart = [
    ("삼각김밥", 2),
    ("컵라면", 1),
    ("코카콜라", 3),
    ("초코파이", 1),
    ("바나나우유", 2),
]

print(" 영수증 ")
print("-" * 40)

merged_cart = {}
for item, qty in cart:
    print(merged_cart.get(item, 0))
    merged_cart[item] = merged_cart.get(item, 0) + qty
    print(merged_cart)