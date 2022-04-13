# - записати сигнали стоячи, тримати пристрій в руці, яка опущена вздовж тулуба
# протягом 1 хвилини;
# - почати запис, покласти пристрій в кишеню, постояти 10 секунд, пройти по коридору
# спокійним кроком, постояти 10 секунд, припинити запис;
# - почати запис, покласти пристрій в кишеню, постояти 10 секунд, пробігти по
# коридору, постояти 10 секунд, припинити запис.
# Зберегти дані в csv-файл, відкрити його з допомогою Python. Зберегти сигнали на
# диск для використання в наступних роботах.
# Побудувати графіки сигналів акселерометра і гіроскопа, підписати вісі.

import csv
import io
import os

import matplotlib.pyplot as plt
import numpy as np

from methods import signal_width


def function_1(*, suptitle, path=r'datas/1_1.csv'):

    accel_x = []
    accel_y = []
    accel_z = []

    giro_x = []
    giro_y = []
    giro_z = []

    with io.open(path, encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for row in csv_reader:
            accel_x.append(float(row['АКСЕЛЕРОМЕТР X (m/s²)']))
            accel_y.append(float(row['АКСЕЛЕРОМЕТР Y (m/s²)']))
            accel_z.append(float(row['АКСЕЛЕРОМЕТР Z (m/s²)']))
            giro_x.append(float(row['ГИРОСКОП X (rad/s)']))
            giro_y.append(float(row['ГИРОСКОП Y (rad/s)']))
            giro_z.append(float(row['ГИРОСКОП Z (rad/s)']))

    time = signal_width(data=accel_x, sample_rate=200)
    fig, axs = plt.subplots(2, 3, figsize=(14, 7))
    t = np.linspace(**time.linspace)
    zero_y = [0 for i in t]

    for j in range(2):
        if j == 0:
            y = [accel_x, accel_y, accel_z]
            titles = ['АКСЕЛЕРОМЕТР X (m/s²)', 'АКСЕЛЕРОМЕТР Y (m/s²)', 'АКСЕЛЕРОМЕТР Z (m/s²)']
        else:
            y = [giro_x, giro_y, giro_z]
            titles = ['ГИРОСКОП X (rad/s)', 'ГИРОСКОП Y (rad/s)', 'ГИРОСКОП Z (rad/s)']
        for i in range(3):
            if min(y[i]) < 0:
                axs[j, i].plot(t, y[i], linewidth=2)
                axs[j, i].plot(t, zero_y, 'orange')
            else:
                axs[j, i].plot(t, y[i], linewidth=2)
            axs[j, i].set_title(titles[i]+f", частота дискретизації {time.sample_rate}")

    plt.suptitle(f"Завантажено з {path}, "+suptitle, fontweight="bold")
    plt.tight_layout()

    for ax in axs.flat:
        ax.set(xlabel='час, с', ylabel='амплітуда')
        ax.grid(linestyle='--', color='grey')
        ax.minorticks_on()

    file_name = r"datas/пункт1/{}.png".format(suptitle)
    file_dir = os.path.abspath(os.curdir) + r"datas\пункт1\{}.png".format(suptitle)
    print(f"\nЗберігаю у: {file_dir}")
    fig.savefig(file_name, bbox_inches='tight')

    fig.set_figwidth(16)
    fig.set_figheight(10)
    plt.show()


def run():
    function_1(suptitle="пункт 1.1")
    function_1(path=r"datas/1_2.csv", suptitle="пункт 1.2")
    function_1(path=r"datas/1_3.csv", suptitle="пункт 1.3")