# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
import sys
#ip_full = input('Insert IP/prefix: ')
#ip_full = '217.17.249.43/12'
ip_full = sys.argv[1]
ip = ip_full.split('/')[0].split('.')
ip = [int(oct) for oct in ip]
#print(ip)

prefix = int(ip_full.split('/')[1])
#print(prefix)
mask_str = ('1' * prefix) + ('0' * (32-prefix))

ip_str = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(ip[0], ip[1], ip[2], ip[3])
#print(ip_str)
net_str = '{:032b}'.format(int(ip_str, 2) & int(mask_str, 2))
#print(net_str)

net = [
    net_str[0:8],
    net_str[8:16],
    net_str[16:24],
    net_str[24:32]
]
#print(net)

mask = [
    mask_str[0:8],
    mask_str[8:16],
    mask_str[16:24],
    mask_str[24:32]
]

tmp = '''Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{4:<8}  {5:<8}  {6:<8}  {7:<8}
'''
print(tmp.format(
    int(net[0], 2), int(net[1], 2), int(net[2], 2), int(net[3], 2),
    net[0], net[1], net[2], net[3]
))

tmp = '''Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{5:<8}  {6:<8}  {7:<8}  {8:<8}
'''
print(tmp.format(prefix,
    int(mask[0], 2), int(mask[1], 2), int(mask[2], 2), int(mask[3], 2),
    mask[0], mask[1], mask[2], mask[3]))