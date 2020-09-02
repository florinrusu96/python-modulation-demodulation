import numpy as np
from scipy import signal
from scipy.fftpack import fft, fftshift
import matplotlib.pyplot as plt

def plot_t(Te, s, title=""):
    ''' Te reprezinta perioada de esantionare in secunde iar s este vectorul care contine esantioanle
        Functia va trasa grafic variatia semnalului in timp
    '''
    t=np.arange(0, s.size*Te, Te) # timpul este de la 0 pana la numarul de esantioane*Te, cu pasul Te
    plt.plot(t,s)
    plt.title(title)
    plt.xlabel("Timp [s]")
    plt.ylabel("Amplitudine [u.m., ex:mV]")
    
def plot_S(Te, s, title=""):
    ''' Te reprezinta perioada de esantionare in secunde iar s este vectorul care contine esantioanle
        Functia va trasa grafic spectrul semnalului
    '''
    N = s.size  # Numarul de esantione
    Np2 = N/2   # Jumatate din numarul de esantionae (la semnalele reale spectrul este o functie para)
    fe = 1/Te  # Frecventa de esantionare [Hz]
    delta_f = fe/N  # distanta dintre esantioanele spectrului
    f_max= Np2*delta_f # frecventa maxima a reprezentarii spectrului
    f_min = -f_max  # frecventa minima a reprezentarii spectrului, reprezentarea este simetrica
    f = np.arange(f_min, f_max, delta_f) # ar trebui sa fie N puncte pe axa frecventelor, de la f_min la f_max
                                         # cu pasul delta_f
    S=fft(s)  # Se calculeaza TFD cu FFT
    S=fftshift(S) # Se deplaseaza circular spectrul pentru a avea originea la mijlocul reprezentarii
    S=np.abs(S)  # Reprezentam doar modulul (atentie, este vb de modulul in sensul complex, nu partea pozitiva)
    plt.plot(f,S)
    plt.title(title)
    plt.xlabel("Frecventa [Hz]")
    plt.ylabel("Modul")   