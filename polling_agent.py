import time

from domain.Statistic import Statistic
from network.snmp import *


def get_current_time(fmt="%d_%m_%y__%Hh_%Mm_%Ss"):
    return f'{time.strftime(fmt, time.localtime())}'


def write_log(log):
    crt_time = get_current_time("%d/%m/%y %Hh:%Mm:%Ss")
    with open('logs/log.txt', 'a') as flog:
        flog.write(f'{crt_time} {log}\n')


done = False
while not done:
    try:
        current_time = get_current_time()

        write_log(f'[info] requesting statistics...')
        statistics = Statistic({
            'if': get_interfaces_info(),
            'disk': get_disks_info(),
            'process': get_processes_info(),
            'cpu': get_cpu_info(),
            'ram': get_ram_info(),
            'system': get_sys_uptime_info()
        })
        write_log(f'[info] writing statistics to file...')

        statistics.save(f'logs/{current_time}.json')
        write_log(f'[info] waiting 5 minutes...')

        done = True
    except Exception as e:
        write_log(f'[info] an exception occurred: {e}. Retrying...')
