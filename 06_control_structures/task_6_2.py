# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

user_ip = input('Enter IP address: ')
#user_ip = '10.0.1.1'

ip = user_ip.split('.')
ip = [int(oct) for oct in ip]
print(ip)
first_bite = ip[0]
if first_bite >=1 and first_bite <= 223:
    print('unicast')
elif first_bite >= 224 and first_bite <= 239:
    print('multicast')
elif user_ip == '255.255.255.255':
    print('local broadcast')
elif user_ip == '0.0.0.0':
    print('unassigned')
else:
    print('unused')