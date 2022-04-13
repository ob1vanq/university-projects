# 4. Для звукових сигналів, які отримані з різною частотою дискретизації, виконати
# допомогою фільтрів розділення на три спектральні діапазони: до 450 Гц; від 450 Гц до 1
# кГц; від 1кГц до 4 кГц. Прослухати отримані сигнали, зробити висновки.

import wave
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavf
from methods import impulse, spectrum


def plot(signals, path, suptitle):
    fig = plt.figure(figsize=(12, 6))
    sig = plt.subplot2grid((3, 5), (0, 0), colspan=3)
    signal_amp = plt.subplot2grid((3, 5), (0, 3), colspan=2)
    filtered_sig = plt.subplot2grid((3, 5), (1, 0), colspan=3)
    filtered_sig_amp = plt.subplot2grid((3, 5), (1, 3), colspan=2)
    filter_amp = plt.subplot2grid((3, 5), (2, 0), colspan=5)
    title = ["Вхідний сигнал", "АЧХ вхідного сигналу",
             "Відфільтрований сигнал", "АЧХ відфільтрованого сигналу",
             "АЧХ фільтру"]

    for ax, i in zip([sig, signal_amp, filtered_sig, filtered_sig_amp, filter_amp], range(5)):
        ax.plot(*signals[i], "b")
        ax.grid(linestyle="--", color="g")
        ax.set_title(title[i])
    plt.suptitle(suptitle)
    plt.tight_layout()
    fig.savefig(path)
    return plt


def audio(path, fs):
    wav = wave.open(path, "r")
    raw = wav.readframes(-1)
    raw = np.frombuffer(raw, np.int16)
    size = len(raw)
    t = np.linspace(0, 5, size)
    return t, raw


def filter1(sig, Fs):
    t, sig = sig
    F_pass = 200
    F_stop = 450
    Rp = 3
    Rs = 40
    Wp = F_pass/(Fs/2)
    Ws = F_stop/(Fs/2)
    n, Wn = signal.buttord(Wp, Ws, Rp, Rs, True)
    b, a = signal.butter(n, Wn, "low")
    w, h = signal.freqz(b, a, fs=Fs, worN=len(sig))
    filtered_sig, _ = signal.lfilter(b, a, sig, zi=signal.lfilter_zi(b, a) * sig[0])
    filtered_sig_amp = spectrum(filtered_sig, Fs)
    sig_amp = spectrum(sig, Fs)
    plot(
        [(t, sig), sig_amp,
         (t, filtered_sig),
         filtered_sig_amp,
         (w, abs(h))
         ],
        path=f"data/{Fs}Hz filter1.png",
        suptitle=f"{Fs//1000}kHz-lowpass-filter"
    ).show()
    wavf.write(filename=f"wav/{Fs//1000}kHz-lowpass-filter.wav", rate=int(Fs), data=filtered_sig.astype(np.int16))


def filter2(sig, Fs):
    t, sig = sig
    F_pass = np.array([450, 1000])
    F_stop = np.array([200, 3000])
    Rp = 3
    Rs = 40
    Wp = F_pass/(Fs/2)
    Ws = F_stop/(Fs/2)
    n, Wn = signal.buttord(Wp, Ws, Rp, Rs, True)
    b, a = signal.butter(n, Wn, "band")
    w, h = signal.freqz(b, a, fs=Fs, worN=len(sig))
    filtered_sig, _ = signal.lfilter(b, a, sig, zi=signal.lfilter_zi(b, a) * sig[0])
    filtered_sig_amp = spectrum(filtered_sig, Fs)
    sig_amp = spectrum(sig, Fs)
    plot(
        [(t, sig), sig_amp,
         (t, filtered_sig),
         filtered_sig_amp,
         (w, abs(h))
         ],
        path=f"data/{Fs}Hz filter2.png",
        suptitle=f"{Fs//1000}kHz-bandpass1-filter"
    ).show()
    wavf.write(filename=f"wav/{Fs//1000}kHz-bandpass1-filter.wav", rate=int(Fs), data=filtered_sig.astype(np.int16))


def filter3(sig, Fs):
    t, sig = sig
    F_pass = np.array([1000, 4000])
    F_stop = np.array([200, 5000])
    if Fs > 8e3:
        F_stop = np.array([200, 8000])
    Rp = 3
    Rs = 40
    Wp = F_pass/(Fs/2)
    Ws = F_stop/(Fs/2)
    n, Wn = signal.buttord(Wp, Ws, Rp, Rs, True)
    b, a = signal.butter(n, Wn, "band")
    w, h = signal.freqz(b, a, fs=Fs, worN=len(sig))
    filtered_sig, _ = signal.lfilter(b, a, sig, zi=signal.lfilter_zi(b, a) * sig[0])
    filtered_sig_amp = spectrum(filtered_sig, Fs)
    sig_amp = spectrum(sig, Fs)
    plot(
        [(t, sig), sig_amp,
         (t, filtered_sig),
         filtered_sig_amp,
         (w, abs(h))
         ],
        path=f"data/{Fs}Hz filter3.png",
        suptitle=f"{Fs // 1000}kHz-bandpass2-filter"
    ).show()
    wavf.write(filename=f"wav/{Fs//1000}kHz-bandpass2-filter.wav", rate=int(Fs), data=filtered_sig.astype(np.int16))


sig1 = audio(path="output 16kHz.wav", fs=8e3)
sig2 = audio(path="output 44_1kHz.wav", fs=44.1e3)

filter1(sig1, Fs=16e3)
filter1(sig2, Fs=88200)
filter2(sig1, Fs=16e3)
filter2(sig2, Fs=88200)
filter3(sig1, Fs=16e3)
filter3(sig2, Fs=88200)
