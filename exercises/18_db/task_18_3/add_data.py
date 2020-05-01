# -*- coding: utf-8 -*-
'''
2. add_data.py - с помощью этого скрипта, выполняется добавление данных в БД. Скрипт должен добавлять данные из вывода sh ip dhcp snooping binding и информацию о коммутаторах

Соответственно, в файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch, его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

'''

import sqlite3
import os.path
import yaml
import re
import glob
from tabulate import tabulate

def add_swithces(db_file, switches_file_yml):
    '''
    Из файла switches_file_yml загружаем банные в БД
    '''
    print('Добавляю данные в таблицу switches...')
    with open(switches_file_yml) as f:
        data = yaml.safe_load(f)
        switches = list(data.values())[0]

    conn = sqlite3.connect(db_file)

    query = 'insert into switches (hostname, location) values(?, ?)'

    for item in switches.items():
        try:
            with conn:
                conn.execute(query, item)
        except sqlite3.IntegrityError as e:
            print(f'Придобавлении данных: {item} Возникла ошибка: ', e)

    conn.close()

def parse_dhcp_snoop_files(dhcp_snoop_filelist):
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    result = []
    for file in dhcp_snoop_filelist:
        switch = re.match(r'.+/(\w+?)_.*', file).group(1)
        with open(file) as f:
            for line in f:
                match = regex.match(line)
                if match:
                    row = list(match.groups())
                    row.append(switch)
                    row.append(1)
                    result.append(tuple(row))
    return result

def add_dhcp_data(db_file, dhcp_snoop_filelist):

    print('Добавляю данные в таблицу dhcp...')

    new_data = parse_dhcp_snoop_files(dhcp_snoop_filelist)

    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row

    #делаем все записи в БД active = 0
    conn.execute('update dhcp set active = 0')

    #Делаем реплейс для всех новых
    query = '''replace into dhcp (mac, ip, vlan, interface, switch, active)
                       values (?, ?, ?, ?, ?, ?)'''

    for row in new_data:
        try:
            with conn:
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print(f'Придобавлении данных: {row} Возникла ошибка: ', e)

    conn.close()

def check_data(macs_list, mac):
    '''
    Функция ищет совпадение в МАС в MACs_list,
    MAC есть = True
    МАС'а нет = False
    '''
    conn = sqlite3.connect(db_file)

    query = 'select mac from dhcp where mac = ?'
    result = conn.execute(query, (mac,))
    if result.fetchall(): #есть совпадение
        return True
    else:
        return False


if __name__ == '__main__':

    db_filename = 'dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'
    switches_filename = 'switches.yml'
    dhch_snoop_files = glob.glob('new_data/*_dhcp_snooping.txt')
    #print(dhch_snoop_files)

    if os.path.isfile(db_filename):
        # add_swithces(db_filename, switches_filename)

        add_dhcp_data(db_filename, dhch_snoop_files)
        # mac = '00:09:BB:3D:D6:58'
        # res = check_data(db_filename, mac)
        # print(res)

    else:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
