import json


class RAM:
    def __init__(self, infos):
        self.mem_avail_real = infos["UCD-SNMP-MIB::memAvailReal.0"]
        self.mem_total_real = infos["UCD-SNMP-MIB::memTotalReal.0"]
        self.mem_total_free = infos["UCD-SNMP-MIB::memTotalFree.0"]
        self.mem_total_swap = infos["UCD-SNMP-MIB::memTotalSwap.0"]

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    def get_mem_avail_real(self):
        return self.mem_avail_real

    def get_mem_total_real(self):
        return self.mem_total_real

    def get_mem_total_free(self):
        return self.mem_total_free

    def get_mem_total_swap(self):
        return self.mem_total_swap



    @classmethod
    def properties(cls):
        return [
            "UCD-SNMP-MIB::memAvailReal.0",
            "UCD-SNMP-MIB::memTotalReal.0",
            "UCD-SNMP-MIB::memTotalFree.0",
            "UCD-SNMP-MIB::memTotalSwap.0"
        ]
