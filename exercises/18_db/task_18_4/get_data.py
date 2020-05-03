# -*- coding: utf-8 -*-
'''
Скрипту могут передаваться аргументы и, в зависимости от аргументов, надо выводить разную информацию.
Если скрипт вызван:
* без аргументов, вывести всё содержимое таблицы dhcp
* с двумя аргументами, вывести информацию из таблицы dhcp, которая соответствует полю и значению
* с любым другим количеством аргументов, вывести сообщение, что скрипт поддерживает только два или ноль аргументов

Файл БД можно скопировать из задания 18.3.
'''

import sqlite3
import sys
from tabulate import tabulate

def get_all(db_file):
    conn = sqlite3.connect(db_file)

    # Позволяет далее обращаться к данным в колонках, по имени колонки
    conn.row_factory = sqlite3.Row

    print('\nВ таблице dhcp такие записи:')

    print('\nАктивные записи:')
    query = 'select * from dhcp where active = 1'
    result = conn.execute(query)
    print(tabulate(result))

    query = 'select * from dhcp where active = 0'
    result = conn.execute(query)
    for_print = tabulate(result)
    if for_print:
        print('\nНеактивные записи:')
        print(for_print)


    conn.close()

def get_cust(db_file, key, value):
    query_dict = {
        'vlan': 'select * from dhcp where vlan = ? and active = ?',
        'mac': 'select * from dhcp where mac = ? and active = ?',
        'ip': 'select * from dhcp where ip = ? and active = ?',
        'interface': 'select * from dhcp where interface = ? and active = ?',
        'switch': 'select * from dhcp where switch = ? and active = ?'
        # ,
        # 'all': 'select * from dhcp where active = ?'
    }

    keys = query_dict.keys()

    if not key in keys:
        print('Данный параметр не поддерживается.\nДопустимые значения параметров: {}'.format(', '.join(keys)))
    else:
        conn = sqlite3.connect(db_file)
        conn.row_factory = sqlite3.Row

        print('\nИнформация об устройствах с такими параметрами:', key, value)

        print('\nАктивные записи:')

        query = query_dict[key]
        result = conn.execute(query, (value, 1))

        print(tabulate(result))

        result = conn.execute(query, (value, 0))
        for_print = tabulate(result)
        if for_print:
            print('\nНективные записи:')
            print(for_print)

        conn.close()

def mngt(db_file):
    if not sys.argv[1:]: #нет аргументов
        get_all(db_file)
        # get_cust(db_file, 'all', 1)
    elif len(sys.argv[1:]) == 2:
        key, val = sys.argv[1:]
        get_cust(db_file, key, val)
    else:
        print('Пожалуйста, введите два или ноль аргументов')


if __name__ == '__main__':
    DB_FILE_NAME = 'dhcp_snooping.db'
    mngt(DB_FILE_NAME)