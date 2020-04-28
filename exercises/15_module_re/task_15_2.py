# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
from pprint import pprint

def parse_sh_ip_int_br(fileout):
    '''
    Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
    имя файла, в котором находится вывод команды show ip int br
    Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
    * Interface
    * IP-Address
    * Status
    * Protocol
    Информация должна возвращаться в виде списка кортежей:
    [('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
     ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
     ('FastEthernet0/2', 'unassigned', 'down', 'down')]
    :param filecfg:
    :return:
    '''
    result = []

    regex = re.compile(r'(\S+) +(\S+) +\S+ +\S+ +(up|down|administratively down) +(up|down)')

    with open(fileout) as f:
        for line in f:
            match = regex.match(line)
            if match:
                result.append(match.groups())

    return result

if __name__ == '__main__':
    out = 'sh_ip_int_br.txt'

    pprint(parse_sh_ip_int_br(out))