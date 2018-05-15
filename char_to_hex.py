#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#16进制转换
#字符串->hex
def char_to_hex(str):
    hex = str.encode('utf8').encode('hex')
    print (hex)

#hex->字符串
def hex_to_char(str):
    char = str.decode('hex')
    print (char)

#输入中文，转换为hex（输入q可随时退出）
while True:
    choose = raw_input('Please choose y/n for ChartoHex/HextoChar: ')
    if choose == 'q':
        break
    elif choose == 'y':
        while True:
            word = raw_input('Please input words(or q to go back): ')
            word_list = map(str, word.split(","))
            if word == 'q':
                break
            else:
                map(char_to_hex, word_list)

#输入hex，转换为中文
    elif choose == 'n':
        while True:
            hex = raw_input('Please input hex strings(or q to go back): ')
            hex_list = map(str, hex.split(","))
            if hex == 'q':
                break
            else:
                map(hex_to_char, hex_list)