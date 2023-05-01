import json


class CPU:
    def __init__(self, infos):
        pass

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    @classmethod
    def properties(cls):
        return []
