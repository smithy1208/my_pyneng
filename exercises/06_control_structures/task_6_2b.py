# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
bad_ip = True

while bad_ip:
    user_ip = input('Enter IP address: ')
    #user_ip = '10.0.1.1'

    if user_ip.count('.') != 3: #Проверим три точки
        print('Неправильный IP-адрес (три точки)')
        continue
    else:
        ip = user_ip.split('.')
        #распакуем для проверки
        oct0, oct1, oct2, oct3 = ip
        if oct0.isdigit() and oct3.isdigit()  and oct3.isdigit()  and oct3.isdigit():
            #print('isdigit')
            ip = [int(oct) for oct in ip]
            print(ip)
            oct0, oct1, oct2, oct3 = ip
            if (oct0 >=0 and oct0 <= 255) and (oct0 >=0 and oct0 <= 255) and (oct0 >=0 and oct0 <= 255) and (oct0 >=0 and oct0 <= 255):
                bad_ip = False # Правильный IP
                first_bite = ip[0]
                if first_bite >=1 and first_bite <= 223:
                    print('unicast')
                elif first_bite >= 224 and first_bite <= 239:
                    print('multicast')
                elif user_ip == '255.255.255.255':
                    print('local broadcast')
                elif user_ip == '0.0.0.0':
                    print('unassigned')
                else:
                    print('unused')
            else:
                print('Неправильный IP-адрес')
                continue
