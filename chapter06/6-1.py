coffee_shops = ['스타벅스','이디야커피','투썸','카페베네','커피빈','공차','빽다방']
print(coffee_shops)

print(coffee_shops[0])
print(coffee_shops[-1][0])

print(coffee_shops[-4:7])

print(coffee_shops.index('투썸'))

print(len(coffee_shops))

#droptop
coffee_shops.append('드랍탑')
coffee_shops.append('메이데이')
coffee_shops.insert(1,'탐앤탐스')
print(coffee_shops)
coffee_shops.remove('탐앤탐스')
del coffee_shops[7]
print(coffee_shops)

coffee_shops.sort()
print(coffee_shops)
coffee_shops.reverse()
print(coffee_shops)