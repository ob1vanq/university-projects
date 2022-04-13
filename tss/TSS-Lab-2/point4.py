import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
from numpy import load

from methods import signal_width, view_proccesing


def func(*, p, ycord, xcord, directory, file_counter: str = ""):
    size = 16 if p == 8 else 12
    fig, axs = plt.subplots(nrows=ycord, ncols=xcord, figsize=(25, size))
    files = os.listdir(r'datas/{}/'.format(directory))
    timer = view_proccesing(end=xcord * ycord - 1, line_size=30, title="Формую графіки")
    for ax in axs.flat:
        fig.set_tight_layout(True)
        timer.load_line()
        path = r'datas/{}/'.format(directory) + files[p]
        data = load(path)

        time = signal_width(
            data=np.linspace(data['source_start'], data['source_end'], data['source_end'] - data['source_start']),
            sample_rate=data['fs'])

        labels = []
        indexes = []
        for i in range(time.size):
            if i in data['labels_indexes']:
                labels.append(data['signal'][i])
                indexes.append(time.data[i])

        t = np.linspace(**time.linspace)

        ax.plot(time.data, data['signal'])
        ax.plot(time.data, np.zeros(time.size), 'orange')
        ax.scatter(indexes, labels, marker='s', color='r')
        ax.xaxis.set_major_locator(ticker.AutoLocator())

        ax.set_title(f"{files[p]} " + f"{data['description']}", fontsize=10, fontweight="bold")
        ax.set(xlabel='час, с', ylabel=data['units'])
        ax.grid(linestyle='--', color='grey')
        ax.minorticks_on()
        p += 1

    plt.tight_layout()
    file_name = r"datas/пункт4/signals{}.png".format(file_counter)
    file_dir = os.path.abspath(os.curdir) + "\datas\пункт4\signals{}.png".format(file_counter)
    print(f"\nЗберігаю у: {file_dir}")
    fig.savefig(file_name, bbox_inches='tight')
    print("Друкую...\n")
    plt.show()


def run():
    func(p=0, ycord=3, xcord=3, directory="anomaly", file_counter="1.1")
    func(p=8, ycord=4, xcord=3, directory="anomaly", file_counter="1.2")
    func(p=0, ycord=3, xcord=3, directory="norm", file_counter="2.1")
    func(p=8, ycord=4, xcord=3, directory="norm", file_counter="2.2")
