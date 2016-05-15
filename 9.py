# -*- coding: utf-8 -*-

import re

def cipher(char):

    a = re.compile('[a-z]')
    b =a.match(char)

    if b is not None:

        char = 219 - ord(char)

    return str(char)


sentence = 'this Is A pen'
cipher_sentence = ''


for i in sentence:

    cipher_sentence += cipher(i)

print cipher_sentence
