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
            percent_used = (used * a_u) / (total_space * a_u) * 100
            if percent_used == 0:
                continue
            if index in disk_status.keys():
                disk_status[index].append(percent_used)
            else:
                disk_status[index] = [percent_used]

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


def process_stat():
    log_entries = LogReader.read_all()
    cpu_dict = {}
    ram_dict = {}
    for entry in log_entries:
        top_cpu = entry.get_processes_top_cpu()
        top_ram = entry.get_processes_top_ram()

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
                cpu_dict[name][3] += (2 ** 32) - cpu_dict[name][1] + cpu_usage

            cpu_dict[name][0] = cpu_usage
            cpu_dict[name][1] = ram_usage

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
                ram_dict[name][3] += (2 ** 32) - ram_dict[name][1] + cpu_usage

            ram_dict[name][0] = cpu_usage
            ram_dict[name][1] = ram_usage
    cpu_dict.update(ram_dict)
    conso_cpu = []
    conso_ram = []
    conso_merge = []
    names = []
    value_zawarudo_cpu = 0
    value_zawarudo_ram = 0
    for pname, stats in cpu_dict.items():
        value_zawarudo_cpu += stats[2]
        value_zawarudo_ram += stats[3]
        if stats[2] > 0 and stats[3] > 0:
            names.append(pname)
            conso_cpu.append((stats[2] / value_zawarudo_cpu) * 100)
            conso_ram.append((stats[3] / value_zawarudo_ram) * 100)
            conso_merge.append([(stats[2] / value_zawarudo_cpu) * 100, (stats[3] / value_zawarudo_ram) * 100])

    Drawer.draw_processes(names, conso_cpu, conso_ram)


process_stat()
