import json


class System:
    def __init__(self, infos):
        self.sys_uptime = infos['DISMAN-EVENT-MIB::sysUpTimeInstance']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    @classmethod
    def properties(cls):
        return [
            "DISMAN-EVENT-MIB::sysUpTimeInstance"
        ]
