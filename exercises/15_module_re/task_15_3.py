# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
from pprint import pprint


def convert_ios_nat_to_asa(ios_nat_file, asa_nat_file):
    '''
    Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

    Функция ожидает такие аргументы:
    - имя файла, в котором находится правила NAT Cisco IOS
    - имя файла, в который надо записать полученные правила NAT для ASA

    Функция ничего не возвращает.
    :param ios_nat_file:
    :param asa_nat_file:
    :return:

    ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022

    И соответствующие правила NAT для ASA:
    object network LOCAL_10.1.2.84
     host 10.1.2.84
     nat (inside,outside) static interface service tcp 22 20022
    '''

    # ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
    regex = re.compile(
        r'ip nat inside source static (?P<proto>\S+) (?P<ip>\S+) (?P<int_port>\d+) interface (\S+) (?P<ext_port>\d+)')
    asa_template = '''object network LOCAL_{0}
 host {0}
 nat (inside,outside) static interface service {1} {2} {3}
'''

    with open(ios_nat_file) as src, open(asa_nat_file, 'w') as dst:
        for line in src:
            match = regex.match(line)
            if match:
                proto = match.group('proto')
                ip = match.group('ip')
                int_port = match.group('int_port')
                ext_port = match.group('ext_port')
                # print(asa_template.format(ip, proto, int_port, ext_port))
                dst.writelines(asa_template.format(ip, proto, int_port, ext_port))
                # print(proto, ip, int_port, ext_port)
                # print(match.groups())

    return None


if __name__ == '__main__':
    ios_nat = 'cisco_nat_config.txt'
    asa_nat = 'asa_nat_config.txt'
    convert_ios_nat_to_asa(ios_nat, asa_nat)