# 5. Для сигналів з п. 3 лабораторної роботи про спектральний аналіз побудувати
# спектрограми сигналу з використанням вікна, тривалість і перекриття якого підібрані
# оптимально для визначення моменту розриву в сигналі. Обгрунтувати свій вибір та
# зробити висновки.
import numpy as np
from scipy import signal

from params import win, plot
import matplotlib.pyplot as plt

fs = 128
time = 3
t = np.linspace(0, time, fs*time)


def indexes(time: float, fs: int = 128, n: int = 10):
    start = int(time * fs)
    end = start+n
    return start, end


def w_tau(s, e, sig):
    size = len(sig)
    center = int((s+e)/2)
    wt_size = int(center/1.618)
    if wt_size+center > size:
        wt_size = int(size-center)
    if center-wt_size < 0:
        wt_size = int(center)
    wt = np.zeros(size)
    wt[center-wt_size: center+wt_size] = win.parzen(wt_size*2)
    return wt


# ind = np.linspace(0, 2.7, 20)
ind = [1.05, 2]
for i in range(2):
    t = np.linspace(0, time, fs * time)
    sig = np.sin(2 * np.pi * t * 20)
    s, e = indexes(ind[i], fs=fs)
    sig[s:e] = 0
    fig, ax = plt.subplots(3, 1, figsize=(10, 6))
    wt = w_tau(s, e, sig)
    sig=wt*sig
    ax[0].plot(t, sig)
    ax[1].plot(t, wt)
    f, t, Sxx = signal.spectrogram(x=sig, fs=fs, window='parzen', nperseg=int(fs/4))
    ax[2].pcolormesh(t, f, Sxx, cmap='PuBu', shading='auto')
    ax[0].set_title(f"Сигнал з розривом у {ind[i]}, з використанням вікна")
    ax[1].set_title("Віконна функція")
    ax[2].set_title("Спектрограма")
    plot.set_param(ax)
    plt.tight_layout()
    fig.savefig(f"data/5_{i+1}.png")
    plt.close()

