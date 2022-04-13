# 1. Сформувати вектор відліків часу тривалістю 5 с для частоти дискретизації 128
# Гц. Сформувати прямокутний імпульс в момент часу 3с тривалості 0.1 с амплітуди 1 В.
# Додати до сигналу випадковий шумовий сигнал із нульовим середнім значенням
# амплітуди 0.5В. Спроектувати ФНЧ Батерворта для позбавлення сигналу від шуму
# (функції buttord, butter, lfilter).
import random

import numpy as np
from scipy import signal

from methods import impulse, spectrum, plot

Fs = 128  # Hz
time = 5  # sec
t = np.linspace(0, time, time * Fs)
impulse = impulse(time=time, fs=Fs, tau=0.3, long=0.1, amp=1)# crate impulse
noise = np.random.normal(0.5, 0.001, Fs*time) # create noise
noised_sig = impulse + noise


F_pass = 20  # Hz
F_stop = 35  # Hz
Rp = 3  # dB
Rs = 40  # dB

Wp = F_pass/(Fs/2)
Ws = F_stop/(Fs/2)

n, Wn = signal.buttord(Wp, Ws, Rp, Rs, True)
b, a = signal.butter(n, Wn, "low")
w, h = signal.freqz(b, a, fs=Fs, worN=Fs*time)
print(len(b))

filtered_sig, _ = signal.lfilter(b, a, noised_sig, zi=signal.lfilter_zi(b, a)*noised_sig[0])
filter_amp = (w, abs(h))
impulse_amp = spectrum(impulse, Fs)
noise_amp = spectrum(noise, Fs)
noised_amp = spectrum(noised_sig, Fs)
filtered_sig_amp = spectrum(filtered_sig, Fs)

plot(
    [
        (t, impulse), impulse_amp,
        (t, noise), noise_amp,
        (t, noised_sig), noised_amp,
        filter_amp,
        (t, filtered_sig), filtered_sig_amp
    ], path="data/1.png"
).show()


print(np.mean(noised_sig / noise))
print(np.mean(filtered_sig / noise))


