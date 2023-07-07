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


def draw_prediction(ax, point, val):
    ax.vlines(x=point, ymin=0, ymax=val, colors='orange', lw=2, label='предсказание')

def draw_slayter_indexes(ax, points, vals):
    slayter_vals = list([vals[i] for i in points])
    ax.scatter(points, slayter_vals, color='green', label="слейтер фронт")

def draw_bassin(ax, vals, point_1=None, point_2=None):
    h = max(vals)
    b = min(vals)
    if point_1 is None:
        point_1=0
    if point_2 is None:
        point_2 = len(vals)
    ax.axvspan(0, point_1, facecolor='0.2', alpha=0.5)
    ax.axvspan(point_2, len(vals), facecolor='0.2', alpha=0.5)


if __name__ == "__main__":
    signal = get_mini_ECG()

    fig, axs = plt.subplots()
    draw_on_ax(axs, signal)
    make_arrows(axs)

    point=20
    val = signal[point]

    draw_prediction(axs, point, val)

    draw_slayter_indexes(axs, points=[20, 21, 22, 23], vals=signal)

    draw_bassin(axs, signal, point_1=5, point_2=30)

    axs.legend(fancybox=True, framealpha=0.5)
    plt.show()
