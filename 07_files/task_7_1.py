# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

my_output = '''{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
'''

with open('ospf.txt') as f:
    for ospf_route in f:
        route_list = [item.strip('[],') for item in ospf_route.split()]
        _, prefix, metric, _, next_hop, update, intf = route_list
        print(my_output.format(
            'Protocol:', 'OSPF',
            'Prefix:', prefix,
            'AD/Metric:', metric,
            'Next-Hop:', next_hop,
            'Last update:', update,
            'Outbound Interface:', intf
        ))