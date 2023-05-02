from domain.Process import Process
from network.snmp import *

# interfaces = []
#
# interfaces_info = get_interfaces_info("HELMpAllUser9465CmA", "192.168.128.24")
# for interface in interfaces_info:
#     interfaces.append(Interface(interface))
#
# print(interfaces)
#
# disks = []
#
# disks_info = get_disks_info("HELMpAllUser9465CmA", "192.168.128.24")
# for disk in disks_info:
#     disks.append(Disk(disk))
#
# print(disks)

# cpus = []
#
# cpus_info = get_cpu_info("HELMpAllUser9465CmA", "192.168.128.24")
# for cpu in cpus_info:
#     cpus.append(CPU(cpu))
#
# print(cpus)

# rams = []
#
# rams_info = get_ram_info("HELMpAllUser9465CmA", "192.168.128.24")
# for ram in rams_info:
#     rams.append(RAM(ram))
#
# print(rams)

# systems = []
#
# system_info = get_sys_uptime_info("HELMpAllUser9465CmA", "192.168.128.24")
# for system in system_info:
#     systems.append(System(system))
#
# print(systems)

processes = []
process_info = get_processes_info("HELMpAllUser9465CmA", "192.168.128.24")
for process in process_info:
    processes.append(Process(process))

print(processes)
