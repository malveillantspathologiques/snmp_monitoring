import json


class System:
    def __init__(self, infos):
        self.sys_uptime = infos['DISMAN-EVENT-MIB::sysUpTimeInstance']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    def get_sys_uptime(self):
        return self.sys_uptime

    @classmethod
    def properties(cls):
        return [
            "DISMAN-EVENT-MIB::sysUpTimeInstance"
        ]

    @classmethod
    def from_log(cls, log):
        data = {
            'DISMAN-EVENT-MIB::sysUpTimeInstance': log['sys_uptime']
        }
        return System(data)
