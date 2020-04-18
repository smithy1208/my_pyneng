# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration', '!']

from sys import argv

conffile = argv[1]
dstfile = argv[2]

with open(conffile) as src, open(dstfile, 'w') as dst:
    for line in src:
        ign_ok = True # В строке нет слова из списка ignore
        for ign in ignore:
            if ign in line:
                ign_ok = False
        if ign_ok:
            dst.write(line)