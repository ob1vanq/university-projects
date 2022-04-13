import numpy as np


def impulse(time: int, fs: int, tau: float, long: float, amp: float):
    start = int(tau * fs)
    end = int((tau + long) * fs)
    y = np.zeros(time * fs)
    y[start:end] = amp
    return y


def spectrum(signal, fs, full_period: bool = False, ph: bool = False):
    fft = np.fft.fft(signal)
    size = len(signal)
    if not full_period:
        size, fs = int(len(signal)/2), int(fs/2)
    t = np.linspace(0, fs, size)
    amp = abs(fft.real)*4/fs
    phase = fft.imag
    if not ph:
        return (t, amp[:size])
    else:
        return (t, amp[:size]), (t, phase[:size]), size


# Для всіх завдань програмно будувати: графік початкового сигналу та його
# амплітудного спектру, графік шуму та його амплітудного спектру, графік зашумленого
# сигналу (вхідного сигналу фільтра) та його амплітудного спектру, графік АЧХ фільтра,
# графік відфільтрованого сигналу та його амплітудного спектру.
# Для всіх фільтрів максимальний припустимий коефіцієнт передачі на частоті зрізу
# обрати 3 дБ, а мінімальний припустимий коефіцієнт передачі на частоті затримки обрати
# так, щоб порядок фільтра був не менше 5-го та не більше 10-го.

def plot(signals, path):
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(12, 10))

    signal = plt.subplot2grid((5, 5), (0, 0), colspan=3)
    signal_amp = plt.subplot2grid((5, 5), (0, 3), colspan=2)
    noise = plt.subplot2grid((5, 5), (1, 0), colspan=3)
    noise_amp = plt.subplot2grid((5, 5), (1, 3), colspan=2)
    noised_sig = plt.subplot2grid((5, 5), (2, 0), colspan=3)
    noised_amp = plt.subplot2grid((5, 5), (2, 3), colspan=2)
    filter_amp = plt.subplot2grid((5, 5), (3, 0), colspan=5)
    filtered_sig = plt.subplot2grid((5, 5), (4, 0), colspan=3)
    filtered_sig_amp = plt.subplot2grid((5, 5), (4, 3), colspan=2)

    title = ["Вхідний сигнал", "АЧХ вхідного сигналу",
             "Сигнал шуму", "АЧХ шуму",
             "Зашумлений сигнал", "АЧХ зашумленого сигналу",
             "АЧХ фільтру", "Відфільтрований сигнал", "АЧХ відфільтрованого сигналу"]

    for ax, i in zip([signal, signal_amp, noise, noise_amp, noised_sig, noised_amp,
                      filter_amp, filtered_sig, filtered_sig_amp], range(9)):
        ax.plot(*signals[i], "b")
        ax.grid(linestyle="--", color="g")
        ax.set_title(title[i])
    plt.tight_layout()
    fig.savefig(path)
    return plt