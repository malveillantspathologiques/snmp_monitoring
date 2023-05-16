from graph import Drawer
from reader import LogReader


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

    Drawer.draw_if(if_stat)


def stat_disk(log_entries):
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
            percent_used = (used * a_u) / (total_space * a_u) * 100
            if percent_used == 0:
                continue
            if descr in disk_status.keys():
                disk_status[descr].append(percent_used)
            else:
                disk_status[descr] = [percent_used]

    Drawer.draw_disks(disk_status, time_list)


def stats_cpu_and_ram():
    log_entries = LogReader.read_all()
    cpu_stats = []
    ram_stats = []
    for entry in log_entries:
        ram = entry.get_ram_stats()
        cpu_stats.append(entry.get_cpu_stats())
        total = float(ram.get_mem_total_real()[:-2])
        avail = float(ram.get_mem_avail_real()[:-2])
        percent_ram_used = 100 - ((avail / total) * 100)
        ram_stats.append(percent_ram_used)
    la_loads = [(float(cpu.get_la_load()) * 100) for cpu in cpu_stats]
    Drawer.draw_cpu_and_ram(ram_stats, la_loads)


def process_stat_cpu(log_entries):
    cpu_dict = {}
    for entry in log_entries:
        top_cpu = entry.get_processes_top_cpu()

        for process in top_cpu:
            name = process.get_hr_sw_run_name()
            cpu_usage = process.get_hr_sw_run_perf_cpu()
            ram_usage = process.get_hr_sw_run_perf_ram()

            if name not in cpu_dict.keys():
                cpu_dict[name] = [cpu_usage, ram_usage, 0, 0]

            if cpu_dict[name][0] <= cpu_usage:
                cpu_dict[name][2] += cpu_usage - cpu_dict[name][0]
            else:
                cpu_dict[name][2] += (2 ** 32) - cpu_dict[name][0] + cpu_usage

            if cpu_dict[name][1] <= ram_usage:
                cpu_dict[name][3] += ram_usage - cpu_dict[name][1]
            else:
                cpu_dict[name][3] += (2 ** 32) - cpu_dict[name][1] + ram_usage

            cpu_dict[name][0] = cpu_usage
            cpu_dict[name][1] = ram_usage

    conso_cpu = []
    names = []
    value_zawarudo_cpu = 0
    for stats in cpu_dict.values():
        value_zawarudo_cpu += stats[2]
    for pname, stats in cpu_dict.items():
        if stats[2] > 0:
            names.append(pname)
            conso_cpu.append((stats[2] / value_zawarudo_cpu) * 100)
    cpu_info = {}
    for index, name in enumerate(names):
        cpu_info[name] = conso_cpu[index]
    conso_cpu_sorted = {k: v for k, v in sorted(cpu_info.items(), key=lambda item: item[1], reverse=True)}
    key = conso_cpu_sorted.keys()
    value = conso_cpu_sorted.values()
    Drawer.draw_processes_cpu(key, value)


def process_stat_ram(log_entries):
    ram_dict = {}
    for entry in log_entries:
        top_ram = entry.get_processes_top_ram()
        for process in top_ram:
            name = process.get_hr_sw_run_name()
            cpu_usage = process.get_hr_sw_run_perf_cpu()
            ram_usage = process.get_hr_sw_run_perf_ram()

            if name not in ram_dict.keys():
                ram_dict[name] = [cpu_usage, ram_usage, 0, 0]

            if ram_dict[name][0] <= cpu_usage:
                ram_dict[name][2] += cpu_usage - ram_dict[name][0]
            else:
                ram_dict[name][2] += (2 ** 32) - ram_dict[name][0] + cpu_usage

            if ram_dict[name][1] <= ram_usage:
                ram_dict[name][3] += ram_usage - ram_dict[name][1]
            else:
                ram_dict[name][3] += (2 ** 32) - ram_dict[name][1] + ram_usage

            ram_dict[name][0] = cpu_usage
            ram_dict[name][1] = ram_usage
    conso_ram = []
    names = []
    value_zawarudo_ram = 0
    for stats in ram_dict.values():
        value_zawarudo_ram += stats[3]
    for pname, stats in ram_dict.items():
        if stats[3] > 0:
            names.append(pname)
            conso_ram.append((stats[3] / value_zawarudo_ram) * 100)
    print(value_zawarudo_ram)

    ram_info = {}
    for index, name in enumerate(names):
        ram_info[name] = conso_ram[index]
    conso_ram_sorted = {k: v for k, v in sorted(ram_info.items(), key=lambda item: item[1], reverse=True)}
    key = conso_ram_sorted.keys()
    value = conso_ram_sorted.values()
    Drawer.draw_processes_ram(key, value)


log_entries = LogReader.read_all()

process_stat_cpu(log_entries)
process_stat_ram(log_entries)