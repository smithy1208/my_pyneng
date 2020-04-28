# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом,
чтобы в значении словаря она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""
import re
from pprint import pprint

def get_ip_from_cfg(filecfg):
    '''
    Функция должна обрабатывать конфигурацию и возвращать словарь:
    * ключ: имя интерфейса
    * значение: список кортежей с двумя строками:
      * IP-адрес
      * маска
    В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.
    Например (взяты произвольные адреса):
    {'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
     'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}
    :param filecfg:
    :return:
    '''
    result = {}

    regex_intf = re.compile(r'interface (\S+)')
    regex_ip = re.compile(r' ip address (\S+) (\S+)')

    with open(filecfg) as f:
        for line in f:

            match_intf = regex_intf.match(line)
            if match_intf:
                intf = match_intf.group(1)

            match_ip = regex_ip.match(line)
            if match_ip:
                if not intf in result.keys():
                    result[intf] = []
                result[intf].append(match_ip.groups())


    return result

if __name__ == '__main__':
    cfg = 'config_r2.txt'

    pprint(get_ip_from_cfg(cfg))