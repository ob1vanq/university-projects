import os

import numpy as np
import scipy.io
from methods import signal_width


def eeg(sample_rate=256, suptitle="", *, path):
    file = scipy.io.loadmat(path)
    array = file.get("sig")[0]
    size = np.linspace(**signal_width(data=array, sample_rate=sample_rate).linspace)

    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()

    ax.plot(size, array)
    ax.plot(size, np.zeros(len(array)), 'orange')
    plt.suptitle(f"Завантажено з '{path}',\n" + suptitle, fontweight="bold")
    ax.set(xlabel='час, с', ylabel='напруга, мВ')
    ax.grid(linestyle='--', color='grey')
    ax.minorticks_on()
    file_name = r"datas/пункт3/{}.png".format(suptitle)
    file_dir = os.path.abspath(os.curdir) + r"datas\пункт3\{}.png".format(suptitle)
    print(f"\nЗберігаю у: {file_dir}")
    plt.tight_layout()
    fig.savefig(file_name, bbox_inches='tight')
    plt.show()


def run():
    eeg(path=r"datas/eeg_healthy_12.mat", suptitle="пункт 3.1 Здорова людина")
    eeg(path=r"datas/eeg_sick_12.mat", suptitle="пункт 3.2 Хвора людина")
