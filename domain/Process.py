import json
import re


class Process:
    def __init__(self, process_info):
        self.process_name = process_info['name']
        self.process_cpu_usage_raw = process_info['cpu']
        self.process_ram_usage_raw = process_info['memory']
        self.process_cpu_usage = int((re.findall("(\d+)", self.process_cpu_usage_raw))[0])
        print(self.process_cpu_usage)
        self.process_ram_usage = int((re.findall("(\d+)", self.process_ram_usage_raw))[0])


    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    def __eq__(self, other):
        return self.process_name == other.process_name

    def add(self, other):
        self.process_cpu_usage += other.process_cpu_usage
        self.process_ram_usage += other.process_ram_usage
        return self
