import json


class Disk:

    def __init__(self, infos):
        self.hr_storage_index = infos['HOST-RESOURCES-MIB::hrStorageIndex']
        self.hr_storage_descr = infos['HOST-RESOURCES-MIB::hrStorageDescr']
        self.hr_storage_allocation_units = infos['HOST-RESOURCES-MIB::hrStorageAllocationUnits']
        self.hr_storage_size = infos['HOST-RESOURCES-MIB::hrStorageSize']
        self.hr_storage_used = infos['HOST-RESOURCES-MIB::hrStorageUsed']

    def __repr__(self):
        return json.dumps(self.__dict__, default=str, indent=4)

    def get_hr_storage_index(self):
        return self.hr_storage_index

    def get_hr_storage_descr(self):
        return self.hr_storage_descr

    def get_storage_allocation_units(self):
        return self.hr_storage_allocation_units

    def get_hr_storage_size(self):
        return self.hr_storage_size

    def get_hr_storage_used(self):
        return self.hr_storage_used

    @classmethod
    def properties(cls):
        return [
            "HOST-RESOURCES-MIB::hrStorageIndex",
            "HOST-RESOURCES-MIB::hrStorageDescr",
            "HOST-RESOURCES-MIB::hrStorageAllocationUnits",
            "HOST-RESOURCES-MIB::hrStorageSize",
            "HOST-RESOURCES-MIB::hrStorageUsed"
        ]

    @classmethod
    def from_log(cls, log):
        data = {
            "HOST-RESOURCES-MIB::hrStorageIndex": log['hr_storage_index'],
            "HOST-RESOURCES-MIB::hrStorageDescr": log['hr_storage_descr'],
            "HOST-RESOURCES-MIB::hrStorageAllocationUnits": log['hr_storage_allocation_units'],
            "HOST-RESOURCES-MIB::hrStorageSize": log['hr_storage_size'],
            "HOST-RESOURCES-MIB::hrStorageUsed": log['hr_storage_used']
        }
        return Disk(data)
