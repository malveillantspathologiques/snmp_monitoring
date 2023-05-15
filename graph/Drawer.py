import matplotlib.pyplot as plt
import numpy as np


def draw_if(if_stat):
    conso_in = []
    conso_out = []
    if_name = []
    for desc, stats in if_stat.items():
        if stats[2] > 0 and stats[3] > 0:
            if_name.append(desc)
            conso_in.append(stats[2])
            conso_out.append(stats[3])

    axe_x = np.arange(len(if_name))
    plt.bar(axe_x - 0.05, conso_in, 0.1, label="Download")
    plt.bar(axe_x + 0.05, conso_out, 0.1, label="Upload")

    plt.xticks(axe_x, if_name, rotation=90)
    plt.xlabel("Nom des interfaces")
    plt.ylabel("Consommation en milliards d'octets")
    plt.title("Consommation totale de chaque interface")
    plt.legend()
    plt.show()


def draw_disks(disk_status, time_list):
    for disk, percent in disk_status.items():
        plt.plot(np.arange(len(percent)), percent, label=disk)
    plt.xticks(np.arange(len(time_list)), time_list, rotation=40, horizontalalignment='right')
    plt.xlabel("Temp passé par tranche de 5 min")
    plt.ylabel("Pourcentage d'espace occupé sur les disques")
    plt.title("Utilisation des disques")
    plt.legend()
    plt.show()


def draw_cpu_and_ram(ram_stats, la_loads):
    plt.plot(np.arange(len(ram_stats)), ram_stats, label="RAM")
    plt.plot(np.arange(len(la_loads)), la_loads, label="CPU")
    plt.xlabel("Temp passé par tranche de 5 min")
    plt.ylabel("Pourcentage d'utilisation")
    plt.title("Consommation du cpu et de la ram")
    plt.legend()
    plt.show()


def draw_processes(names, conso_cpu, conso_ram):
    axe_x = np.arange(len(names))

    # ToDo
    # sorted_merge = sorted(conso_merge, reverse=True, key=lambda x: liste[0] + liste[1]) / 2))

    plt.bar(axe_x - 0.1, conso_cpu, 0.2, label="CPU")
    plt.bar(axe_x + 0.1, conso_ram, 0.2, label="RAM")

    plt.xticks(axe_x, names, rotation=90)
    set_options("Process name", "Percentage of use CPU/RAM", "Total consumption", True, True)


def set_options(x_label, y_label, title, legend=False, show=False):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if legend:
        plt.legend()

    if show:
        plt.show()
