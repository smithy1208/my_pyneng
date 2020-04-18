# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

conffile = argv[1]

with open(conffile) as src, open('config_sw1_cleared.txt', 'w') as dst:
    for line in src:
        ign_ok = True # В строке нет слова из списка ignore
        for ign in ignore:
            if ign in line:
                ign_ok = False
        if ign_ok:
            dst.write(line)