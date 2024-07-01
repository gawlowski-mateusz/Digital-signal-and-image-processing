import argparse
from pathlib import Path
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def generate_plot_labels(columns):
    labels = []
    for column in range(columns):
        labels.append("Odprowadzenie " + str(column + 1))
    return labels

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="signal's filename. Must be in 'data' directory.")
    args = parser.parse_args()

    filename = args.file
    path = Path.cwd().parent.joinpath("data", filename)
    signals = np.loadtxt(path)

    fs = 1000
    lenght = signals.shape[0]
    samples = np.linspace(0, lenght//fs, lenght)
    signals = signals.transpose()

    plt.figure(figsize=(16,9))
    sns.set_theme(style="whitegrid", context="paper", palette=sns.color_palette("husl", 12))

    for signal in signals:
        sns.lineplot(x=samples, y=signal, errorbar=None, alpha=0.7).set(xlabel="Czas [s]", ylabel="Amplituda [mV]", title="Sygnał EKG")

    labels = generate_plot_labels(signals.shape[1])
    plt.legend(labels=labels, title="Odprowadzenia", loc=2, bbox_to_anchor= (1,1))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()