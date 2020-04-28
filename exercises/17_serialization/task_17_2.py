# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint

def parse_sh_cdp_neighbors(sh_cdp):
    '''
    Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
    Функция должна возвращать словарь, который описывает соединения между устройствами.
    '''
    result = {}
    host = re.match(r'\n?(\w+)[>#]', sh_cdp).group(1)
    regex = r'\n(?P<neighbour>\S+)\s+(?P<local_intf>\S+ \S+)\s+\d+.+\s(?P<neigh_intf>\S+ \S+)'
    match_dict = [match.groupdict() for match in re.finditer(regex, sh_cdp)]

    intf_dict = {}
    for item in match_dict:
        neigh = {}
        neigh[item['neighbour']] = item['neigh_intf']
        local_intf = {}
        intf_dict[item['local_intf']] = neigh

    result[host] = intf_dict

    return result

if __name__ == '__main__':
    cdp_file = 'sh_cdp_n_sw1.txt'
    with open(cdp_file) as f:
        pprint(parse_sh_cdp_neighbors(f.read()))