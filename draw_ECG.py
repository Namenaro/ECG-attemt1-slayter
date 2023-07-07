import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero
from ECG_getter import get_signal, get_mini_ECG


def make_arrows(axs):
    axs.xaxis.set_ticks_position('bottom')
    axs.yaxis.set_ticks_position('left')

    # make arrows
    axs.spines['left'].set_position('zero')
    axs.spines['right'].set_visible(False)
    axs.spines['bottom'].set_position('zero')
    axs.spines['top'].set_visible(False)
    axs.xaxis.set_ticks_position('bottom')
    axs.yaxis.set_ticks_position('left')
    axs.plot((1), (0), ls="", marker=">", ms=10, color="k",
             transform=axs.get_yaxis_transform(), clip_on=False)
    axs.plot((0), (1), ls="", marker="^", ms=10, color="k",
             transform=axs.get_xaxis_transform(), clip_on=False)


def draw_on_ax(ax, ecg):
    signal = ecg
    ax.plot(signal)
    ax.set_xticks(range(0,len(signal),5))


if __name__ == "__main__":
    signal = get_mini_ECG()

    fig, axs = plt.subplots()
    draw_on_ax(axs, signal)
    make_arrows(axs)
    plt.show()
