# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

user_ip = input('Enter IP address: ')
#user_ip = '10.0.1.1'

if user_ip.count('.') != 3: #Проверим три точки
    print('Неправильный IP-адрес (три точки)')
else:
    ip = user_ip.split('.')
    if len(ip) != 4:
        print('Неправильный IP-адрес (не 4 октета)')
    else:
        #распакуем для проверки
        oct0, oct1, oct2, oct3 = ip
        if oct0.isdigit() and oct3.isdigit()  and oct3.isdigit()  and oct3.isdigit():
            #print('isdigit')
            ip = [int(oct) for oct in ip]
            print(ip)
            oct0, oct1, oct2, oct3 = ip
            if (oct0 >=0 and oct0 <= 255) and (oct0 >=0 and oct0 <= 255) and (oct0 >=0 and oct0 <= 255) and (oct0 >=0 and oct0 <= 255):
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
        else:
            print('Неправильный IP-адрес')