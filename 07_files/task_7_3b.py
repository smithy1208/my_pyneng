# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
my_template = '{:<7}{:<18}{:<8}'

srcfile = 'CAM_table.txt'

result = []
with open(srcfile) as src:
    for line in src:
        if line.split() and line.split()[0].isdigit():
            vlan, mac, _, intf = line.split()
            vlan = int(vlan)
            vlan_line = [vlan, mac, intf]
            result.append(vlan_line)

#result.sort()
# for lst in result:
#     vlan, mac, intf = lst
#     print(my_template.format(vlan, mac, intf))
user_vlanid = int(input('Enter vlanid: '))
user_result = [lst for lst in result if lst[0] == user_vlanid]
for item in user_result:
    vlan, mac, intf = item
    print(my_template.format(vlan, mac, intf))
