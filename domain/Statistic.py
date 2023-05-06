import json
import time

from operation.operation import top


class Statistic:

    def __init__(self, stats):
        self.time_stats = time.strftime("%I:%M:%S %p", time.localtime())
        self.interfaces_stats = stats['if']
        self.disks_stats = stats['disk']
        self.processes_stats = stats['process']

        self.processes_top_cpu, self.processes_top_ram = top(self.processes_stats)

        self.cpu_stats = stats['cpu']
        self.ram_stats = stats['ram']
        self.system_stats = stats['system']

    def __str__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)

    def save(self, path):
        with open(path, 'a') as f:
            f.write(str(self))
