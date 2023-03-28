chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEGETARIAN_PRICE = 8.15
DELIVERY = 2.50

menus_price = \
(chicken_menus * CHICKEN_PRICE) + \
(fish_menus * FISH_PRICE) + \
(vegetarian_menus * VEGETARIAN_PRICE)

dessert_price = menus_price * 0.20

total_price = menus_price + dessert_price + DELIVERY

print(total_price)