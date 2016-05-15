# -*- coding: utf-8 -*-

import random

def mess_word(word):

    if len(word) > 4:
        head = word[0]
        foot = word[-1]

        body = ''

        word = list(word[1: len(word) - 1])
        len_body = len(word)

        for i in range(len_body):

            idx = random.randint(0, len(word) - 1)
            s = word.pop(idx)
            body += s

        body += foot
        head += body

        return head

    else:

        return word


word = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

word = word.split(' ')

for i in word:

    w = mess_word(i)

    print w
