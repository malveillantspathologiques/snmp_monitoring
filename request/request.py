from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen

def snmp_get_info_test1(address:str, community: str, oid:str ) -> list:
    cmdGen = cmdgen.CommandGenerator()
    errorIndication, errorStatus, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((address, 161)),
        oid
    )
def snmp_get_info(host:str, community: str, oid:str ) -> list:
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))
    return varBinds


snmp_get_info("192.168.128.24", "HELMpAllUser9465CmA", "1.3.6.1.2.1.2.2.1.10.1")

