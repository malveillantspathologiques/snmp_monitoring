from pysnmp.hlapi import *


def snmp_get_info(host: str, community: str, oid: (tuple or str)) -> any:
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(*oid)) if type(oid) is tuple else ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(errorIndication)
        return None
    elif errorStatus:
        print(f"OID={oid} gave an error of type {errorStatus.prettyPrint()}")
        return None
    else:
        return varBinds[0][1].prettyPrint()


print(f'[INT]Octets IN for interface 1 = {snmp_get_info("192.168.128.24", "HELMpAllUser9465CmA", "1.3.6.1.2.1.2.2.1.10.1")}')
print(f'[STR]Octets IN for interface 1 = {snmp_get_info("192.168.128.24", "HELMpAllUser9465CmA", ("IF-MIB", "ifInOctets", 1))}')
