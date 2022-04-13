# Створити функцію, яка розраховує тривалість сигналів. З її допомогою
# визначити тривалості всіх сигналів, що використовуються в роботі.
import sys


class signal_width():

    def __init__(self, start=0, sample_rate=256,*, data):
        self.data = data
        self.size = len(self.data)
        self.sample_rate = sample_rate
        self.width = int(self.size / self.sample_rate)
        self.linspace = {
            'start': start,
            'stop': self.width,
            'num': self.size}


class view_proccesing():

    def __init__(self, end, line_size=20, title="Залишилось"):
        self.title = title
        self.line_size = line_size
        self.end = int(end)
        self.counter = 1
        self.percent = lambda: f" {round((self.counter / self.end) * 100, 2)}%]"
        self.line = lambda stik=0, space=10: f"[{self.title}: |{'█' * stik + ' ' * space}|"

    def load_line(self):
        stick = int(self.line_size * self.counter / self.end)
        space = self.line_size - stick - 1
        sys.stdout.write("\r" + f"{self.line(stick, space)}" + self.percent())
        self.counter += 1
