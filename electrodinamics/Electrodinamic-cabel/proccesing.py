import sys
print("Номер варіанту >> ")
file = open("data.txt", "w", encoding="utf-8")
sys.stdout = file

from variants import eps, f, d, D, l, Zn
import numpy as np


d = d * 10 ** -3
D = D * 10 ** -3
l = l * 10 ** -2

Z0 = 25 * round((60 * np.log(D/d)/np.sqrt(eps))/25)
p = (Zn - Z0) / (Zn + Z0)
print(f"Z0 = {60 * np.log(D/d)/np.sqrt(eps)} = {Z0}")
print(f"p = {Zn - Z0}/{Zn + Z0} = |{np.round(p, 3)}| = {round(abs(p), 3)}")
p_complex = p
faz = np.arctan(p_complex.imag/p_complex.real)
print(f"фаза = atan({np.round(p_complex.imag, 3)}/{np.round(p_complex.real, 3)}) = {faz} = {round(faz*180/np.pi)} ")
p = round(abs(p), 3)

ksx = round((1+p)/(1-p), 3)
print(f"КСХ = (1 + {p})/(1 - {p}) = {1+p}/{round(1-p, 3)} = {ksx}")
k = round(2*np.pi*f*np.sqrt(eps)/(3*10**8), 3)
print(f"k = {k}")
Z_start = Z0 * ((Zn + 1j * Z0 * np.tan(l * k)) / (Z0 + 1j * Zn * np.tan(l * k)))
print(f"Zвх = {Z0} * ({Zn} + 1j*{Z0}*tan({l} * {k}))/({Z0} + 1j*{Zn}*tan({l * k})) ="
      f"\n= {np.round(Z0 * (Zn + 1j * Z0 * np.tan(l * k)),4)}/{np.round((Z0 + 1j * Zn * np.tan(l * k)),4)} "
      f"= {np.round(Z_start,4)}")

wave_long = round(2*np.pi/k, 1)
print(f"Довжина хвилі λ = {wave_long} м")
x1 = np.linspace(0, l, 1000)
x2 = np.linspace(0, wave_long, 1000)
x3 = np.linspace(0, wave_long/2, 1000)

Vm = lambda x: abs(1 + p_complex*np.exp(-2j*k*x))
Im = lambda x: abs(1 - p_complex*np.exp(-2j*k*x))

import matplotlib.pyplot as plt
import colorset

c1, c2 = colorset.colors.random(2, alpha_limit=(2,3))
c3 = colorset.colors.get("gr", 2, colorset.colors.line_colors)
# c1, c2, c3 = "royalblue", "lime", "grey"
fig, ax = plt.subplots(2, 1, figsize=(12, 7))

ax[0].plot(x1, Vm(x1), c=c1)
ax[0].plot(x1, Im(x1), c=c2)
ax[0].legend(['$V_m(x)/V_m^{+}$', '$I_m(x)/I_m^{+}$'], fontsize=14)
ax[0].set(title="Розподіл нормованих амплітуд струму та напруги по довжині кабеля (лінії)",
       xlabel = "x, м", ylabel="Нормовані амплітуди")
ax[1].plot(x2, Vm(x2), c=c1)
ax[1].plot(x2, Im(x2), c=c2)
ax[1].legend(["$V_m(x)/V_m^{i}$", "$I_m(x)/I_m^{i}$"], fontsize=14)
ax[1].set(title="Розподіл нормованих амплітуд струму та напруги по довжині хвилі",
       xlabel = "x, м", ylabel="Нормовані амплітуди")
for ax in ax.flat:
    ax.grid(linestyle="--", color=c3)
plt.tight_layout()
fig.savefig("1.png")
plt.close()

Z = lambda x: Z0 * (Zn + Z0 * 1j * np.tan(k * x)) / (Z0 + Zn * 1j * np.tan(k * x))

fig = plt.figure(figsize=(16, 6))
ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=2)
ax2 = plt.subplot2grid((1, 3), (0, 2), colspan=1)
ax1.plot(x1, Z(x1).real, c=c1)
ax1.plot(x1, Z(x1).imag, c=c2)
ax1.grid(linestyle="--", color=c3)
ax1.set(xlabel = "x, м", ylabel="Опір")
ax1.set_title("Розподіл нормованих активного та реактивного опорів\nпо довжині кабеля (лінії)", fontsize=15)
Z3r = Z(x3).real
Z3i = Z(x3).imag
ax2.plot(x3, Z3r, c=c1)
ax2.plot(x3, Z3i, c=c2)
ind = np.argwhere(np.diff(np.sign(Z0-Z(x3).real))).flatten()[0]
ax2.axvline(x3[ind], color=c3)
ax2.plot([0, wave_long/2], [Z0, Z0], c=c3)
ax2.plot(x3[ind], Z3r[ind], 'o', markeredgecolor=c1, c=c1)
ax2.plot(x3[ind], Z3i[ind], 'o', markeredgecolor=c2, c=c2)
ax2.set(xlabel = "x, м")
ax2.set_title("Розподіл в межах половини\nдовжини хвилі", fontsize=15)
ax2.legend(['$Re(Z(x))$', '$Im(Z(x))}$', '$Z_0$'], fontsize=14)
ax2.grid(linestyle="--", color=c3)
plt.tight_layout()
fig.savefig("2.png")

print(f"Відстань шлейфа (точка шлейфа x*) = {np.round(x3[ind],3)} м = {100*np.round(x3[ind],3)} cм\n"
      f"Реактивний опір шлейфа = {np.round(Z3i[ind], 3)}j, {-np.round(Z3i[ind])} Ом")
l_shl = np.round(1/k*(np.arctan(Z3i[ind]/(Z0))), 4)

print(f"Довжина шлейфу l = {l_shl} м = {100*abs(l_shl)} cм")

file.close()