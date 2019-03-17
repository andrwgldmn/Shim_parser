#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import requests

value = None
def help():
        print (' ----------------------------')
        print ('\n Eng:\n Put near this script your log.txt to work with 1 item, copy a link of your logcat from Web to work with 2 item. \n')
        print (' \n Рус: Положите рядом со скриптом ваш log.txt с 1 пунктом, скопируйте ссылку на ваш логкат из сети для работы с 2 пунктом. \n ')
        print (' \n Укр: Покладіть біля цього скрипта ваш log.txt для роботи з 1 пунктом, скопіюйте ссилку на ваш  логкат з мережі для роботи з 2 пунктом. \n ')
        print (' \n Made by andrwgldmn \n') 
        print (' ----------------------------')

def shimparser_inet():
        with open('shims.c', 'w') as output_file:
            url = raw_input(' Enter the URL: ')
            r = requests.get(url)
            text = r.text
            pat = r"""cannot\s*locate\s*symbol\s*"(.+?)"\s*referenced\s*"""
            for symbol in re.findall(pat, text):
                part_one = "#include <stdint.h>\nvoid "
                part_two = "{}".format(symbol)
                part_three = "(){}\n"
                shim = (part_one + part_two + part_three)
                output_file.write(shim)

        File = open('shims.c', 'r')
        str_list = set()
        for i in File.readlines():
            if i not in str_list:
                str_list.add(i)
        File.close()
        File = open('shims.c', 'w')
        for j in str_list:
            File.write(j)
        os.system('cls' if os.name == 'nt' else 'clear') 

def shimparser_local():
        with open('log.txt') as input_file, open('shims.c', 'w') as output_file:
            text = input_file.read()
            pat = r"""cannot\s*locate\s*symbol\s*"(.+?)"\s*referenced\s*"""
            for symbol in re.findall(pat, text):
                part_one = "#include <stdint.h>\nvoid "
                part_two = "{}".format(symbol)
                part_three = "(){}\n"
                shim = (part_one + part_two + part_three)
                output_file.write(shim)

        File = open('shims.c', 'r')
        str_list = set()
        for i in File.readlines():
            if i not in str_list:
                str_list.add(i)
        File.close()
        File = open('shims.c', 'w')
        for j in str_list:
            File.write(j)
        os.system('cls' if os.name == 'nt' else 'clear') 

while value != 0:
    help()
    print (' ----------------------------')
    value = int(input(" 1) English \n 2) Русский \n 3) Українська \n ---------------------------- \n "))
    if (value != 1 and value != 2 and value != 3 ):
        print ("\n Program has been terminated. \n" )
    if (value == 1):
        while value != 0:
            print (' ----------------------------')
            value = int(input(" Choose category: \n \n 0) Exit \n 1) Parsing local log.txt for getting shims \n 2) Parsing log.txt for getting shims rules via Internet (log.txt will be given from your entered URL) \n  ---------------------------- \n "))
            
            if (value == 0):
                print('-' * 28 + '\n Thanks!\n' + '-' * 28)

            elif (value == 1):
                shimparser_local()

            elif (value == 2 ):
                shimparser_inet()

    if (value == 2):
        while value != 0:
            print (' ----------------------------')
            value = int(input(" Выберите категорию: \n \n 0) Выход \n 1) Анализ локального log.txt для получения шимок \n 2) Анализ log.txt для получения шимок через Internet (log.txt будет скачан по ссылке, которую Вы введёте. URL) \n   ---------------------------- \n "))
            
            if (value == 0):
                print('-' * 28 + '\n Спасибо!\n' + '-' * 28)

            elif (value == 1):
                shimparser_local()

            elif (value == 2 ):
                shimparser_inet()

    if (value == 3):
        while value != 0:
            print (' ----------------------------')
            value = int(input(" Оберіть категорію: \n \n 0) Вихід \n 1) Аналіз локального log.txt для отримання шимок \n 2) Аналіз log.txt для отримання шимок через Internet (log.txt буде завантажений з URL, яку Ви введете) \n  ---------------------------- \n "))
            
            if (value == 0):
                print('-' * 28 + '\n Дякую!\n' + '-' * 28)
            elif (value == 1):
                shimparser_local()

            elif (value == 2 ):
                shimparser_inet()
