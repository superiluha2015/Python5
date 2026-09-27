import random

count = 0
comp_count = 0
for number in range(10):
    player = int(input("""Выберите ход:
1. Камень
2. Ножницы
3. Бумага
Ответ запишите в виде числа: """))
    if player == 1:
        print("Ваш ход: камень")
    elif player == 2:
        print("Ваш ход: ножницы")
    elif player == 3:
        print("Ваш ход: бумага")
    else:
        print("Ошибка")
        exit()

    comp = random.randint(1, 3)

    if comp == 1:
        print("Ход компьютера: камень")
    elif comp == 2:
        print("Ход компьютера: ножницы")
    elif comp == 3:
        print("Ход компьютера: бумага")
    if player == comp:
        print("Ничья")
    elif player == 1 and comp == 3:
        print("Компьютер победил")
        comp_count += 1
    elif player == 2 and comp == 1:
        print("Компьютер победил")
        comp_count += 1
    elif player == 3 and comp == 2:
        print("Компьютер победил")
        comp_count += 1
    else:
        count += 1
        print("Вы победили")
    print(f"Вы победили {count} раз.")
    print(f"Компьютер победил {comp_count} раз.")
    if count == 3:
        print("Вы победили компьютера")
        break
    if comp_count == 6 or comp_count == 7:
        print("Пасхалка!")
        break