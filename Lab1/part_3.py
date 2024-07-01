import argparse
from pathlib import Path
import numpy as np
from scipy import fft
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="signal's filename. Must be in 'data' directory.")
    args = parser.parse_args()

    filename = args.file
    path = Path.cwd().parent.joinpath("data", filename)
    signal = np.loadtxt(path, dtype=float)

    fs = 360
    lenght = signal.shape[0]
    normalize = lenght / 2
    samples = np.linspace(0, lenght//fs, lenght)
    freq_domain = fft.rfftfreq(lenght, 1/fs)
    fsignal = fft.rfft(signal)
    inv_signal = fft.irfft(fsignal)

    sns.set_theme(palette="colorblind", style="whitegrid", context="paper")
    fig = plt.figure(figsize=(16,9))
    fig.suptitle("Sygnał EKG i jego przekształcenia")
    gs = plt.GridSpec(nrows=3, ncols=1)
    fig.add_subplot(gs[0,0])
    sns.lineplot(x=samples, y=signal, legend=None, color='C0').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał EKG")
    fig.add_subplot(gs[1,0])
    sns.lineplot(x=freq_domain, y=np.abs(fsignal)/normalize, legend=None, color='C1').set(xlabel="Częstotliwość [Hz]", ylabel="Amplituda [mV]", title="Widmo amplitudowe sygnału")
    fig.add_subplot(gs[2,0])
    sns.lineplot(x=samples, y=inv_signal, legend=None, color='C2').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał po odwrotnej transformacji Fouriera")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()