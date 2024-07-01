import argparse
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("frequencies", type=int, nargs='+', help="frequencies of signals in Hz")
    parser.add_argument("-t", "--time", type=int, default= 1, help="signal time in s")
    args = parser.parse_args()

    frequencies = args.frequencies
    time = args.time
    lenght = 65536
    normalize = lenght / 2
    samples = np.linspace(0, time, lenght)
    freq_domain = np.fft.rfftfreq(lenght, 1 / (lenght//time))
    signal = np.sin(2 * np.pi * samples * frequencies[0])
    for i in range(1, len(frequencies)):
        signal += np.sin(2 * np.pi * samples * frequencies[i])
    fsignal = np.fft.rfft(signal)
    inv_signal = np.fft.irfft(fsignal)

    sns.set_theme(palette="colorblind", style="whitegrid", context="paper")
    fig = plt.figure(figsize=(16,9))
    fig.suptitle("Sygnał i jego przekształcenia")
    gs = plt.GridSpec(nrows=3, ncols=1)
    fig.add_subplot(gs[0,0])
    sns.lineplot(x=samples, y=signal, legend=None, color='C0').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał sinusoidalny")
    fig.add_subplot(gs[1,0])
    sns.lineplot(x=freq_domain, y=np.abs(fsignal)/normalize, legend=None, color='C1').set(xlabel="Częstotliwość [Hz]", ylabel="Amplituda [mV]", title="Widmo amplitudowe sygnału po transformacji Fouriera")
    fig.add_subplot(gs[2,0])
    sns.lineplot(x=samples, y=inv_signal, legend=None, color='C2').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał po odwrotnej transformacji Fouriera")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()