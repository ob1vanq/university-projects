# Прочитати сигнали значення серцевого ритму (HR) та сатурації артеріальної
# крові киснем (SpO2). Побудувати графіки обох сигналів. Побудувати графіки середніх
# значень сигналів, які обраховані у вікнах тривалістю 30 сек., вікна не
# перекриваються.
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from methods import view_proccesing


class HeartSignal:

    def __init__(self, path=r"datas/signals/Subject1_SpO2Hr.csv"):
        self.path = path
        file = pd.read_csv(path, delimiter=",")
        time_s = file['Elapsed time(seconds)']
        self.spo2 = [time_s, file['SpO2(%)']]
        self.hr_bpm = [time_s, file['hr (bpm)']]

    def data(self):
        return {
            "data": [self.spo2, HeartSignal.avg(self.spo2[-1]), self.hr_bpm, HeartSignal.avg(self.hr_bpm[-1])],
            "title": ["Cатурація артеріальної крові киснем (SpO2)", "Середнє значення SpO2",
                      "Серцевий ритм (HR)", "Середнє значення HR"],
            "suptitle": f"Завантажено з {self.path}"
        }

    @staticmethod
    def avg(data, T=30):
        time = int(len(data) / T)
        avg_data = []
        for i in range(time):
            const = np.mean(data[T * (i - 1):T * i])
            i += 1
            avg_data += [const for j in range(30)]
        return [np.linspace(0, time * T, time * T), avg_data]

    def plot(self, show=False):
        data = [self.spo2, HeartSignal.avg(self.spo2[-1]), self.hr_bpm, HeartSignal.avg(self.hr_bpm[-1])]
        title = ["Cатурація артеріальної крові киснем (SpO2)", "Середнє значення SpO2",
                 "Серцевий ритм (HR)", "Середнє значення HR"]
        fig, axs = plt.subplots(2, 2, figsize=(14, 6))

        i = 0

        for ax in axs.flat:
            ax.plot(*data[i])
            ax.grid(linestyle='--', color='grey')
            ax.set(xlabel="Час, с", title=title[i])
            i += 1
        plt.suptitle(f"Завантажено з {self.path}", fontweight="bold")
        plt.tight_layout()
        file_name = f"datas/пункт7/{self.path.split('/')[-1].split('.')[0]}"
        fig.savefig(file_name, bbox_inches='tight')
        if show:
            plt.show(block=False)
            plt.pause(1)
            plt.close(fig)
        else:
            plt.close(fig)

def run():
    files = os.listdir(r"datas/signals/")
    show = False
    print(f"Починаю зберігати файли у datas/пункт6/ Всього графіків: {len(files)}\n")
    if str(input("Відображати всі графіки? [y/n]: ")).lower() == "y":
        show = True
    print()
    timer = view_proccesing(len(files))
    for file in files:
        timer.load_line()
        sig = HeartSignal(r"datas/signals/"+file)
        sig.plot(show)
    print()
