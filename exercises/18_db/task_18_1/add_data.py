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

def add_dhcp_data(db_file, dhch_snoop_filelist):
    regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

    result = []

    for file in dhch_snoop_filelist:
        switch = re.match(r'(\w+?)_.*', file).group(1)
        #print(host)
        with open(file) as f:
            for line in f:
                match = regex.match(line)
                if match:
                    row = list(match.groups())
                    row.append(switch)
                    result.append(tuple(row))
    #print(result)


    query = '''insert into dhcp (mac, ip, vlan, interface, switch)
                       values (?, ?, ?, ?, ?)'''

    conn = sqlite3.connect(db_file)

    print('Добавляю данные в таблицу dhcp...')

    for row in result:
        try:
            with conn:
                conn.execute(query, row)
        except sqlite3.IntegrityError as e:
            print(f'Придобавлении данных: {row} Возникла ошибка: ', e)

    conn.close()

if __name__ == '__main__':

    db_filename = 'dhcp_snooping.db'
    schema_filename = 'dhcp_snooping_schema.sql'
    switches_filename = 'switches.yml'
    dhch_snoop_files = glob.glob('*_dhcp_snooping.txt')
    #print(dhch_snoop_files)

    if os.path.isfile(db_filename):
        add_swithces(db_filename, switches_filename)

        add_dhcp_data(db_filename, dhch_snoop_files)

    else:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
