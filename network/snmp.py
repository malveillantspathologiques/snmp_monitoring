import subprocess

from domain.CPU import CPU
from domain.Disk import Disk
from domain.Interface import Interface
from domain.RAM import RAM
from domain.System import System


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

    if oid_base == 'HOST-RESOURCES-MIB::hrSWRunPerfCPU':
        # Process CPU usage
        return [x.split(".")[1].strip() for x in output.split("\n") if x]
    elif oid_base == 'HOST-RESOURCES-MIB::hrSWRunPerfMem':
        # Process memory usage
        return [x.split(".")[1].strip() for x in output.split("\n") if x]

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
            disk_oid = f'{property_name}.{disk_index}'
            key_val = snmp_get_info(community, host, disk_oid)
            if key_val is None:
                key_val = ['', f'MISSING VALUE FOR {property_name} in get_disks_info']
            disk_info[property_name] = key_val[1]

        disks_info.append(disk_info)

    return disks_info


def get_cpu_info(community, host):
    cpu_info = {}
    for property_name in CPU.properties():
        cpu_oid = f'{property_name}'
        key_val = snmp_get_info(community, host, cpu_oid)
        if key_val is None:
            key_val = ['', f'MISSING VALUE FOR {property_name} in get_cpu_info']
        cpu_info[property_name] = key_val[1]

    return [cpu_info]


def get_ram_info(community, host):
    ram_info = {}
    for property_name in RAM.properties():
        ram_oid = f'{property_name}'
        key_val = snmp_get_info(community, host, ram_oid)
        if key_val is None:
            key_val = ['', f'MISSING VALUE FOR {property_name} in get_ram_info']
        ram_info[property_name] = key_val[1]

    return [ram_info]


def get_sys_uptime_info(community, host):
    sys_info = {}
    for property_name in System.properties():
        system_oid = f'{property_name}'
        key_val = snmp_get_info(community, host, system_oid)
        if key_val is None:
            key_val = ['', f'MISSING VALUE FOR {property_name} in get_sys_uptime_info']
        sys_info[property_name] = key_val[1]

    return [sys_info]


def get_processes_info(community, host):
    hrSWRunIndex_oid = "HOST-RESOURCES-MIB::hrSWRunIndex"
    hrSWRunName_oid = "HOST-RESOURCES-MIB::hrSWRunName"
    hrSWRunPerfCPU_oid = "HOST-RESOURCES-MIB::hrSWRunPerfCPU"
    hrSWRunPerfMem_oid = "HOST-RESOURCES-MIB::hrSWRunPerfMem"

    # TODO add uptime

    # Get the index values and names for each running process
    hrSWRunIndex_values = [x[1][x[1].index(' ') + 1:] for x in snmp_walk_info(community, host, hrSWRunIndex_oid)]
    hrSWRunName_values = [x[1][x[1].index(' ') + 1:] for x in snmp_walk_info(community, host, hrSWRunName_oid)]

    # Create a dictionary mapping process IDs to process names
    process_names = {hrSWRunIndex: hrSWRunName for hrSWRunIndex, hrSWRunName in
                     zip(hrSWRunIndex_values, hrSWRunName_values)}

    # For each running process, get the name, CPU usage, and memory usage
    processes_info = []
    for hrSWRunIndex in hrSWRunIndex_values:
        process_info = {
            'name': process_names.get(hrSWRunIndex, f'MISSING NAME FOR hrSWRunIndex={hrSWRunIndex}')}
        for oid, property_name in zip([hrSWRunPerfCPU_oid, hrSWRunPerfMem_oid], ['cpu', 'memory']):
            key_val = snmp_get_info(community, host, f'{oid}.{hrSWRunIndex}')
            if key_val is None:
                key_val = ['', f'INTEGER: 0']
            process_info[property_name] = key_val[1]

        processes_info.append(process_info)

    return processes_info
