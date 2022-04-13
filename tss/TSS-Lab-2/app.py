import sys
import logging
import os

from point1 import run as r1
from point2 import run as r2
from point3 import run as r3
from point4 import run as r4
from point5 import run as r5
from point6 import run as r6
from point7 import run as r7
from point8 import run as r8
from point9 import run as r9


def menu():
    while True:
        os.system("cls")
        txt = ""
        for i in [f"[{i}]: пункт {i}\n" for i in range(1, 10)]:
            txt += i
        index = int(input("-------------------------------------------\n" +
                          txt +
                          "[0]: Вихід / Reload\n >> "))
        print("-------------------------------------------")

        if index == 1:
            r1()
        if index == 2:
            r2()
        if index == 3:
            r3()
        if index == 4:
            r4()
        if index == 5:
            r5()
        if index == 6:
            r6()
        if index == 7:
            r7()
        if index == 8:
            r8()
        if index == 9:
            r9()
        if index == 0:
            os.system("cls")
            if int(input("[0]: Вихід\n[1]: Перезантаження\n >> ")) == 0:
                break
            else:
                os.system("cls")
                python = sys.executable
                os.execl(python, python, *sys.argv)


if __name__ == "__main__":
    try:
        menu()
    except:
        os.system("cls")
        print("Щось пішло не так...")
        logging.exception('')
