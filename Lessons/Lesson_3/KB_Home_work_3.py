alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                      '"That depends a good deal on where you want to get to," said the Cat.\n' \
                      '"I don\'t much care where ——" said Alice.\n' \
                      '"Then it doesn\'t matter which way you go," said the Cat.\n' \
                      '"—— so long as I get somewhere," Alice added as an explanation.\n' \
                      '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800

seas_area = black_sea_area + azov_sea_area

print(f"The area of Black and Azov seas are {seas_area} square kilometers\n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_goods = 375_291
warehouse_1 = all_goods - 222_950
warehouse_3 = all_goods - 250_449
warehouse_2 = all_goods - warehouse_1 - warehouse_3

print(f"First warehouse has {warehouse_1} goods, \n"
      f"Second warehouse has {warehouse_2} goods,\n"
      f"And Third warehouse has {warehouse_3} goods.\n")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_payment = 1179
quantity_of_payments = 18

total_amount = month_payment * quantity_of_payments

print(f"The total sum is {total_amount} hrn.\n")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
list_of_dividends = [8019, 9907, 2789, 7248, 7128, 19224]
list_of_dividers = [8, 9, 5, 6, 5, 9]

solutions = []

for dividend, divider in zip(list_of_dividends, list_of_dividers):
    solutions.append(dividend % divider)

print(f"Remainder list looks like {solutions}\n")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
items = [
    ("pizza_big", 4, 274),
    ("pizza_mild", 2, 218),
    ("juice", 4, 35),
    ("cake", 1, 350),
    ("beverages", 3, 21)
]
total_sum = sum(quantity * price for _, quantity, price in items)

print(f"The total sum for birthday is {total_sum} hrn.\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_page_amount = (232 // 8) + 1

print(f"{total_page_amount} pages is needed to include 232 photos.\n")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
tank = 48
gasoline_consumption = 9

total_gasoline = 1600 / 100 * 9
quantity_of_refueling = 1 + total_gasoline // tank + 1

print(f"Total gasoline consumption is {total_gasoline} l.\n"
      f"At least {quantity_of_refueling} times they should go to the gasoline station "
      f"(in a case the tank was empty at the beginning). \n")
