import os

import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import scipy.interpolate


def ritmogram(suptitle, *, path, type):
    file = scipy.io.loadmat(path)
    data = file[type]
    data = np.array([i[0] for i in data])
    size = len(data)
    sw = round(np.sum(data) / 1000)
    data[0] = data[-1]

    t = np.linspace(0, sw, size)
    t_new = np.arange(0, size, 1)
    f = scipy.interpolate.interp1d(t, data, bounds_error=False)
    data_new = f(t_new)

    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    axs[0].plot(t, data)
    axs[0].set_title("початковий сигнал")
    axs[1].plot(t_new, data_new)
    axs[1].set_title("інтерпольований сигнал")
    axs[2].plot(t, data, label='початковий сигнал')
    axs[2].plot(t_new, data_new, label='інтерпольований сигнал')
    axs[2].legend(loc="lower left")

    for ax in axs.flat:
        ax.set(xlabel='час, с', ylabel='інтервал між ударами серця, с')
        ax.grid(linestyle='--', color='grey')
    plt.suptitle(f"Завантажено з '{path}'", fontweight="bold")
    plt.tight_layout()
    file_name = r"datas/пункт5/{}.png".format(suptitle)
    file_dir = os.path.abspath(os.curdir) + r"datas\пункт5\{}.png".format(suptitle)
    print(f"\nЗберігаю у: {file_dir}")
    fig.savefig(file_name, bbox_inches='tight')
    plt.show()


def run():
    ritmogram(path=r'datas/heart_rate_apnea.mat', type="hr_ap", suptitle="пункт 5.1")
    ritmogram(path=r'datas/heart_rate_norm.mat', type="hr_norm",suptitle="пункт 5.2")

