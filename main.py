import time

from domain.Statistic import Statistic
from network.snmp import *

# Every 5min run the loop
PERIOD = 60 * 5

while True:
    try:
        while True:
            print(f'[info] requesting statistics...')
            statistics = Statistic({
                'if': get_interfaces_info(),
                'disk': get_disks_info(),
                'process': get_processes_info(),
                'cpu': get_cpu_info(),
                'ram': get_ram_info(),
                'system': get_sys_uptime_info()
            })

            print(f'[info] writing statistics to file...')
            statistics.save(f'{time.strftime("%d_%m_%y__%Hh_%Mm_%Ss", time.localtime())}.json')
            print(f'[info] waiting {PERIOD} seconds...')
            time.sleep(PERIOD)
    except Exception as e:
        print(e)
        pass
