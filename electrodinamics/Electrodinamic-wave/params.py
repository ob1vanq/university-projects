import sys

import numpy as np

from plot import *
from app import prm, ab, var


np.seterr(divide='ignore')
file = open("data.txt", "w", encoding="utf-8")
sys.stdout = file

print(f"Варіант: {var}\n\n")
c = 2.998e8
a, b = ab
a *= 1e-3
b *= 1e-3
print(f"{a=}, {b=}")
# a = 47.6e-3
# b = 22.1e-3
# a = 28.5e-3
# b = 12.6e-3


def rounder(func):
    def wrapper(*args, **kwargs):
        return np.round(func(*args, **kwargs), 3)
    return wrapper


def wave_long(m, n, a, b): return 2/np.sqrt((m/a)**2 + (n/b)**2)
@rounder
def frequency(wave_long): return c/wave_long


long_10 = wave_long(1, 0, a, b)
long_20 = wave_long(2, 0, a, b)
freq_10 = frequency(long_10)
freq_20 = frequency(long_20)
f1 = 1.5*freq_10

print(f"Довжина хвилі (10): {long_10} м\n"
      f"Частота хвилі (10): {freq_10/1e9} ГГц\n\n"
      f"Довжина хвилі (20): {long_20} м\n"
      f"Частота хвилі (20): {freq_20/1e9} ГГц\n"
      f"Збільшена частота х1.5: {f1/1e9}\n")


A = (long_10/1.5)/np.sqrt(1 - (freq_10/f1)**2)
A_prostir = c/f1

f_10_2c = freq_10 * np.sqrt(4/3)
f_20_2c = freq_20 * np.sqrt(4/3)

print(f"Частоти при 2с:\nf10 = {f_10_2c/1e9}\nf20 = {f_20_2c/1e9}")

print(f"Довжина хвилі (х1.5): {A} м\n"
      f"Діапазон частот з подвійною фаз. швидкістю: [{f_10_2c/1e9} ГГц; {f_20_2c/1e9}] ГГц\n")

phase_velocity(freq_10, freq_20, f_10_2c, f_20_2c)
ph_vel = c/np.sqrt(1 - 4/9)
K = 2*np.pi*f1/ph_vel

import tabulate
table = [
    ["Значення", "У хвилеводі", "У вільному просторі"],
    ["Фазова швидкість [м/с]", f"{ph_vel/1e8}*10^8", f"{c/1e8}*10^8"],
    ["Довжина хвилі [см]", f"{A*100}", f"{A_prostir*100}"],
    ["Хвильове число [рад/м]", f"{K}", f"{2*np.pi*f1/c}"],
]
print(tabulate.tabulate(table, tablefmt='grid'), "\n")

z = power(K)
print(f"Відстань z: {z}\n")

fields(a, b, A,  A_prostir)

Zc = 120*np.pi
P = a**3*b*Zc/(A*A_prostir)
print(f"Потужність при H = 1 А/м: {P}\n")

mu, tau, mu2, tau2 = prm
print("Значення провідності та маг. проникності для: \n")
print(tabulate.tabulate([
    ["Параметр", "Алюміній", "Золото", "Мідь", "Срібло"],
    ["Провідність (tau) [См/м]", "3.8e7", "4.55e7", "5.7e7", "6.2e7"],
    ["Проникність (mu)", "1.00002", "0.999963", "0.999912", "0.999981"]
], tablefmt="grid"))
# tau = 3.8e7
# mu = 1.00002
delta = np.sqrt(1/(np.pi*f1*mu*(4*np.pi*1e-7)*tau))
damping_factor = (a + 2*b*(2/3)**2)/(2*tau*delta*Zc*a*b*np.sqrt(1 - 4/9))

print(f"дельта: {delta*1e6} мкм\n"
      f"коефіцієнт загасання = ({a} + 2*{b}*(2/3)**2)/(2*{tau}*{delta}*{Zc}*{a}*{b}*np.sqrt(1 - 4/9)) ="
      f"\n= {damping_factor} \n")

L = 10 * np.log10(np.exp(2*damping_factor))
print(f"Чисельне значення втрат: {L}\n\n")

# tau2 = 4.55e7
# mu2 = 0.999963
delta2 = np.sqrt(1/(np.pi*f1*mu2*(4*np.pi*1e-7)*tau2))
damping_factor2 = (a + 2*b*(2/3)**2)/(2*tau2*delta2*Zc*a*b*np.sqrt(1 - 4/9))
L = 10 * np.log10(np.exp(2*damping_factor2))

print(f"дельта: {delta2}\n"
      f"коефіцієнт загасання: {damping_factor2}\n"
      f"Чисельне значення втрат: {L}")

file.close()