import numpy as np
from signals import create_signal, filter_signal
import matplotlib.pyplot as plt
from utils.plot_utils import plot_S, plot_t
from utils.sound_utils import record, play


def get_params():
    T = 13.23  # durata semnalului
    Te = 1 / 10000  # perioada de esantionare
    fm = 20  # o frecventa din componeta semnalului mesaj
    t = np.arange(0, T, Te)  # vectorul timp
    sm = 10 * t
    sound = record(seconds=3)
    flat_sound = []
    for sub_sound in sound:
        flat_sound.append(sub_sound[0])
    flat_sound = np.array(flat_sound)
    sm = sm + flat_sound
    modulated_signal = create_signal(T, Te, sm, t)
    plt.figure()
    plt.subplot(2, 1, 1)
    plot_t(Te, sm)
    plt.subplot(2, 1, 2)
    plot_S(Te, sm)
    plt.show()
    filtered_signal = filter_signal(modulated_signal, Te)

    # reprezentarea semnalului modulat
    plt.figure()
    plt.subplot(2, 1, 1)
    plot_t(Te, modulated_signal)
    plt.subplot(2, 1, 2)
    plot_S(Te, modulated_signal)
    plt.show()

    plt.figure()
    plt.subplot(2, 1, 1)
    plot_t(Te, filtered_signal)
    plt.subplot(2, 1, 2)
    plot_S(Te, filtered_signal)
    plt.show()


    signal_to_play = []
    for value in filtered_signal:
        signal_to_play.append([value])
    print(len(signal_to_play))
    play(np.array(signal_to_play))


get_params()
