# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from pprint import pprint

def get_int_vlan_map(config_filename):
    mode_access = {}
    mode_trunk = {}
    with open(config_filename) as f:
        for line in f:
            if line.startswith('interface'):
                intf = line.split()[1]
                #print(intf)
            elif 'access vlan' in line:
                mode_access[intf] = int(line.split()[-1])
            elif 'mode access' in line:
                mode_access[intf] = 1
            elif 'allowed vlan' in line:
                mode_trunk[intf] = [int(vid) for vid in line.split()[-1].split(',')]

    #print(mode_access)
    #print(mode_trunk)

    return (mode_access, mode_trunk)

pprint(get_int_vlan_map('config_sw2.txt'))
