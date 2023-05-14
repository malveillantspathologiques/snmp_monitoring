import json


class Process:
    def __init__(self, process_info):
        self.hr_sw_run_index = process_info['HOST-RESOURCES-MIB::hrSWRunIndex']
        self.hr_sw_run_status = process_info['HOST-RESOURCES-MIB::hrSWRunStatus']

        hr_sw_run_name_raw = process_info['HOST-RESOURCES-MIB::hrSWRunName']
        hr_sw_run_perf_cpu_raw = process_info['HOST-RESOURCES-MIB::hrSWRunPerfCPU']
        hr_sw_run_perf_ram_raw = process_info['HOST-RESOURCES-MIB::hrSWRunPerfMem']

        self.hr_sw_run_name = hr_sw_run_name_raw.strip('\"')

        try:
            self.hr_sw_run_perf_cpu = int(
                hr_sw_run_perf_cpu_raw) if "MISSING VALUE" not in hr_sw_run_perf_cpu_raw else 0
            self.hr_sw_run_perf_ram = int(hr_sw_run_perf_ram_raw.replace(' KBytes',
                                                                         '')) if "MISSING VALUE" not in hr_sw_run_perf_ram_raw else 0
        except ValueError as e:
            print(e)
            print(self.hr_sw_run_perf_cpu, self.hr_sw_run_perf_ram)

    def __repr__(self):
        return json.dumps(
            {
                'hr_sw_run_index': self.hr_sw_run_index,
                'hr_sw_run_name': self.hr_sw_run_name,
                'hr_sw_run_status': self.hr_sw_run_status,
                'hr_sw_run_perf_cpu': self.hr_sw_run_perf_cpu,
                'hr_sw_run_perf_ram': self.hr_sw_run_perf_ram
            },
            default=str, indent=4)

    def __eq__(self, other):
        return self.hr_sw_run_name == other.hr_sw_run_name

    def add(self, other):
        self.hr_sw_run_perf_cpu += other.hr_sw_run_perf_cpu
        self.hr_sw_run_perf_ram += other.hr_sw_run_perf_ram
        return self

    def get_hr_sw_run_index(self):
        return self.hr_sw_run_index

    def get_hr_sw_run_name(self):
        return self.hr_sw_run_name

    def get_hr_sw_run_status(self):
        return self.hr_sw_run_status

    def get_hr_sw_run_perf_cpu(self):
        return self.hr_sw_run_perf_cpu

    def get_hr_sw_run_perf_ram(self):
        return self.hr_sw_run_perf_ram

    @classmethod
    def properties(cls):
        return [
            "HOST-RESOURCES-MIB::hrSWRunIndex",
            "HOST-RESOURCES-MIB::hrSWRunName",
            "HOST-RESOURCES-MIB::hrSWRunStatus",
            "HOST-RESOURCES-MIB::hrSWRunPerfCPU",
            "HOST-RESOURCES-MIB::hrSWRunPerfMem"
        ]

    @classmethod
    def from_log(cls, log):
        data = {
            "HOST-RESOURCES-MIB::hrSWRunIndex": log['hr_sw_run_index'],
            "HOST-RESOURCES-MIB::hrSWRunName": log['hr_sw_run_name'],
            "HOST-RESOURCES-MIB::hrSWRunStatus": log['hr_sw_run_status'],
            "HOST-RESOURCES-MIB::hrSWRunPerfCPU": str(log['hr_sw_run_perf_cpu']),
            "HOST-RESOURCES-MIB::hrSWRunPerfMem": str(log['hr_sw_run_perf_ram'])
        }
        return Process(data)
