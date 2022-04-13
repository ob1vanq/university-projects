# 3. Сформувати вектор відліків часу тривалістю 10 с для частоти дискретизації 256 Гц.
# Сформувати сигнали прямокутний імпульс амплітуди 1 В тривалості 1 сек. в момент часу 3 сек.
# (сигнал 1), та прямокутного імпульсу амплітуди 1 В тривалістю 1 сек. в момент часу 0сек.
# (сигнал 2). Побудувати графік взаємнокореляційної функції, зробити висновки щодо
# можливості визначення локалізації в часі прямокутного імпульсу з використанням
# кореляційного аналізу.


import matplotlib.pyplot as plt
import numpy as np

from methods import akf, vkf, mirror, impulse

fs = 512
time = 10
t = np.linspace(0, time, time*fs)
sig1 = impulse(time=time, amp=1, tau=3, long=1, fs=fs)
sig2 = impulse(time=time, amp=1, tau=0, long=1, fs=fs)
noise = np.random.normal(0, 0.01, fs*time)

for i in range(1, 2):
    if i == 1:
        # 4. Повторити п. 3, попередньо додавши до сигналу 1 шум з нульовим середнім
        # значенням. Зробити висновки, порівняти з п. 3.
        sig1 += noise
        sig2 += noise
    plt.rcParams.update({'font.size': 12})
    fig = plt.figure(figsize=(16, 6))
    ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=3)
    ax1.plot(t, sig1, "b")
    ax1.plot(t, sig2, "r")
    ax2 = plt.subplot2grid((2, 3), (1, 0), colspan=1)
    ax3 = plt.subplot2grid((2, 3), (1, 1), colspan=1)
    ax4 = plt.subplot2grid((2, 3), (1, 2), colspan=1)

    vkf_12 = mirror(vkf(sig1, sig2))
    akf1 = mirror(akf(sig1))
    akf2 = mirror(akf(sig2))

    ax2.plot(mirror(t, with_minus=True), vkf_12, "limegreen")
    ax3.plot(mirror(t, with_minus=True), akf1, "b")
    ax4.plot(mirror(t, with_minus=True), akf2, "r")

    ax1.set(title="Прямокутні імпульси")
    ax2.set(title="ВКФ сигналів")
    ax3.set(title="АКФ 1-го імпульсу")
    ax4.set(title="АКФ 2-го імпульсу")
    ax1.legend(['імпульс 1', 'імпульс 2'])

    for ax in (ax1, ax2, ax3, ax4):
        ax.grid(color="gray", linestyle="--")

    plt.tight_layout()
    fig.savefig(f'data/{3+i}.png')
    plt.show()

