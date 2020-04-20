# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from pprint import pprint

def parse_cdp_neighbors(command_output):
    '''
    Функция обрабатывает вывод команды show cdp neighbors.
    Функция должна возвращать словарь, который описывает соединения между устройствами.

    Например, если как аргумент был передан такой вывод:
    R4>show cdp neighbors

    Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
    R5           Fa 0/1          122           R S I           2811       Fa 0/1
    R6           Fa 0/2          143           R S I           2811       Fa 0/0

    Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
    '''
    result = {}

    next_is_neighbors = False

    for line in command_output.split('\n'):

        if line: # String not empty
            # Find device name
            if line.find('>') != -1:
                device = line[:line.find('>')]
            if line.startswith('Device'):
                next_is_neighbors = True
                continue
            if next_is_neighbors:
                neighbor, s_intf_type, s_intf_num, *_, n_intf_type, n_intf_num = line.split()

                #print(neighbor, s_intf_type, s_intf_num, n_intf_type, n_intf_num)
                result[(device, s_intf_type + s_intf_num)] = (neighbor, n_intf_type + n_intf_num)


    return result


if __name__ == '__main__':
    test_file = 'sh_cdp_n_sw1.txt'

    with open(test_file) as f:
        cdp_out = f.read()
    #print(cdp_out)
    pprint(parse_cdp_neighbors(cdp_out))