import json


class Disk:

    def __init__(self, infos):
        self.hr_storage_index = infos['HOST-RESOURCES-MIB::hrStorageIndex']
        self.hr_storage_type = infos['HOST-RESOURCES-MIB::hrStorageType']
        self.hr_storage_descr = infos['HOST-RESOURCES-MIB::hrStorageDescr']
        self.hr_storage_allocation_units = infos['HOST-RESOURCES-MIB::hrStorageAllocationUnits']
        self.hr_storage_size = infos['HOST-RESOURCES-MIB::hrStorageSize']
        self.hr_storage_used = infos['HOST-RESOURCES-MIB::hrStorageUsed']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    @classmethod
    def properties(cls):
        return [
            "HOST-RESOURCES-MIB::hrStorageIndex",
            "HOST-RESOURCES-MIB::hrStorageType",
            "HOST-RESOURCES-MIB::hrStorageDescr",
            "HOST-RESOURCES-MIB::hrStorageAllocationUnits",
            "HOST-RESOURCES-MIB::hrStorageSize",
            "HOST-RESOURCES-MIB::hrStorageUsed"
        ]