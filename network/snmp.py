import subprocess

from domain.CPU import CPU
from domain.Disk import Disk
from domain.Interface import Interface


def snmp_get_info(community, host, oid):
    command = ['snmpget', '-v', '2c', '-c', community, host, oid]
    output = subprocess.check_output(command).decode('utf-8')
    if 'No Such Object available' in output or 'No Such Instance currently exists' in output:
        return None
    else:
        return output.split("=")[0].strip(), output.split("=")[1].strip()


def snmp_walk_info(community, host, oid_base, index=None):
    if index:
        oid = f"{oid_base}.{index}"
    else:
        oid = oid_base

    command = ['snmpwalk', '-v', '2c', '-c', community, host, oid]
    try:
        output = subprocess.check_output(command).decode('utf-8')
    except subprocess.CalledProcessError as e:
        print(f"Error executing SNMP walk: {e}")
        return []

    return [(x.split("=")[0].strip(), x.split("=")[1].strip()) for x in output.split("\n") if x]


def get_interfaces_info(community, host):
    # Get the index values for each interface
    if_index_oid = "IF-MIB::ifIndex"
    if_indexes = [x[1][x[1].index(' ') + 1:] for x in snmp_walk_info(community, host, if_index_oid)]

    # For each interface, get the interface properties
    interfaces_info = []
    for if_index in if_indexes:
        interface_info = {}
        for property_name in Interface.properties():
            if_oid = f'{property_name}.{if_index}'
            key_val = snmp_get_info(community, host, if_oid)
            if key_val is None:
                key_val = ['', f'MISSING VALUE FOR {property_name} in get_interfaces_info']
            interface_info[property_name] = key_val[1]

        interfaces_info.append(interface_info)

    return interfaces_info


def get_disks_info(community, host):
    # Get the index values for each disk
    disk_index_oid = "HOST-RESOURCES-MIB::hrStorageIndex"
    disk_indexes = [x[1][x[1].index(' ') + 1:] for x in snmp_walk_info(community, host, disk_index_oid)]

    # For each disk, get the disk properties
    disks_info = []
    for disk_index in disk_indexes:
        disk_info = {}
        for property_name in Disk.properties():
            if_oid = f'{property_name}.{disk_index}'
            key_val = snmp_get_info(community, host, if_oid)
            if key_val is None:
                key_val = ['', f'MISSING VALUE FOR {property_name} in get_disks_info']
            disk_info[property_name] = key_val[1]

        disks_info.append(disk_info)

    return disks_info


def get_cpu_info(community, host):
    return []
