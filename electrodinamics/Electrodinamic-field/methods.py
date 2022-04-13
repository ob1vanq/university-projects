import locale
import imageio
import os

locale.setlocale(locale.LC_ALL, "uk_UA.utf8")

a_before = -1


def print_calc(v, string: str, i, j,  a, table=None, stop=1):
    if a+1 == stop:
        global a_before
        if a != a_before:
            a_before = a
            iter_str = f"\n\nIteration [{a + 1}]\n\n"
        else:
            iter_str = ""
        string = string.replace("i", "{i}")
        string = string.replace("j", "{j}")
        string = string.format(i=i, j=j)
        string += f" = {round(v, 3)}\n"
        if table:
            string += "\n" + table + "\n"

        with open("log/calc.txt", "a", encoding="utf8") as file:
            file.write(iter_str + string)


def create_gif():
    filenames = [f"data/{f}" for f in os.listdir("data/")]
    with imageio.get_writer(f'field.gif', mode='I', duration=0.5) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)

    for filename in filenames:
        os.remove(filename)

