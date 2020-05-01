# -*- coding: utf-8 -*-
'''
Скрипту могут передаваться аргументы и, в зависимости от аргументов, надо выводить разную информацию.
Если скрипт вызван:
* без аргументов, вывести всё содержимое таблицы dhcp
* с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
* с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов

Файл БД можно скопировать из задания 18.1.
'''

import sqlite3
import sys
from tabulate import tabulate

def get_all(db_file):
    query = 'select * from dhcp'

    conn = sqlite3.connect(db_file)

    # Позволяет далее обращаться к данным в колонках, по имени колонки
    conn.row_factory = sqlite3.Row

    result = conn.execute(query)

    print('В таблице dhcp такие записи:')
    print(tabulate(result))
    # for mac, ip, vid, intf, sw in result:
    #         print((mac, ip, vid, intf, sw))

    conn.close()

def get_cust(db_file, key, value):
    query_dict = {
        'vlan': 'select * from dhcp where vlan = ?',
        'mac': 'select * from dhcp where mac = ?',
        'ip': 'select * from dhcp where ip = ?',
        'interface': 'select * from dhcp where interface = ?',
        'switch': 'select * from dhcp where switch = ?'
    }

    keys = query_dict.keys()

    if not key in keys:
        print('Данный параметр не поддерживается.\nДопустимые значения параметров: {}'.format(', '.join(keys)))
    else:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row

        print('\nИнформация об устройствах с такими параметрами:', key, value)

        query = query_dict[key]
        result = conn.execute(query, (value,))

        print(tabulate(result))

        conn.close()

def mngt(db_file):
    if not sys.argv[1:]: #нет аргументов
        get_all(db_file)
    elif len(sys.argv[1:]) == 2:
        key, val = sys.argv[1:]
        get_cust(db_file, key, val)
    else:
        print('Пожалуйста, введите два или ноль аргументов')


if __name__ == '__main__':
    DB_FILE_NAME = 'dhcp_snooping.db'
    mngt(DB_FILE_NAME)