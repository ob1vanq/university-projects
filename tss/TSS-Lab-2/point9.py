# Побудувати функцію для виводу на графік ділянки сигналів. В функцію
# передавати: час початку та закінчення ділянки (в секундах), вектор з відліками
# сигналу, частоту дискретизації. Передбачити перевірку правильності введення
# моментів часу, та можливість отримання за допомогою функції вектору з відліками
# ділянки сигналу та відліками часу.
import random
from typing import Union

import matplotlib.pyplot as plt
import numpy as np


def plot_selected_time(sig: list, start: float = 0, end: float = 30, sample_rate: int = 125,
                       parameters: Union["dict", "None"] = None) -> list:
    '''
    :param parameters:
    :param sig: [x_array, y_array]
    :param start: start of signal, s
    :param end: end of signal, s
    :param sample_rate: sample_rate, Hz
    :param parameters: dict = {"title": "Сигнал", "ylabel": "амплітуда", "xlabel": "час, с"}
    :return [x_cutting, y_cutting]
    '''

    if parameters is None:
        parameters = {"title": f"Сигнал {start}-{end} s", "ylabel": "амплітуда", "xlabel": "час, с"}

    class TimeIndex(Exception):
        pass

    x = sig[0]
    y = sig[1]
    second = len(x) / sample_rate

    if end > second or start > second:
        raise TimeIndex(f"time index out of range, long signal {second} s")
    if start < 0 or end < 0:
        raise TimeIndex("time index cannot be less than zero")
    start = int(start * sample_rate)
    end = int(end * sample_rate)

    x_new = x[start:end]
    y_new = y[start:end]

    fig, ax = plt.subplots()

    ax.plot(x_new, y_new)
    ax.grid(linestyle='--', color='grey')
    ax.set(**parameters)
    plt.show()

    return [x_new, y_new]


def simple_signal(long=16, rate=256, T=2, start=1, end=9):
    t = np.linspace(0, long, long * rate)
    y = []
    for i in range(int(long/T)):
        const = random.randint(0, 10)
        y += [const for j in range(T*rate)]
    plt.plot(t, y)
    plt.plot([start, start], [0, 10], [end, end], [0, 10], ls='--', c='orange')
    plt.grid(linestyle='--', color='grey')
    plt.ion()

    return [t, y]

def run():
    sig = simple_signal()
    plot_selected_time(sig=sig, start=1, end=9, sample_rate=256)
