#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#16进制转换
#字符串->hex
def char_to_hex(str):
    hex = str.encode('utf8').encode('hex')
    print hex

#hex->字符串
def hex_to_char(str):
    char = str.decode('hex')
    print char

#输入q可随时退出
while True:
    choose = input('Please choose y/n for ChartoHex/HextoChar: ')
    if choose == 'q':
        break
    elif choose == 'y':
        while True:
            word = input('Please input a word(or q to go back): ')
            if word == 'q':
                break
            else:
                char_to_hex(word)

    elif choose == 'n':
        while True:
            hex = input('Please input a hex(or q to go back): ')
            if hex == 'q':
                break
            else:
                hex_to_char(hex)
