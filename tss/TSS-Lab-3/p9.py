import numpy as np

from p1 import a, b, c1, c2
from scipy import signal
import matplotlib.pyplot as plt

w, h = signal.freqz(b, a, worN=100, fs=256)
fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(abs(h),  c1)
ax1.set_ylabel('Amplitude [dB]', color=c1)
ax1.set_xlabel('Frequency [rad/sample]')
ax1.grid(linestyle="--")

angles = np.unwrap(np.angle(h))
ax2.plot(angles, c2)
ax2.set_ylabel('Angle (radians)', color=c2)
ax2.set_xlabel('Frequency [rad/sample]')
ax2.grid(linestyle="--")
plt.show()

h = abs(h)
min = np.min(h)
ind = np.where(h == min)[0][0]
print(ind)

