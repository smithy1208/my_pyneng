# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (пример mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.

Для части пользователей запись только одна и тогда в итоговый файл надо записать только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_datetimestr_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.

Функцию convert_datetimestr_to_datetime использовать не обязательно.

"""

import datetime
import csv
from pprint import pprint


def convert_datetimestr_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, output):
    '''
    Аргументы функции:
    * source_log - имя файла в формате csv, из которого читаются данные (пример mail_log.csv)
    * output - имя файла в формате csv, в который будет записан результат

    Функция ничего не возвращает.
    '''
    with open(source_log) as src:
        reader = csv.reader(src)
        headers = next(reader)
        # print('Headers: ', headers)

        email_dict = {}
        for row in reader:
            name, email, last_changed = row

            if not email in email_dict.keys():
                email_dict[email] = [name, last_changed]
            else:
                old_data = email_dict[email][1]
                if convert_datetimestr_to_datetime(old_data) < convert_datetimestr_to_datetime(last_changed):
                    email_dict[email] = [name, last_changed]

    # pprint(email_dict)
    with open(output, 'w') as dst:
        writer = csv.writer(dst)
        writer.writerow(headers)
        for email, item in email_dict.items():
            name, last_changed = item
            writer.writerow([name, email, last_changed])


if __name__ == '__main__':
    write_last_log_to_csv('mail_log.csv', 'mail_out.csv')
