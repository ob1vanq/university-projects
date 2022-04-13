import numpy as np


def akf(sig):
    sig_size = len(sig)
    sig = np.append(sig, np.zeros(sig_size-1))
    b_denom = (1 / sig_size) * np.sum(np.array([sig[n] ** 2 for n in range(sig_size)]))

    r = lambda j: (1/sig_size) * np.sum(np.array([sig[n]*sig[n-j] for n in range(sig_size)]))
    b = lambda j: r(j) / b_denom
    return list(map(b, np.arange(0, sig_size, 1)))


def vkf(x1, x2):
    sig_size = len(x1)
    x1 = np.append(x1, np.zeros(sig_size-1))
    x2 = np.append(x1, np.zeros(sig_size-1))
    b_denom = (1 / sig_size) * np.sum(np.array([np.sqrt(x1[n]**2 * x2[n]**2) for n in range(sig_size)]))

    def r(j):
        return (1/sig_size) * np.sum(np.array([x1[n]*x2[n-j] for n in range(sig_size)]))

    def b(j):
        return r(j) / b_denom
    return list(map(b, np.arange(0, sig_size, 1)))


def mirror(array, with_minus: bool = False):
    n = len(array)
    if with_minus:
        array = np.append(-np.array(array[::-1][:n - 1]), array)
    else:
        array = np.append(array[::-1][:n - 1], array)
    return array


def impulse(time: int, fs: int, tau: float, long: float, amp: float):
    start = int(tau * fs)
    end = int((tau + long) * fs)
    y = np.zeros(time * fs)
    y[start:end] = amp
    return y