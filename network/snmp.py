import subprocess

from domain.CPU import CPU
from domain.Disk import Disk
from domain.Interface import Interface
from domain.Process import Process
from domain.RAM import RAM
from domain.System import System


def snmp_get_info(oids, community="HELMpAllUser9465CmA", host="192.168.128.24"):
    command = ['snmpget', "-Oqvn", '-v', '2c', '-c', community, host, *oids]
    try:
        output = subprocess.check_output(command).decode('utf-8').strip()
        if 'No Such Object available' in output or 'No Such Instance currently exists' in output:
            return None
        return [x.strip() for x in output.split("\n") if x]
    except subprocess.CalledProcessError as e:
        print(' '.join(command))
        return []


def snmp_walk_info(oid, community="HELMpAllUser9465CmA", host="192.168.128.24"):
    command = ['snmpwalk', "-Oqvn", '-v', '2c', '-c', community, host, oid]
    try:
        output = subprocess.check_output(command).decode('utf-8')
        return [x.strip() for x in output.split("\n") if x]
    except subprocess.CalledProcessError as e:
        print(' '.join(command))
        return []


def request_properties_all(indexes, clazz):
    clazz_infos = []
    for index in indexes:
        clazz_info = request_properties_single(index, clazz)
        clazz_infos.append(clazz_info)

    return clazz_infos


def request_properties_single(index, clazz):
    clazz_info = {}
    oids = clazz.properties() if index is None else [f"{property_name}.{index}" for property_name in clazz.properties()]
    values = snmp_get_info(oids)
    for idx, value in enumerate(values):
        clazz_info[clazz.properties()[idx]] = value

    return clazz(clazz_info)


def get_interfaces_info():
    if_index_oid = "IF-MIB::ifIndex"
    if_indexes = snmp_walk_info(if_index_oid)

    return request_properties_all(if_indexes, Interface)


def get_disks_info():
    disk_index_oid = "HOST-RESOURCES-MIB::hrStorageIndex"
    disk_indexes = snmp_walk_info(disk_index_oid)

    return request_properties_all(disk_indexes, Disk)


def get_processes_info():
    hrSWRunIndex_oid = "HOST-RESOURCES-MIB::hrSWRunIndex"
    processes_indexes = snmp_walk_info(hrSWRunIndex_oid)

    return request_properties_all(processes_indexes, Process)


def get_cpu_info():
    return [request_properties_single(None, CPU)]


def get_ram_info():
    return [request_properties_single(None, RAM)]


def get_sys_uptime_info():
    return [request_properties_single(None, System)]
