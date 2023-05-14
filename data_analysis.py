from reader import LogReader
import matplotlib.pyplot as plt
import numpy as np


def stat_if():
    log_entries = LogReader.read_all()
    if_stat = {}
    for entry in log_entries:
        interfaces_stats = entry.get_interfaces()

        for interface in interfaces_stats:
            descr = interface.get_if_descr()
            if_in = interface.get_if_in_octets()
            if_out = interface.get_if_out_octets()

            if descr not in if_stat.keys():
                if_stat[descr] = [if_in, if_out, 0, 0]

            if if_stat[descr][0] <= if_in:
                if_stat[descr][2] += if_in - if_stat[descr][0]
            else:
                if_stat[descr][2] += (2 ** 32) - if_stat[descr][0] + if_in

            if if_stat[descr][1] <= if_out:
                if_stat[descr][3] += if_out - if_stat[descr][1]
            else:
                if_stat[descr][3] += (2 ** 32) - if_stat[descr][1] + if_in

            if_stat[descr][0] = if_in
            if_stat[descr][1] = if_out

    conso_in = []
    conso_out = []
    if_name = []
    for desc, stats in if_stat.items():
        if stats[2] > 0 and stats[3] > 0:
            if_name.append(desc)
            conso_in.append(stats[2])
            conso_out.append(stats[3])

    axe_x = np.arange(len(if_name))
    # print(conso_out)
    # print(conso_in)
    plt.bar(axe_x - 0.05, conso_in, 0.1, label="Download")
    plt.bar(axe_x + 0.05, conso_out, 0.1, label="Upload")

    plt.xticks(axe_x, if_name, rotation=90)
    plt.xlabel("Nom des interfaces")
    plt.ylabel("Consommation en milliards d'octets")
    plt.title("Consommation totale de chaque interface")
    plt.legend()
    plt.show()


def stat_disk():
    log_entries = LogReader.read_all()
    disk_status = {}
    time_list = []
    for entry in log_entries:
        disk_stats = entry.get_disks()
        time_stat = entry.get_time_stats()
        time_list.append(time_stat)
        for disk in disk_stats:
            index = disk.get_hr_storage_index()
            descr = disk.get_hr_storage_descr()
            used = int(disk.get_hr_storage_used())
            total_space = int(disk.get_hr_storage_size())
            a_u = int(disk.get_storage_allocation_units()[0:4])
            percent_used = (used*a_u)/(total_space*a_u)*100
            if percent_used == 0:
                continue
            if index in disk_status.keys():
                disk_status[index].append(percent_used)
            else:
                disk_status[index] = [percent_used]

    for disk, percent in disk_status.items():
        plt.plot(np.arange(len(percent)), percent, label=disk)
    plt.xticks(np.arange(len(time_list)), time_list, rotation=40, horizontalalignment='right')
    plt.xlabel("Temp passé par tranche de 5 min")
    plt.ylabel("Pourcentage d'espace occupé sur les disques")
    plt.title("Utilisation des disques")
    plt.legend()
    plt.show()


def stats_cpu_and_ram():
    log_entries = LogReader.read_all()
    cpu_stats = []
    ram_stats = []
    for entry in log_entries:
        ram = entry.get_ram_stats()
        cpu_stats.append(entry.get_cpu_stats())
        totale = float(ram.get_mem_total_real()[:-2])
        avail = float(ram.get_mem_avail_real()[:-2])
        percent_ram_used = 100 - ((avail/totale)*100)
        ram_stats.append(percent_ram_used)
    la_loads = [(float(cpu.get_la_load()) * 100) for cpu in cpu_stats]
    plt.plot(np.arange(len(ram_stats)), ram_stats, label="RAM")
    plt.plot(np.arange(len(la_loads)), la_loads, label="CPU")
    plt.xlabel("Temp passé par tranche de 5 min")
    plt.ylabel("Pourcentage d'utilisation")
    plt.title("Consommation du cpu et de la ram")
    plt.legend()
    plt.show()


def process_stat():
    pass
