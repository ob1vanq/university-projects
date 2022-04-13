import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from methods import view_proccesing


class stabilogram:
    names = ["time_s", "top_left_f_kg", "top_right_f_kg", "bottom_left_f_kg",
             "bottom_right_f_kg", "cop_x", "cop_y", "total_f"]

    def __init__(self, path):
        try:
            self.file = pd.read_csv(path, delimiter=" ", names=stabilogram.names)
            self.time_s = self.file['time_s'] / 1000
        except:
            self.file = pd.read_csv(path, delimiter="\t", names=stabilogram.names)
            self.time_s = self.file['time_s'] / 1000
        self.top_left_f_kg = self.file['top_left_f_kg']
        self.top_right_f_kg = self.file['top_right_f_kg']
        self.bottom_left_f_kg = self.file['bottom_left_f_kg']
        self.bottom_right_f_kg = self.file['bottom_right_f_kg']
        self.cop_x = self.file['cop_x']
        self.cop_y = self.file['cop_y']
        self.total_f = self.file['total_f']
        self.path = path

    def all_parameters(self):
        return [stabilogram.data_params(self, sig) for sig in stabilogram.signals(self)]

    @staticmethod
    def table(data, title=" "):
        r = lambda data: round(data, 2)
        return [
            [f"{title}", " "],
            ["Середнє\nзначення", f"{r(np.mean(data))}"],
            ["Медіанне\nзначення", f"{r(np.median(data))}"],
            ["Квадратичне\nвідхилення", f"{r(np.std(data))}"]
        ]

    def signals(self):
        top = {
            "data": [self.time_s, self.top_left_f_kg, self.time_s, self.top_right_f_kg],
            "cellText": stabilogram.table(self.top_left_f_kg, "1") + stabilogram.table(self.top_right_f_kg, "2"),
            "label": ["top_left_f_kg - 1", "top_right_f_kg - 2"],
            "title": "raw top left, right sensor data kg"
        }
        bottom = {
            "data": [self.time_s, self.bottom_left_f_kg, self.time_s, self.bottom_right_f_kg],
            "cellText": stabilogram.table(self.bottom_left_f_kg, "1") + stabilogram.table(self.bottom_right_f_kg, "2"),
            "label": ["bottom_left_f_kg - 1", "bottom_right_f_kg - 2"],
            "title": "raw bottom left, right sensor data  kg"
        }
        cop = {
            "data": [self.time_s, self.cop_x, self.time_s, self.cop_y],
            "cellText": stabilogram.table(self.cop_x, "1") + stabilogram.table(self.cop_y, "2"),
            "label": ["cop_x - 1", "cop_y - 2"],
            "title": "cop x, y axis, cm"
        }
        total = {
            "data": [self.time_s, self.total_f],
            "cellText": stabilogram.table(self.cop_x, "total_f"),
            "label": ["total_f", "total_f"],
            "title": "total force"
        }
        return [top, bottom, cop, total]

    def data_params(self, data):
        return {
            "data": data.get("data"),
            "params": {
                "label": data.get("label"),
            },
            "title": data.get("title"),
            "suptitle": f"Завантажено з {self.path}",
            "table": {
                "cellText": data.get("cellText"),
                "bbox": [1, 0, 0.3, 1],
                "colWidths": [0.9, 0.35]
            }
        }


def plot(data, path, f, show=False):
    fig, axs = plt.subplots(2, 2, figsize=(14, 7))
    i = 0
    plt.suptitle(data[i].get("suptitle"), fontweight="bold")
    for ax in axs.flat:

        ax.plot(*data[i].get("data"))
        ax.set(xlabel="Час, c", title=data[i].get("title"))
        table = ax.table(**data[i].get("table"))
        table.auto_set_font_size(False)
        table.set_fontsize(9)
        ax.legend(data[i].get("params").get("label"))
        ax.grid(linestyle='--', color='grey')
        file_name = r"{}{}.png".format(path, f)
        fig.savefig(file_name, bbox_inches='tight')
        i += 1
    if show:
        plt.show(block=False)
        plt.pause(1)
        plt.close(fig)
    else:
        plt.close(fig)


def run():
    show = False
    files = ["datas/acrobats/base_open/" + str(path) for path in os.listdir(r"datas/acrobats/base_open/")]
    files += ["datas/acrobats/sway_left-right_60/" + str(path) for path in
              os.listdir(r"datas/acrobats/sway_left-right_60/")]
    files += ["datas/handball/base_open/" + str(path) for path in os.listdir(r"datas/handball/base_open/")]
    files += ["datas/handball/sway_left-right_60/" + str(path) for path in
              os.listdir(r"datas/handball/sway_left-right_60/")]

    print(f"Починаю зберігати файли у datas/пункт6/ Всього графіків: {len(files)}\n")
    if str(input("Відображати всі графіки? [y/n]: ")).lower() == "y":
        show = True
    print()
    timer = view_proccesing(len(files))
    f = 0
    for csv in files:
        timer.load_line()
        csv = stabilogram(r"{}".format(csv))
        plot([sig for sig in csv.all_parameters()], "datas/пункт6/", f=f, show=show)
        f += 1
    print()
