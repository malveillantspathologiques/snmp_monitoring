import json


class Process:
    def __init__(self, process_info):
        self.process_name = process_info['name']
        self.process_cpu_usage = process_info['cpu']
        self.process_ram_usage = process_info['memory']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)
