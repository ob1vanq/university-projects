# 6. Побудувати функцію, яка будує графік зміни в часі середньої спектральної
# густини потужності в заданому частотному діапазоні та часовому діапазоні для заданого
# сигналу. В якості параметрів функції передавати назву сигналу, час t1, t2 та частоти f1, f2,
# а також інші необхідні параметри.
from scipy import signal

import numpy as np
import matplotlib.pyplot as plt

from params import plot

fs = 1000
time = 10
t = np.linspace(0, time, time*fs)
mod = 200*np.cos(2*np.pi*0.25*t)
sig1 = 2 * np.sin(2*np.pi*300*t + mod)
sig2 = np.sin(2*np.pi*t*10)

def spectral_power(sig, fr: tuple, t: tuple, fs: int, signame: str):
    fig = plt.figure()
    t1, t2 = t
    t1, t2 = int(t1 * fs), int(t2 * fs)
    f1, f2 = fr
    f1, f2 = int(2*129*f1/fs), int(2*129*f2/fs)
    long = np.linspace(0, len(sig)/fs, len(sig))
    f, ts, sxx = signal.spectrogram(x=sig, fs=fs)
    time_str = f'Time [sec] ({t[0]}-{t[1]})'
    freq_str = f'Frequency [Hz] ({fr[0]}-{fr[1]})'

    sig_ax = fig.add_subplot(2, 3, (1, 2))
    sig_ax.plot(long[t1:t2], sig[t1:t2], c=plot.color)
    sig_ax.set_xlabel(time_str)
    sig_ax.set_ylabel('Amplitude')

    spc_ax = fig.add_subplot(233)
    spc_ax.plot(f[f1:f2], sxx[f1:f2])
    spc_ax.set_xlabel(freq_str)

    sgr_ax = fig.add_subplot(212)
    t1, t2 = t
    time = len(sig)/fs
    t1, t2 = int(t1/time*len(ts)), int(t2/time*len(ts))
    sxx = [arr[t1:t2] for arr in sxx]
    sgr_ax.pcolormesh(ts[t1:t2], f[f1:f2], sxx[f1:f2], cmap='PuBu', shading='auto')
    sgr_ax.set_ylabel(freq_str)
    sgr_ax.set_xlabel(time_str)
    plt.suptitle(signame, fontweight="bold")
    plt.tight_layout()
    fig.savefig("data/"+signame+".png")
    plt.show()


spectral_power(sig1, fs=fs, fr=(100, 500), t=(2, 8), signame="Signal 1")
spectral_power(sig2, fs=fs, fr=(0, 20), t=(6, 10), signame="Signal 2 first position")
spectral_power(sig2, fs=fs, fr=(0, 200), t=(0, 1), signame="Signal 2 second position")