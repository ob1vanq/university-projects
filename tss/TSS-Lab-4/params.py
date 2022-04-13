import numpy as np


def spectrum(signal, full_period=False, phase=False):
    amp = np.fft.fft(signal)
    if not phase:
        amp = abs(amp.real)
    if full_period:
        return amp
    return amp[:int(len(amp) / 2)]


c1, c2 = "royalblue", "springgreen"