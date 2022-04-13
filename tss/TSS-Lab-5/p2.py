# 2. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 128 Гц.
# Сформувати сигнали ділянки синусоїди частотою 2 та 2.5 Гц. Побудувати амплітудний спектр
# сигналів без використання віконної функції та з використанням першого вікна згідно варіанту.
# Тривалість вікна обрати рівною тривалості сигналів. Порівняти з результатами п. 1 лабораторної
# роботи зі спектрального аналізу. Зробити висновки щодо спотворення спектрів та доцільності
# використання віконної обробки.

import numpy as np
import matplotlib.pyplot as plt
from params import spectrum, plot, win
fs = 128
t = np.linspace(0, 1, fs)
sin2 = np.sin(2 * np.pi * t * 2)
sin2_5 = np.sin(2 * np.pi * t * 2.5)
fig, axs = plt.subplots(2, 3, figsize=(14, 5))
sig = [sin2, sin2_5]
for i in range(2):
    s = sig[i]
    spc, size = spectrum(s, fs)
    t_spc, amp = spc
    axs[i, 0].plot(t, s)
    axs[i, 1].stem(*spc); axs[i, 1].set_title("Спектр")
    axs[i, 2].stem(*spectrum(amp*win.parzen(size), fs)[0]); axs[i, 2].set_title("Віконний спектр")
axs[0, 0].set_title("Сигнал 2 Гц")
axs[1, 0].set_title("Сигнал 2.5 Гц")
plot.set_param(axs)
fig.savefig("data/2.png")
plt.show()
plt.close()

