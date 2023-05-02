def top(liste_process, size=10):
    exhaustif_process = []
    for process in liste_process :
        if process in exhaustif_process :
            index = exhaustif_process.index(process)
            exhaustif_process[index].add(process)
        else:
            exhaustif_process.append(process)

    top_cpu = sorted(exhaustif_process, reverse=True, key=lambda p: p.process_cpu_usage)
    top_ram = sorted(exhaustif_process, reverse=True, key=lambda p: p.process_ram_usage)
    return top_cpu[:size], top_ram[:size]