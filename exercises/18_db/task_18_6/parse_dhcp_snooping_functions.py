# -*- coding: utf-8 -*-

import sqlite3
import os.path
import yaml
import re
from tabulate import tabulate


def create_db(db_name, db_schema):
    if os.path.isfile(db_name):
        print('База данных существует')
    else:
        print('Создаю базу данных...')

        conn = sqlite3.connect(db_name)

        print('Creating schema...')
        with open(db_schema, 'r') as f:
            conn.executescript(f.read())
        print("Done")

        conn.close()


def add_data_switches(db_file, src_filenames):
    '''
    Из файла switches_file_yml загружаем банные в БД
    '''
    switches = {}
    for file in src_filenames:
        print(f'Добавляю данные из файла {file} в таблицу switches...')
        with open(file) as f:
            data = yaml.safe_load(f)
            switches.update(list(data.values())[0])
    # print(switches)
    conn = sqlite3.connect(db_file)

    query = 'insert into switches (hostname, location) values(?, ?)'

    for item in switches.items():
        try:
            with conn:
                conn.execute(query, item)
        except sqlite3.IntegrityError as e:
            print(f'Придобавлении данных: {item} Возникла ошибка: ', e)

    conn.close()


def add_data(db_file, dhcp_snoop_filelist):
    print('Добавляю данные в таблицу dhcp...')

    new_data = parse_dhcp_snoop_files(dhcp_snoop_filelist)

    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row

    # делаем все записи в БД active = 0
    conn.execute('update dhcp set active = 0')

    # Удаляем все старые записи в БД
    # now = datetime.today().replace(microsecond=0)
    # week_ago = str(now - timedelta(days=7))
    # delete_old_data(conn, week_ago)

    # Делаем реплейс для всех новых
    query = '''replace into dhcp (mac, ip, vlan, interface, switch, active, last_active)
                           values (?, ?, ?, ?, ?, ?, datetime('now', 'localtime'))'''

    for row in new_data:
        try:
            with conn:
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print(f'Придобавлении данных: {row} Возникла ошибка: ', e)

    conn.close()


def parse_dhcp_snoop_files(dhcp_snoop_filelist):
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []
    for file in dhcp_snoop_filelist:
        switch = re.match(r'(?:.+/)?(\w+?)_.*', file).group(1)
        with open(file) as f:
            for line in f:
                match = regex.match(line)
                if match:
                    row = list(match.groups())
                    row.append(switch)
                    row.append(1)
                    result.append(tuple(row))
    return result


def get_all_data(db_file):
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


def get_data(db_file, key, value):
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
