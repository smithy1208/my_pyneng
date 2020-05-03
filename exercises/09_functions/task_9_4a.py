# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4, но функция convert_config_to_dict должна поддерживать еще один уровень вложенности.
При этом, не привязываясь к конкретным разделам в тестовом файле.
Функция должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

При записи команд в словарь, пробелы в начале строки надо удалить.

Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Секция итогового словаря на примере interface Ethernet0/3.100:

'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}

Примеры других секций словаря можно посмотреть в тесте к этому заданию.
Тест проверяет не весь словарь, а несколько разнотипных секций.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from pprint import pprint

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)


def convert_config_to_dict(config_filename):
    result = {}
    with open(config_filename) as f:
        second_level = False
        for line in f:
            if (not line.rstrip()) or line.lstrip().startswith('!') or ignore_command(line, ignore):
                # пустая строка, или начинается с '!', или команда должна быть проигнорирована
                pass
            else:
                if not line.startswith(' '):  # Если строка не начинается с пробела
                    second_level = False
                    parent_command = line.rstrip()

                    result[parent_command] = []
                else:  # Строка начинается с пробела
                    c_level = len(line) - len(line.lstrip())

                    if c_level == 1:  # собираем список команд первого уровня вложенности
                        child_command = line.strip()
                        if second_level:  # В блоке был второй уровень - заполняем словарь
                            result[parent_command][child_command] = []
                        else:
                            if not parent_command in result.keys():
                                result[parent_command] = []
                            result[parent_command].append(child_command)
                    elif c_level == 2:  # собираем список команд второго уровня
                        # нужен флаг который снимаем когда переходим к parent_command
                        second_level = True
                        grandchild_command = line.strip()
                        # преобразуем список в словарь
                        if type(result[parent_command]) == list:
                            result[parent_command] = {key: [] for key in result[parent_command]}
                        # Добавляем в список команду второго уровня
                        if not child_command in result[parent_command].keys():
                            result[parent_command][child_command] = []
                        result[parent_command][child_command].append(grandchild_command)

    return result


if __name__ == '__main__':
    print(
    convert_config_to_dict('config_r1.txt')
    )
