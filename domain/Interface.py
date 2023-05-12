import json


class Interface:

    def __init__(self, infos):
        self.if_index = infos['IF-MIB::ifIndex']
        self.if_descr = infos['IF-MIB::ifDescr']
        self.if_type = infos['IF-MIB::ifType']
        self.if_in_octets = infos['IF-MIB::ifInOctets']
        self.if_out_octets = infos['IF-MIB::ifOutOctets']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    def get_if_index(self):
        return self.if_index

    def get_if_descr(self):
        return self.if_descr

    def get_if_type(self):
        return self.if_type

    def get_if_in_octets(self):
        return int(self.if_in_octets)

    def get_if_out_octets(self):
        return int(self.if_out_octets)

    @classmethod
    def properties(cls):
        return [
            "IF-MIB::ifIndex",
            "IF-MIB::ifDescr",
            "IF-MIB::ifType",
            "IF-MIB::ifInOctets",
            "IF-MIB::ifOutOctets"
        ]

    @classmethod
    def from_log(cls, log):
        data = {
            "IF-MIB::ifIndex": log['if_index'],
            "IF-MIB::ifDescr": log['if_descr'],
            "IF-MIB::ifType": log['if_type'],
            "IF-MIB::ifInOctets": log['if_in_octets'],
            "IF-MIB::ifOutOctets": log['if_out_octets']
        }
        return Interface(data)
