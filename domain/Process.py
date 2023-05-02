import json


class Process:
    def __init__(self, process_info):
        self.process_name_raw = process_info['name']
        self.process_cpu_usage_raw = process_info['cpu']
        self.process_ram_usage_raw = process_info['memory']

        self.process_name = self.process_name_raw.strip('\"')
        try:
            self.process_cpu_usage = int(self.process_cpu_usage_raw.split(' ')[1])
            self.process_ram_usage = int(self.process_ram_usage_raw.split(' ')[1])
        except ValueError as e:
            print(e)
            print(self.process_cpu_usage_raw, self.process_ram_usage_raw)

    def __repr__(self):
        return json.dumps(
            {
                'process_name': self.process_name,
                'process_cpu_usage': self.process_cpu_usage,
                'process_ram_usage': self.process_ram_usage
            },
            default=str, indent=4)

    def __eq__(self, other):
        return self.process_name == other.process_name

    def add(self, other):
        self.process_cpu_usage += other.process_cpu_usage
        self.process_ram_usage += other.process_ram_usage
        return self
