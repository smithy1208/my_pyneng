# -*- coding: utf-8 -*-
'''
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
'''
import re
from pprint import pprint


def generate_description_from_cdp(cdp_out_file):
    '''
    Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.
    Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
    'Eth 0/0': 'description Connected to SW1 port Eth 0/1'
    :param cdp_out_file:
    :return:
    '''
    result = {}
    #R1           Eth 0/1         122           R S I           2811       Eth 0/0
    regex = re.compile(r'(?P<neighbour>\S+)\s+(?P<local_intf>\S+ \S+)\s+\d+.+\s(?P<neighbor_intf>\S+ \S+$)')
    template = 'description Connected to {0} port {1}'

    with open(cdp_out_file) as f:
        for line in f:
            match = regex.match(line)
            if match:
                local_intf = match.group('local_intf')
                neighbour = match.group('neighbour')
                neighbor_intf = match.group('neighbor_intf')
                result[local_intf] = template.format(neighbour, neighbor_intf)


    return result


if __name__ == '__main__':
    cdp_out = 'sh_cdp_n_sw1.txt'
    pprint(generate_description_from_cdp(cdp_out))
