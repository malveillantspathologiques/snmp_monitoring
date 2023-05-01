from network.snmp import *

interfaces = []

interfaces_info = get_interfaces_info("HELMpAllUser9465CmA", "192.168.128.24")
for interface in interfaces_info:
    interfaces.append(Interface(interface))

print(interfaces)

disks = []

disks_info = get_disks_info("HELMpAllUser9465CmA", "192.168.128.24")
for disk in disks_info:
    disks.append(Disk(disk))

print(disks)

cpus = []

cpus_info = get_cpu_info("HELMpAllUser9465CmA", "192.168.128.24")
for disk in cpus_info:
    cpus.append(CPU(disk))

print(cpus)
