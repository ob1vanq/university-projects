import os

import imageio
import matplotlib.pyplot as plt
import numpy as np

from potentials import v, x, y, v2, v3
from field import Ex, Ey
from timer import ViewProcessing



strs = """
'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper'"""
print(strs)
color = str(input("\ncmap >> "))
color2 = str(input("color >> "))

if color2 == "":
    color2 = "black"
if color == "":
    color = "cool"

e = -1
fig, ax = plt.subplots(figsize=(10, 7))
ax.quiver(x, y, Ex, Ey, alpha=1)
ax.set(xlabel="x, мкм", ylabel="y, мкм", title="Вектори напруженості електричного поля")
fig.savefig(r"data/field.png")
plt.close()

fig, ax = plt.subplots(figsize=(10, 7))
c = ax.contour(x, y, np.round(v, 2), levels=np.linspace(v2, v3, round(int((abs(v2) + v3)/0.1), 2)), cmap=color)
ax.clabel(c, inline=1, fontsize=10, fmt='%1.1f')
# fig.colorbar(c, shrink=1, aspect=10)
ax.set(xlabel="x, мкм", ylabel="y, мкм", title="Еквіпотенціальні лінії")
fig.savefig(r"data/lines.png")
plt.close()

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(x, y, e*v, linewidth=0, antialiased=False, cmap=color)
ax.view_init(25, 130)
ax.plot_wireframe(x, y, e*v, color=color2)
ax.set(xlabel="x, мкм", ylabel="y, мкм", zlabel="U, eВ", title="Потенціальний рельєф")
ax.view_init(30, -75)
fig.savefig(r"data/3d_1.png")
ax.view_init(-112, -190)
fig.savefig(r"data/3d_2.png")
plt.tight_layout()
plt.show()
plt.close()

t = 360
if str(input("make gif[y/n] >> ")).lower() == "y":
    print()
    timer = ViewProcessing(t, title="Создаю гифку")
    with imageio.get_writer(f'field.gif', mode='I', duration=10/t) as writer:
        for ang in range(t):
            timer.load_line()
            path = "gif_data/3d{}.png".format(ang)
            fig = plt.figure(figsize=(10, 7))
            ax = fig.add_subplot(projection='3d')
            surf = ax.plot_surface(x, y, e*v, linewidth=0, antialiased=False, cmap=color)
            ax.view_init(25, 130+ang)
            ax.plot_wireframe(x, y, e*v, color=color2)
            ax.set(xlabel="j", ylabel="i", zlabel="E, eВ", title="Потенціальний рельєф")
            fig.savefig(path)
            plt.close()
            image = imageio.imread(path)
            writer.append_data(image)
            os.remove(path)
else:
    pass
print()


