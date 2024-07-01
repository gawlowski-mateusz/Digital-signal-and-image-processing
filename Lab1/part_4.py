import argparse
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import fft, signal

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="signal's filename. Must be in 'data' directory.")
    args = parser.parse_args()

    filename = args.file
    path = Path.cwd().parent.joinpath("data", filename)
    data = np.loadtxt(path)

    time, signl = data.T
    lenght = len(signl)
    normalize = lenght / 2
    fs = lenght // time[-1]
    freq_domain = fft.rfftfreq(lenght, 1 / fs)

    lowcut = 5
    highcut = 60
    order = 7
    fsignal = fft.rfft(signl)

    sosl = signal.butter(N=order, Wn=highcut, btype='lowpass', analog=False, output='sos', fs=fs)
    wl, hl = signal.sosfreqz(sos=sosl, fs=fs)
    lsignal = signal.sosfiltfilt(sos=sosl, x=signl)
    flsignal = fft.rfft(lsignal)

    sosh = signal.butter(N=order, Wn=lowcut, btype='highpass', analog=False, output='sos', fs=fs)
    wh, hh = signal.sosfreqz(sos=sosh, fs=fs)
    hsignal = signal.sosfiltfilt(sos=sosh, x=signl)
    fhsignal = fft.rfft(hsignal)

    sns.set_theme(palette="colorblind", style="whitegrid", context="paper")
    fig = plt.figure(figsize=(16,9))
    fig.suptitle("Demonstracja filtracji sygnału EKG")
    gs = plt.GridSpec(nrows=3, ncols=3)
    fig.add_subplot(gs[1,0])
    sns.lineplot(x=time, y=signl, legend=None, color='C0').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał EKG z szumem")
    fig.add_subplot(gs[2,0])
    sns.lineplot(x=freq_domain, y=np.abs(fsignal)/normalize, legend=None, color='C1').set(xlabel="Częstotliwość [Hz]", ylabel="Amplituda [mV]", title="Widmo amplitudowe sygnału")
    fig.add_subplot(gs[0,1])
    sns.lineplot(x=wl, y=abs(hl), legend=None, color='C2').set(xlabel="Częstotliwość [Hz]", ylabel="Tłumienie [dB]", title="Filtr dolnoprzepustowy")
    fig.add_subplot(gs[0,2])
    sns.lineplot(x=wh, y=abs(hh), legend=None, color='C2').set(xlabel="Częstotliwość [Hz]", ylabel="Tłumienie [dB]", title="Filtr górnoprzepustowy")
    fig.add_subplot(gs[1,1])
    sns.lineplot(x=time, y=signl, legend=None, color='C9', alpha=0.7)
    sns.lineplot(x=time, y=lsignal, legend=None, color='C0').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał EKG po filtracji dolnoprzepustowej")
    fig.add_subplot(gs[1,2])
    sns.lineplot(x=time, y=signl, legend=None, color='C9', alpha=0.7)
    sns.lineplot(x=time, y=hsignal, legend=None, color='C0').set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał EKG po filtracji górnoprzepustowej")
    fig.add_subplot(gs[2,1])
    sns.lineplot(x=freq_domain, y=np.abs(flsignal)/normalize, legend=None, color='C1').set(xlabel="Częstotliwość [Hz]", ylabel="Amplituda [mV]",
                                                                                           title="Widmo amplitudowe sygnału po filtracji dolnoprzepustowej")
    fig.add_subplot(gs[2,2])
    sns.lineplot(x=freq_domain, y=np.abs(fhsignal)/normalize, legend=None, color='C1').set(xlabel="Częstotliwość [Hz]", ylabel="Amplituda [mV]",
                                                                                           title="Widmo amplitudowe sygnału po filtracji górnoprzepustowej")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()