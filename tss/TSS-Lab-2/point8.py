# 8. Прочитати в робочу область сигнал внутрішньочерепного тиску. Зберегти
# отриманий сигнал для використання в наступних роботах. Файл TBI_ICP.txt, сигнал
# одноканальний, записаний з частотою дискретизації 125 Гц, одиниці виміру – ммHg),
# вивести графік на екран, позначити вісі.

import matplotlib.pyplot as plt
import numpy as np

from methods import signal_width


def run():

    with open(r"datas/TBI_ICP.txt", "r") as file:
        array = np.array(file.readlines())
        array = np.float_(array)

    t = np.linspace(**signal_width(data=array, sample_rate=125).linspace)

    fig, ax = plt.subplots()

    ax.plot(t, array)
    ax.grid(linestyle='--', color='grey')
    ax.set(xlabel="Час, с", ylabel="ммHg", title="Частота дискретизації 125 Гц")
    plt.suptitle(f"Завантажено з datas/TBI_ICP.txt", fontweight="bold")
    plt.tight_layout()
    plt.show()

