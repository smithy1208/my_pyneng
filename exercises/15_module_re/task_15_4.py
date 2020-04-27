# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
'''
import re
from pprint import pprint

def get_ints_without_description(cfg_file):
    '''
    Создать функцию get_ints_without_description, которая ожидает как аргумент
    имя файла, в котором находится конфигурация устройства.


    Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
    на которых нет описания (команды description).
    :param cfg_file:
    :return:
    '''
    result = []

    # Ищем по двум строкам. Первая начинается на 'interface', и захватываем слово из второй
    regex = re.compile(r'\ninterface (?P<intf>\S+)(?:\s+)(?P<desc_or_not>\S+)')

    with open(cfg_file) as f:
        for m in regex.finditer(f.read()):
            # Если слово во во второй строке _не_ 'description', то добавляем интерфейс в результат
            if m.group('desc_or_not') != 'description':
                result.append(m.group('intf'))

    return result

if __name__ == '__main__':
    cfg = 'config_r1.txt'

    pprint(get_ints_without_description(cfg))
