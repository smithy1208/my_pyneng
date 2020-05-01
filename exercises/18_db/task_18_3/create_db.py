# -*- coding: utf-8 -*-
'''
1. create_db.py - в этот скрипт должна быть вынесена функциональность по созданию БД:
  * должна выполняться проверка наличия файла БД
  * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql, должна быть создана БД
  * имя файла бд - dhcp_snooping.db

В БД должно быть две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - тут хранится информация полученная из вывода sh ip dhcp snooping binding

Пример выполнения скрипта, когда файла dhcp_snooping.db нет:
$ python create_db.py
Создаю базу данных...

После создания файла:
$ python create_db.py
'''

import sqlite3
import os.path

DB_NAME = 'dhcp_snooping.db'
f_schema = 'dhcp_snooping_schema.sql'

if os.path.isfile(DB_NAME):
    print('База данных существует')
else:
    print('Создаю базу данных...')

    conn = sqlite3.connect(DB_NAME)

    print('Creating schema...')
    with open(f_schema, 'r') as f:
        schema = f.read()
        conn.executescript(schema)
    print("Done")

    conn.close()

