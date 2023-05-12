import json


class CPU:
    def __init__(self, infos):
        self.ss_cpu_raw_user = infos['UCD-SNMP-MIB::ssCpuRawUser.0']
        self.ss_cpu_raw_system = infos['UCD-SNMP-MIB::ssCpuRawSystem.0']
        self.ss_cpu_raw_kernel = infos['UCD-SNMP-MIB::ssCpuRawKernel.0']
        self.la_load = infos["UCD-SNMP-MIB::laLoad.1"]

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    def get_ss_cpu_raw_user(self):
        return self.ss_cpu_raw_user

    def get_ss_cpu_raw_system(self):
        return self.ss_cpu_raw_system

    def get_ss_cpu_rw_kernel(self):
        return self.ss_cpu_raw_kernel

    def get_la_load(self):
        return self.la_load

    @classmethod
    def properties(cls):
        return [
            "UCD-SNMP-MIB::ssCpuRawUser.0",
            "UCD-SNMP-MIB::ssCpuRawSystem.0",
            "UCD-SNMP-MIB::ssCpuRawKernel.0",
            "UCD-SNMP-MIB::laLoad.2"
        ]
