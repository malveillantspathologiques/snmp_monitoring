import json
import os

from domain.Disk import Disk
from domain.Interface import Interface
from domain.Process import Process
from domain.System import System


def read_all(path_to_json='logs/'):
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

    logs = []
    for file in json_files:
        with open(f'logs/{file}', 'r') as f:
            logs.append(json.loads(f.read()))

    return from_logs(logs)


def from_log(log):
    return LogEntry(log)


def from_logs(logs):
    entries = []
    for log in logs:
        entries.append(from_log(log))
    return entries


class LogEntry:

    def __init__(self, log):
        self.time_stats = log['time_stats']

        self.interfaces = []
        interfaces_stats = log['interfaces_stats']
        for stat in interfaces_stats:
            self.interfaces.append(Interface.from_log(stat))

        self.disks = []
        disks_stats = log['disks_stats']
        for stat in disks_stats:
            self.disks.append(Disk.from_log(stat))

        self.processes = []
        processes_stats = log['processes_stats']
        for stat in processes_stats:
            self.processes.append(Process.from_log(stat))

        self.processes_top_cpu = []
        processes_stats_cpu = log['processes_top_cpu']
        for stat in processes_stats_cpu:
            self.processes_top_cpu.append(Process.from_log(stat))

        self.processes_top_ram = []
        processes_stats_ram = log['processes_top_ram']
        for stat in processes_stats_ram:
            self.processes_top_ram.append(Process.from_log(stat))

        system_stats = log['system_stats'][0]
        self.system_stat = System.from_log(system_stats)

    def __repr__(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__)

    def get_time_stats(self):
        return self.time_stats

    def get_interfaces(self):
        return self.interfaces

    def get_disks(self):
        return self.disks

    def get_processes(self):
        return self.processes

    def get_processes_top_cpu(self):
        return self.processes_top_cpu

    def get_processes_top_ram(self):
        return self.processes_top_ram

    def get_system_stat(self):
        return self.system_stat
