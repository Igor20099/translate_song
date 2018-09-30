import os
import re

letters = {
    "а":"a",
    "б":"b",
    "в":"v",
    'г':"g",
    "д":'d',
    "е":"e",
    'ё':'e',
    "ж":"j",
    "з":'z',
    "и":'i',
    "й":'i',
    "к":'k',
    "л":'l',
    'м':'m',
    "н":'n',
    'о':'o',
    "п":"p",
    "р":'r',
    'с':'s',
    "т":"t",
    "у":"u",
    "ф":'f',
    "х":'h',
    "ц":'c',
    "ч":'ch',
    'ш':'sh',
    "щ":'sh',
    'ы':'i',
    'э':'e',
    "ю":'y',
    "я":'ya',
    '-':'-',
    ' ':' ',
    '(':'(',
    ')':')',
    "a":'a',
    "b":"b",
    "c":"c",
    'd':"d",
    "e":'e',
    "f":"f",
    "g":"g",
    "h":'h',
    "i":'i',
    "j":'j',
    "k":'k',
    "l":'l',
    'm':'m',
    "n":'n',
    'o':'o',
    "p":"p",
    "q":'q',
    'r':'r',
    "s":"s",
    "t":"t",
    "u":'u',
    "v":'v',
    "w":'w',
    "x":'x',
    'y':'y',
    "z":'z',
    "0":'0',
    "1":'1',
    "2":'2',
    "3":'3',
    "4":'4',
    "5":'5',
    "6":'6',
    "7":'7',
    "8":"8",
    "9":"9",
    '[':'[',
    ']':']',
    '#':'#'
}

old_filename =""
filename = ""
files = []
directory = ''

while directory == '':
    try:
        directory = input("Введите путь к папке с файлами: ")
        files = os.listdir(directory)
        os.chdir(directory)
    except:
        print('Такой папки не существует!.Пожалуйста введите правильный путь к папке!')
        directory = ''
print("-" * 100)
print()
num = 1
for file in files:
    fl = str(file)
    if fl.endswith('mp3'):
            old_filename = fl
            rename = old_filename.replace('mp3','')
            for let in rename.lower():
                for x, y in letters.items():
                    if let in x:
                        filename += y
            filename = filename.title()
            os.rename(old_filename,filename + ".mp3")
            print(str(num) + '.' + old_filename + " -> " + filename + ".mp3")
            filename=''
            num += 1
print()
print("-" * 100)
print('Все файлы успешно переименованы!')
