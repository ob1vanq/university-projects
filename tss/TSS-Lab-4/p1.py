# 1. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 128 Гц.
# Сформувати сигнали ділянки синусоїди частотою 2, 2.5, 40, 100, 600 Гц. Врахувати необхідність
# дотримання періодичності дискретного сигналу для отримання адекватного спектру. Побудувати
# за допомогою функції plot графіки сигналів та за допомогою функції stem графіки їх амплітудних
# спектрів. Зробити висновки щодо відповідності отриманих спектрів тим, які повинні бути
# отримані згідно теоретичних міркувань.

import numpy as np
import matplotlib.pyplot as plt
from params import c1, c2, spectrum

fs = 128

t = np.linspace(0, 1, fs)
signal_2 = np.sin(2*np.pi * t * 2), 2
signal_2_5 = np.sin(2*np.pi * t * 2.5), 2.5
signal_40 = np.sin(2*np.pi * t * 40), 40
signal_100 = np.sin(2*np.pi * t * 100), 100
signal_600 = np.sin(2*np.pi * t * 600), 600

signals = [signal_2, signal_2_5, signal_40, signal_100, signal_600]

fig, axs = plt.subplots(5, 2, figsize=(14, 15))


for i in range(len(signals)):
    sig, fq = signals[i]
    axs[i, 0].set(title=f"Сигнал з частотою {fq} Гц")
    axs[i, 0].plot(t, sig, c1)
    axs[i, 1].set(title=f"Спектр сигналу, частота дискретизації: {fs} Гц")
    full_period = True if fq >= 64 else False
    axs[i, 1].stem(spectrum(sig, full_period)*2/(fs/2), linefmt=c2)

for ax in axs.flat:
    ax.grid()
plt.tight_layout()
fig.savefig("data/1.png")
plt.show()
plt.close()

