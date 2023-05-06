import json


class Interface:

    def __init__(self, infos):
        self.if_index = infos['IF-MIB::ifIndex']
        self.if_descr = infos['IF-MIB::ifDescr']
        self.if_type = infos['IF-MIB::ifType']
        self.if_in_octets = infos['IF-MIB::ifInOctets']
        self.if_out_octets = infos['IF-MIB::ifOutOctets']
        self.if_phys_address = infos['IF-MIB::ifPhysAddress']
        self.if_last_change = infos['IF-MIB::ifLastChange']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    @classmethod
    def properties(cls):
        return [
            "IF-MIB::ifIndex",
            "IF-MIB::ifDescr",
            "IF-MIB::ifType",
            "IF-MIB::ifInOctets",
            "IF-MIB::ifOutOctets",
            "IF-MIB::ifPhysAddress",
            "IF-MIB::ifLastChange"
        ]
