# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

conffile = argv[1]

with open(conffile) as f:
    for line in f:
        if not line.startswith('!'):
            ign_ok = True # В строке нет слова из списка ignore
            for ign in ignore:
                if ign in line:
                    ign_ok = False
            if ign_ok:
                print(line.rstrip())

