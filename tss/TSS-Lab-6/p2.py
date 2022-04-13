# 2. Сформувати вектор відліків часу тривалістю 1 с для частоти дискретизації 128
# Гц. Сформувати сигнали ділянки синусоїди частотою 10 Гц амплітуди 1 В. Додати
# випадковий сигнал з нульовим середнім значенням амплітуди 2 В. Спроектувати ФНЧ,
# ФВЧ та СФ Чебишова І роду для позбавлення сигналу від шуму (cheb1ord, cheby1).

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from methods import spectrum, plot

Fs = 128  # Hz
time = 1  # sec
t = np.linspace(0, time, time * Fs)
sig = np.sin(2*np.pi*10*t)
noise = np.random.normal(2, 0.5, Fs*time)
noised_sig = sig + noise

F_pass = [50, 20, np.array([7, 13])]  # Hz
F_stop = [40, 30,  np.array([4, 16])]  # Hz
R = [3,3,1]
Rp = 3  # dB
Rs = 30  # dB

btype=["high", "low", "band"]

path_list = ["ФВЧ", "ФНЧ", "СФ"]
for i in range(3):
    Wp = F_pass[i]/(Fs/2)
    Ws = F_stop[i]/(Fs/2)

    N, Wn = signal.cheb1ord(Wp, Ws, Rp, Rs, True)
    b, a = signal.cheby1(N, R[i], Wn, btype[i])
    w, h = signal.freqz(b, a, fs=Fs)


    filtered_sig, _ = signal.lfilter(b, a, noised_sig, zi=signal.lfilter_zi(b, a)*noised_sig[0])
    filtered_sig_amp = spectrum(filtered_sig, Fs)
    signal_amp = spectrum(sig, Fs)
    noise_amp = spectrum(noise, Fs)
    noised_amp = spectrum(noised_sig, Fs)
    filter_amp = (w, abs(h))

    plot(
        [
            (t, sig), signal_amp,
            (t, noise), noise_amp,
            (t, noised_sig), noised_amp,
            filter_amp,
            (t, filtered_sig), filtered_sig_amp
        ], path=f"data/2-{path_list[i]}.png"
    ).show()

    print(path_list[i])
    print(len(b))
    print(np.mean(sig / noise))
    print(np.mean(filtered_sig / noise))
