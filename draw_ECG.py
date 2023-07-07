import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from ECG_getter import get_signal, get_mini_ECG


def draw_on_ax(ax, ecg):
    signal = ecg
    ax.plot(signal)
    #ax.set_xticks(range(len(signal)))


if __name__ == "__main__":
    signal = get_mini_ECG()

    fig, axs = plt.subplots()
    draw_on_ax(axs, signal)
    plt.show()
