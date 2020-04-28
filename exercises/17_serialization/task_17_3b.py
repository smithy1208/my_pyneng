# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

import yaml
from pprint import pprint
from draw_network_graph import draw_topology

def transform_topology(topology_file_yaml):
    '''
    Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

    Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

    Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
        {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
         ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}
     '''
    result = {}
    result1 = {}

    with open(topology_file_yaml) as f:
        src = yaml.safe_load(f)

    # pprint(src)
    for k_host, v_host in src.items():
        # print(key, value)
        host = k_host
        for k_intf, v_intf in v_host.items():
            intf = k_intf
            # print(host, intf, tuple(v_intf.items())[0])
            new_key = (host, intf)
            result1[new_key] = tuple(v_intf.items())[0]

    for key, value in result1.items():
        if not key in result.values():
            result[key] = value

    return result


if __name__ == '__main__':
    topology_file = 'topology.yml'
    pprint(transform_topology(topology_file))
    draw_topology(transform_topology(topology_file))