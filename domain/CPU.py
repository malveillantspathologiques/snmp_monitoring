import json


class CPU:
    def __init__(self, infos):
        self.ss_cpu_raw_user = infos['UCD-SNMP-MIB::ssCpuRawUser.0']
        self.ss_cpu_raw_system = infos['UCD-SNMP-MIB::ssCpuRawSystem.0']
        self.ss_cpu_raw_kernel = infos['UCD-SNMP-MIB::ssCpuRawKernel.0']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    @classmethod
    def properties(cls):
        return [
            "UCD-SNMP-MIB::ssCpuRawUser.0",
            "UCD-SNMP-MIB::ssCpuRawSystem.0",
            "UCD-SNMP-MIB::ssCpuRawKernel.0"
        ]
