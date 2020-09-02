import numpy as np
from scipy import signal


def filter_signal(sM, Te):
    fe = 1 / Te
    ff = [0, 500, 1000, 4000]  # freceventele profilului filtrului
    af = [5, 0]  # palierele amplitudii filtrului
    nf = 100  # dimensiunea filtrului
    b = signal.remez(nf, ff, af, Hz=fe)  # coeficientii filtrului

    filtered_signal = signal.lfilter(b, 1, np.abs(sM))  # iesirea filtrului

    return filtered_signal


def create_signal(T, Te, sm, t):
    fe = 1 / Te  # frecventa de esantionare
    L = len(t)  # numarul de esantioane

    fp = 1000  # frecventa purtatoarei
    sp = np.cos(2 * np.pi * fp * t)  # semnalul purtator

    sM = sp * sm + sp  # semnalul modulat

    return sM
