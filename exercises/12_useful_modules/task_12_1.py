# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint
import ipaddress
import subprocess as sp

def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def ping_ip_addresses(ip_list):
    '''
    Функция проверяет доступность IP-адресов.
    
    Функция ожидает как аргумент список IP-адресов.
    
    Функция должна возвращать кортеж с двумя списками:
    * список доступных IP-адресов
    * список недоступных IP-адресов

    Для проверки доступности IP-адреса, используйте ping.
    
    :param ip_list: 
    :return: result: tuple(avalible_list, not_avalible_list)
    '''

    avalible_list = []
    not_avalible_list = []

    for ip in ip_list:
        if check_ip(ip):
            result = sp.run('ping -c 3 -n {}'.format(ip), shell=True).returncode
            if result == 0:
                avalible_list.append(ip)
            else:
                not_avalible_list.append(ip)
        else:
            not_avalible_list.append(ip)

    return (avalible_list, not_avalible_list)

if __name__ == '__main__':
    ip_addrs = ['1.2.3.', '192.168.16.33', '81.20.197.42', '123.23.23.255']
    pprint(ping_ip_addresses(ip_addrs))


