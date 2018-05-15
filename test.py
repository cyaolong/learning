#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# def char_to_hex(str):
#     hex = str.encode('utf8').encode('hex')
#     print hex

word = raw_input()
# w = str(word)

word_list = map(str, word.split(","))
print(word_list)