# Записати звук з зовнішнього пристрою тривалістю 5 с допомогою Python.
# Записати однакові фрази або музику з частотою дискретизації 8 кГц та 44.1 кГц.
# Прочитати з файлу та прослухати отримані записи. Вивести графік, позначити вісі.

import os
from datetime import datetime
from methods import view_proccesing

import numpy as np
import pyaudio
import wave


def wav_processing(suptitle="", seconds=5, *, path):
    import matplotlib.pyplot as plt

    wav = wave.open(path, "r")
    raw = wav.readframes(-1)
    raw = np.frombuffer(raw, np.int16)

    t = np.linspace(0, seconds, len(raw))

    fig, ax = plt.subplots()
    ax.plot(t, raw)
    ax.plot(t, np.zeros(len(raw)), 'orange')
    plt.suptitle(f"Завантажено з '{path}', " + suptitle, fontweight="bold")
    ax.set(xlabel='час, с', ylabel='амплітуда')
    ax.grid(linestyle='--', color='grey')
    ax.minorticks_on()
    file_name = r"datas/пункт2/{}.png".format(suptitle)
    file_dir = os.path.abspath(os.curdir) + r"datas\пункт2\{}.png".format(suptitle)
    print(f"\nЗберігаю у: {file_dir}")
    plt.tight_layout()
    fig.savefig(file_name, bbox_inches='tight')
    plt.show()

    return [t, raw]


def record(seconds=5, title=""):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 2
    rate = 44100
    record_seconds = seconds
    wave_output_filename = f"datas/output{title} {rate}Hz.wav"
    p = pyaudio.PyAudio()

    for file in os.listdir():
        if file == wave_output_filename:
            os.remove(file)

    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)
    input("Натисність Enter щоб почати запис...\n")
    print(f"Запис увімкнено ({record_seconds}) сек")
    now = datetime.now().second
    frames = []
    timer = view_proccesing(rate / chunk * record_seconds)

    for i in range(timer.end):
        timer.load_line()
        data = stream.read(chunk)
        frames.append(data)
    print("\nЗапис завершено!")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(wave_output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    wav_processing(path=wave_output_filename)


def run(is_record: bool = False):
    if is_record:
        record(title="1")
    wav_processing(suptitle="пункт 2.1", path=r"datas/output 44100Hz.wav")
    wav_processing(suptitle="пункт 2.2", path=r"datas/output 8000Hz.wav")
