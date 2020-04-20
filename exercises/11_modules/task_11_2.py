# -*- coding: utf-8 -*-
'''
Задание 11.2

Создать функцию create_network_map, которая обрабатывает
вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

У функции должен быть один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

Функция должна возвращать словарь, который описывает соединения между устройствами.
Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}


Cгенерировать топологию, которая соответствует выводу из файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt

В словаре, который возвращает функция create_network_map, не должно быть дублей.

С помощью функции draw_topology из файла draw_network_graph.py нарисовать схему на основании топологии, полученной с помощью функции create_network_map.
Результат должен выглядеть так же, как схема в файле task_11_2a_topology.svg


При этом:
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме

Не копировать код функций parse_cdp_neighbors и draw_topology.

Ограничение: Все задания надо выполнять используя только пройденные темы.

> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


from pprint import pprint
from draw_network_graph import draw_topology
from task_11_1 import parse_cdp_neighbors

def create_network_map(filenames):
    '''
    Функция create_network_map обрабатывает вывод команды show cdp neighbors из нескольких файлов и объединяет его в одну общую топологию.

    один параметр filenames, который ожидает как аргумент список с именами файлов, в которых находится вывод команды show cdp neighbors.

    Функция возвращает словарь, который описывает соединения между устройствами.
    Структура словаря такая же, как в задании 11.1:
    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}
    :param filenames:
    :return: dict
    '''
    result = {}

    # Разбираем первый файл.
    with open(filenames.pop(0)) as f1:
        result = parse_cdp_neighbors(f1.read())
    #print(filenames)
    for file in filenames:
        with open(file) as f:
            for key, value in parse_cdp_neighbors(f.read()).items():
                if not value in result.keys(): # Если значение не в ключах, то добавляем в словарь
                    result[key] = value

    return result

if __name__ == '__main__':

   draw_topology(create_network_map(['sh_cdp_n_r1.txt', 'sh_cdp_n_r2.txt', 'sh_cdp_n_r3.txt', 'sh_cdp_n_sw1.txt']))
