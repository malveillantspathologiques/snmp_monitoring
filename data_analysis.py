from reader import LogReader

log_entries = LogReader.read_all()

if_stat = {}
for entry in log_entries[:5]:
    interfaces_stats = entry.get_interfaces()

    for interface in interfaces_stats:
        descr = interface.get_if_descr()
        if_in = interface.get_if_in_octets()
        if_out = interface.get_if_out_octets()

        print(descr, if_in, if_out)

        if descr not in if_stat.keys():
            if_stat[descr] = [if_in, if_out, 0, 0]
        else:
            delta_in = if_in - if_stat[descr][0]
            delta_out = if_out - if_stat[descr][1]

            if delta_in < 0:
                delta_in = 2**32 + delta_in

            if delta_out < 0:
                delta_out = 2**32 + delta_out

            if_stat[descr][0] = if_in
            if_stat[descr][1] = if_out
            if_stat[descr][2] = delta_in
            if_stat[descr][3] = delta_out


print(if_stat)

