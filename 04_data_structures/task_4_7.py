# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

#print(mac.replace(':', ''))
mac_list = list(mac.replace(':', ''))
#print(mac_list)

# print('{:04b}'.format(int('A', 16)))
template = '{:04b}' * 12

# for i in range(12):
#     print('int(mac_list[0], 16),'.format(i))

result = (template.format(
    int(mac_list[0], 16),
    int(mac_list[1], 16),
    int(mac_list[2], 16),
    int(mac_list[3], 16),
    int(mac_list[4], 16),
    int(mac_list[5], 16),
    int(mac_list[6], 16),
    int(mac_list[7], 16),
    int(mac_list[8], 16),
    int(mac_list[9], 16),
    int(mac_list[10], 16),
    int(mac_list[11], 16)
))
if result == '101010101010101010111011101110111100110011001100':
    print(result)