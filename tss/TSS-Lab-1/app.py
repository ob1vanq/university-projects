import math as m
import os
import random

from builder import builder

sin = lambda t, w, a: a * m.sin(2 * m.pi * w * t)


def print_save():
    os.system("cls")
    print("\n --- Файл збережено ----\n")


def print_err():
    os.system("cls")
    print("\n --- Некоректе введення данних --- \n")


def menu():
    while True:
        try:
            index = int(input("[1] - Побудувати графік автоматично\n"
                              "[2] - Ввести амплітуди з клавіатури\n"
                              "[3] - Побудувати імпульс автоматично\n"
                              "[4] - Задати параметри імпульсу\n"
                              "[5] - Побудувати імпульс із збережених даних\n"
                              "[6] - Видалити всі збережені данні\n"
                              "[0] - Вийти з програми\n>> "))

            if index == 0:
                break

            if index == 1:
                a = [random.randint(1, 20) for i in range(3)]
                x = builder.fill_x(0, 1, 256)
                y1 = builder.fill_y(func=sin, stuff=x, w=1, a=a[0])
                y2 = builder.fill_y(func=sin, stuff=x, w=10, a=a[1])
                y3 = builder.fill_y(func=sin, stuff=x, w=50, a=a[2])

                print_save()
                builder.triple(x=[x, x, x], y=[y1, y2, y3], w=[1, 10, 50], amp=a)

            if index == 2:
                a = [float(input(f"Амплітуда({i + 1}): ")) for i in range(3)]
                x = builder.fill_x(0, 1, 256)
                y1 = builder.fill_y(func=sin, stuff=x, w=1, a=a[0])
                y2 = builder.fill_y(func=sin, stuff=x, w=10, a=a[1])
                y3 = builder.fill_y(func=sin, stuff=x, w=50, a=a[2])

                print_save()
                builder.triple(x=[x, x, x], y=[y1, y2, y3], w=[1, 10, 50], amp=a)

            if index == 3:
                print_save()
                builder.impulse()

            if index == 4:
                long = float(input("Довжина імпульсу {0; 9,9}: "))
                amp = float(input("Амплітуда: "))
                builder.impulse(amp=amp, long=long, rand=True)

            if index == 5:
                builder.upload()

            if index == 6:
                if input("Введіть щоб підтвердити[y/n]: ").lower() == 'y':
                    builder.clean_all_directory()
                else:
                    os.system("cls")
        except:
            print_err()


if __name__ == '__main__':
    menu()
