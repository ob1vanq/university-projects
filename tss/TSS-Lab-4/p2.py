# 2. Сформувати вектор відліків часу тривалістю 10 с для частоти дискретизації 256 Гц.
# Сформувати сигнали ділянки синусоїди частотою 10 Гц (S 1 ) та 100 Гц (S 2 ).
# Сформувати на їх основі три сигнали:
#
# 2.1. сигнал (тривалістю 10 с), що дорівнює сумі цих двох сигналів;
# 2.2. сигнал, який спочатку містить сигнал 2*S 1 , а потім сигнал 2*S 2
# (матиме тривалість 20 секунд);
# 2.3. сигнал, який спочатку містить сигнал 2*S 2 , а потім сигнал 2*S 1
# (матиме тривалість 20 секунд).
#
# Побудувати графіки сигналів п. 2.1-2.3 (функція plot) та їх амплітудних спектрів (функція stem).
# Зробити висновки щодо можливості розрізнити коливання, присутні у сигналі, по їх спектральному складу,
# а також щодо відповідності властивостей сигналів у часі та їх спектрів.

import numpy as np
from params import c1, c2, spectrum
import matplotlib.pyplot as plt

fs = 256

t = np.linspace(0, 10, 10*fs)
t2 = np.linspace(0, 20, 20*fs)

s1 = np.sin(2*np.pi*t*10)
s2 = np.sin(2*np.pi*t*100)

sig_sum = s1+s2, t
sig_2xs1 = np.append(2*s1, 2*s2), t2
sig_2xs2 = np.append(2*s2, 2*s1), t2

signals = [sig_sum, sig_2xs1, sig_2xs2]
signals_name = ["sig_sum", "sig_2xs1", "sig_2xs2"]

fig, axs = plt.subplots(3, 2, figsize=(14, 7))


for i in range(len(signals)):
    sig, t = signals[i]
    axs[i, 0].set(title=f"Сигнал {signals_name[i]}")
    axs[i, 0].plot(t, sig, c1)
    axs[i, 1].set(title=f"Спектр сигналу, частота дискретизації: {fs} Гц")
    axs[i, 1].stem(spectrum(sig)*2/(fs/2), linefmt=c2)

for ax in axs.flat:
    ax.grid()


fig.savefig("data/2.png")
plt.show()
plt.close()