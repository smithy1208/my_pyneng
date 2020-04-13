# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

#keys_d = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']
route_list = ospf_route.split()
my_output = '''{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
{:<24} {:<}
{:<24} {:<}'''
print(my_output.format(
    'Protocol:', 'OSPF',
    'Prefix:', route_list[1],
    'AD/Metric:', route_list[2].strip('[]'),
    'Next-Hop:', route_list[4].replace(',', ''),
    'Last update:', route_list[5].replace(',', ''),
    'Outbound Interface:', route_list[6]
))
