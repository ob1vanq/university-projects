import numpy as np
from scipy import signal
from p1 import a, b, c1, c2
import matplotlib.pyplot as plt

def freq_params(a, b, fq, fs=256, N=100, show=True):
    fq -= 1 if  fq !=0 else 0
    c3 = "mediumslateblue"
    w, h = signal.freqz(b, a, worN=N, fs=fs)
    amp = abs(h)
    phase = np.unwrap(np.angle(h))

    if show:
        top = amp[fq] if amp[fq] > phase[fq] else phase[fq]
        low = min(amp) if min(amp) < min(phase) else min(phase)
        fig, ax = plt.subplots()
        ax.plot(amp, c1)
        ax.scatter(fq, amp[fq], c=c1, label=f"amp = {round(amp[fq], 3)}")
        ax.plot(phase, c2)
        ax.scatter(fq, phase[fq], c=c2, label=f"phase = {round(phase[fq], 3)}")
        ax.scatter(fq, low, c=c3, label=f"fq = {fq+1}")
        ax.plot([fq, fq], [top, low], c=c3, linestyle="--")
        ax.legend(loc='upper right', shadow=True)
        ax.set_ylabel('amplitude, phase')
        ax.set_xlabel('frequency')
        ax.grid(linestyle="--")
        plt.show()

    return amp[fq], phase[fq]

freq_params(a, b, 10)
