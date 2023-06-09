import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime


def addlabels(x,y):
    for i in range(0,len(x)):
        plt.text(i,round(y[i],3),round(y[i],3), rotation=45)


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
    fig, ax = plt.subplots()
    for disk, percent in disk_status.items():
        ax.plot(np.arange(len(percent)), percent, label=disk)

    # for disk, percent in disk_status.items():
    #     plt.plot(np.arange(len(percent)), percent, label=disk)

    #plt.xticks(np.arange(len(time_list)), time_list, rotation=90, horizontalalignment='right')
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


def draw_processes_cpu(names, conso_cpu):
    axe_x = np.arange(len(names))

    # ToDo
    # sorted_merge = sorted(conso_merge, reverse=True, key=lambda x: liste[0] + liste[1]) / 2))

    plt.bar(axe_x - 0.1, conso_cpu, 0.2, label="CPU")

    plt.xticks(axe_x, names, rotation=90)
    list_of_names = []
    list_conso = []
    for element in names:
        list_of_names.append(element)
    for element in conso_cpu:
        list_conso.append(element)
    addlabels(list_of_names, list_conso)
    set_options("Process name", "Percentage of use CPU", "Total consumption", True, True)


def draw_processes_ram(names, conso_ram):
    axe_x = np.arange(len(names))
    plt.bar(axe_x + 0.1, conso_ram, 0.2, label="RAM")

    plt.xticks(axe_x, names, rotation=90)
    list_of_names = []
    list_conso = []
    for element in names:
        list_of_names.append(element)
    for element in conso_ram:
        list_conso.append(element)
    addlabels(list_of_names, list_conso)
    set_options("Process name", "Percentage of use RAM", "Total consumption", True, True)


def set_options(x_label, y_label, title, legend=False, show=False):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    if legend:
        plt.legend()

    if show:
        plt.show()

# def draw_disks(disk_status, time_list):
#     day = mdates.DayLocator()  # every year
#     months = mdates.HourLocator()  # every month
#     dayFmt = mdates.DateFormatter('%D')
#     fig, ax = plt.subplots()
#     for disk, percent in disk_status.items():
#         ax.plot(np.arange(len(percent)), percent, label=disk)
#
#     ax.xaxis.set_major_locator(day)
#     ax.xaxis.set_major_formatter(dayFmt)
#     ax.xaxis.set_minor_locator(months)
#     datemin = datetime.datetime(2023,5,6,15,30,1 )
#     datemax = datetime.datetime(2023,5,12,18,40,2 )
#     ax.set_xlim(datemin, datemax)
#
#     plt.xlabel("Temp passé par tranche de 5 min")
#     plt.ylabel("Pourcentage d'espace occupé sur les disques")
#     plt.title("Utilisation des disques")
#     plt.legend()
#     plt.show()