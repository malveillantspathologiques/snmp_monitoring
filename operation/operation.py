def top(processes, size=10):
    sorted_processes = []
    for process in processes:
        if process in sorted_processes:
            index = sorted_processes.index(process)
            sorted_processes[index].add(process)
        else:
            sorted_processes.append(process)

    top_cpu = sorted(sorted_processes, reverse=True, key=lambda p: p.process_cpu_usage)
    top_ram = sorted(sorted_processes, reverse=True, key=lambda p: p.process_ram_usage)
    return top_cpu[:size], top_ram[:size]
