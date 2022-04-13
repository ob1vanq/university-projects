import json
import os
from random import randint

import matplotlib.pyplot as plt
import numpy as np


class builder():
    counter: int

    @staticmethod
    def get_counter():
        with open(r"graphics/counter.json", "r") as file:
            builder.counter = json.load(file)["c"]

    @staticmethod
    def update_counter():
        builder.get_counter()
        with open(r"graphics/counter.json", "w") as file:
            json.dump({"c": builder.counter + 1}, file, indent=2)

    @staticmethod
    def save(dct: dict):
        with open(r"graphics/graphic_data/{}.json".format(builder.counter), "w") as file:
            json.dump(dct, file, indent=2)

    @staticmethod
    def fill_x(start, end, wdist=256):
        return np.linspace(start, end, wdist)

    @staticmethod
    def fill_y(func, stuff: list, **kwargs):
        return [func(numb, **kwargs) for numb in stuff]

    @staticmethod
    def triple(x: list, y: list, w: list, amp: list):

        builder.update_counter()
        fig, axs = plt.subplots(1, 3)

        for i in range(3):
            axs[i].plot(x[i], y[i], color='mediumslateblue', linewidth=2)
            axs[i].grid(color='grey', linestyle='--')
            axs[i].minorticks_on()
            axs[i].set_title(f"Частота {w[i]} Гц, Амплітуда {amp[i]}")

        for ax in axs.flat:
            ax.set(xlabel="Час, с", ylabel="Амплітуда")

        fig.set_figwidth(16)
        fig.set_figheight(4)
        fig.suptitle(f"Збережено triple-{builder.counter}.png", fontweight="bold")

        fig.savefig(r"graphics/triple/triple-{}.png".format(builder.counter))
        plt.show()

    @staticmethod
    def upload():
        ls = os.listdir('graphics/graphic_data/')
        builder.update_counter()
        if not ls:
            os.system("cls")
            print("Немає збережених даних для імпульсу\n")
            return None
        try:
            filename = int(input(f"Оберіть номер № графіка імпульсу {ls}: "))
            with open(r"graphics/graphic_data/{}.json".format(filename), "r") as file:
                data = json.load(file)
                builder.impulse(amp=data["amp"],
                                long=data["long"],
                                tau=data["tau"],
                                upload=True)
            print()
        except:
            os.system("cls")
            print("Файла з таким ім'ям не існує\n")

    @staticmethod
    def impulse(long=0.3, amp=1, tau=4, rand=False, upload=False):
        builder.update_counter()
        fig, ax = plt.subplots()

        tau = tau
        long = long
        if rand:
            tau = randint(1 + int(long * 5), 99 - int(long * 5)) / 10

        start = int((tau - long / 2) * 256)
        end = int((tau + long / 2) * 256)

        x = np.linspace(0, 10, 2560)
        y = np.zeros(2560)
        y[start:end] = amp

        plt.plot(x, y, color='mediumslateblue', linewidth=2)
        plt.title(f"Центр імпульса {tau}, Довжина {long}, Амплітуда {amp}, номер #{builder.counter}")
        ax.set(xlabel="Час, с", ylabel="Амплітуда")
        plt.minorticks_on()
        plt.grid(color='grey', linestyle='--')
        if not upload:
            fig.suptitle(f"Збережено impulse-{builder.counter}.png", fontweight="bold")
            fig.savefig(r"graphics/impulse/impulse-{}.png".format(builder.counter))
            builder.save({"long": long,
                          "amp": amp,
                          "tau": tau})
        plt.show()

    @staticmethod
    def clean_all_directory():
        for file in os.listdir('graphics/graphic_data/'):
            os.remove('graphics/graphic_data/' + file)
        for file in os.listdir('graphics/impulse/'):
            os.remove('graphics/impulse/' + file)
        for file in os.listdir('graphics/triple/'):
            os.remove('graphics/triple/' + file)

        with open(r"graphics/counter.json", "w") as file:
            json.dump({"c": 0}, file, indent=2)
        os.system("cls")
        print("-- Дані видалено --\n")
