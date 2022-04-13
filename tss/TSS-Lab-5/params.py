import numpy as np


class plot:
    grid_color = "g"
    color = "royalblue"

    @staticmethod
    def set_param(ax):
        for ax in ax.flat:
            ax.grid(color=plot.grid_color, linestyle="--")
            for lines in ax.get_lines():
                lines.set_color(plot.color)


class win:

    @staticmethod
    def parzen(n):
        from scipy.signal import windows as w
        return w.get_window(window="parzen", Nx=n)

    @staticmethod
    def triang(n):
        from scipy.signal import windows as w
        return w.get_window(window="triang", Nx=n)


def spectrum(signal, fs, full_period: bool = False, ph: bool = False):
    fft = np.fft.fft(signal)
    size = len(signal)
    if not full_period:
        size, fs = int(len(signal)/2), int(fs/2)
    t = np.linspace(0, fs, size)
    amp = abs(fft.real)
    phase = fft.imag
    if not ph:
        return (t, amp[:size]), size
    else:
        return (t, amp[:size]), (t, phase[:size]), size


def impulse(t: int, fs: int, tau: float, long: float, amp: float):
    start = int(tau * fs)
    end = int((tau + long) * fs)
    x = np.linspace(0, t, t * fs)
    y = np.zeros(t * fs)
    y[start:end] = amp
    return x, y