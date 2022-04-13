import numpy as np
from p2 import t, y, z_null, c1, c2
import matplotlib.pyplot as plt


def ku(signals, diapason, fs=10, show_peaks=True):

    """
    :param signals: array_of_tuples [(x1, y1), (x2,y2)]
    :param diapason: tuple_of_int (start, end, precision)
    :param fs: sampling frequency int
    :param show_peaks: bool, plot signals with peaks
    """

    start_index, end_index = [], []
    start, end, pr = diapason
    s1, s2 = signals
    x1, y1 = s1
    x2, y2 = s2

    # Використання даного блоку коду доцільне, оскільки при малих частотах дискретизації періодичні функції
    # мають не рівномірно однакове заповненя, тобто масимуми по амплітуді, можуть бути знайдені із похибкою
    # операція нижче дозволяє обраховувати лише заданий відрізок сигналу
    for xs in [x1, x2]:
        ind1, ind2 = True, True
        precision = pr
        while precision > 0:
            for x in xs:
                if round(x, precision) == start and ind1:
                    start_index.append(np.where(x1 == x)[0][0])
                    ind1 = False
                if round(x, precision) == end and ind2:
                    end_index.append(np.where(x1 == x)[0][0])
                    ind2 = False
            precision -= 1

    s1, s2 = start_index
    e1, e2 = end_index
    max1 = np.max(y1[s1:e1])
    t1 = x1[np.where(y1 == max1)[0][0]]
    max2 = np.max(y2[s2:e2])
    t2 = x2[np.where(y2 == max2)[0][0]]

    if show_peaks:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x1, y1, c=c1)
        ax.plot(x2, y2, c=c2)
        ax.scatter(t1, max1, c=c1)
        ax.scatter(t2, max2, c=c2)
        ax.set(xlabel="t, с", ylabel="амплітуда")
        ax.grid(linestyle="--")
        fig.savefig("data/point 3.png")
        plt.show()
        plt.close()

    return max2/max1, (t2-t1)*fs*2*np.pi


ku, phase = ku(signals=[(t, y), (t, z_null)], diapason=(0.0, 0.1, 3))
print(f"{ku=}, {phase=}")