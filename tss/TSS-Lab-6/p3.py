# 3. Сформувати вектор відліків часу тривалістю 10 с для частоти дискретизації 128
# Гц. Сформувати випадковий сигнал амплітуди 10 мВ з нульовим середнім значенням,
# який зашумлений мережевою перешкодою частоти 50 Гц амплітуди 1В. Спроектувати ЗФ
# Батерворта для позбавлення сигналу від перешкоди.

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from methods import spectrum, plot

Fs = 128  # Hz
time = 1  # sec
t = np.linspace(0, time, time * Fs)
# sig = np.sin(2*np.pi*10*t)
sig = np.random.normal(0.1, 0.001, Fs*time)
noise = np.sin(2*np.pi*t*50)
noised_sig = sig + noise

F_pass = np.array([45, 55])  # Hz
F_stop = np.array([35, 65])  # Hz
Rp = 3  # dB
Rs = 40  # dB

Wp = F_pass/(Fs/2)
Ws = F_stop/(Fs/2)

n, Wn = signal.buttord(Wp, Ws, Rp, Rs)
b, a = signal.butter(n, Wn, btype="bandstop")
w, h = signal.freqz(b, a, fs=Fs, worN=Fs*time)
print(len(b))


filtered_sig, _ = signal.lfilter(b, a, noised_sig, zi=signal.lfilter_zi(b, a)*noised_sig[0])
filter_amp = (w, abs(h))
sig_amp = spectrum(sig, Fs)
noise_amp = spectrum(noise, Fs)
noised_amp = spectrum(noised_sig, Fs)
filtered_sig_amp = spectrum(filtered_sig, Fs)

plot(
    [
        (t, sig), sig_amp,
        (t, noise), noise_amp,
        (t, noised_sig), noised_amp,
        filter_amp,
        (t, filtered_sig), filtered_sig_amp
    ], path="data/3.png"
).show()

