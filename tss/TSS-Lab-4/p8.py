# 8. Сформувати сигнал синусоїди частоти 20.5 Гц амплітуди 1 В та тривалості 1 сек. для
# частоти дискретизації 1000 Гц. Отримати амплітудний спектр заданого сигналу.
# Дописати в кінці сигналу нульові відліки (10, 100, 1000 та 10000 відліків), отримуючи для
# кожного сигналу його амплітудний спектр.
# На графік кожного разу виводити спектр за допомогою функції stem в межах від 19 до
# 22 Гц. Зробити висновки щодо впливу доповнення сигналу нулями на роздільну здатність в
# частотній області та на якість визначення наявності синусоїдального коливання за спектральними
# характеристиками.

import numpy as np
import matplotlib.pyplot as plt
from params import c1, c2, spectrum


fs = 1000
sig_10 = np.zeros(10)
sig_100 = np.zeros(100)
sig_1000 = np.zeros(1000)
sig_10000 = np.zeros(10000)

signals = [[], sig_10, sig_100, sig_1000, sig_10000]


def freqs_ind(sig):
    size = len(sig)
    s = size/fs * 19
    e = size/fs * 22
    return int(s), int(e)


fig, axs = plt.subplots(5, 2, figsize=(14, 8))
for i in range(5):
    t = np.linspace(0, 1, 1 * fs)
    sig = np.sin(2*np.pi*t*20.5)
    sig = np.append(sig, signals[i])
    time = float(1 + len(signals[i])/1000)
    t = np.linspace(0, time, int(time*fs))
    axs[i, 0].plot(t, sig, c1)
    axs[i, 0].set(title=f"Сигнал 20.5 Гц доповненний {len(signals[i])} нулями")
    s, e = freqs_ind(sig)
    sptr = (spectrum(sig)*4/fs)[s:e]
    axs[i, 1].stem(np.linspace(19, 22, len(sptr)), sptr, linefmt=c2)
    axs[i, 1].set(title=f"Спектр сигналу у межах 19 - 22 Гц, Частота дискр. 1000 Гц")
for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/8.png")
plt.show()
plt.close()