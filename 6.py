# -*- coding: utf-8 -*-


def text2ngrams(text, n=3, unit_word=True):

    a = []
    if unit_word == True:
        text = text.split(' ')

    for i in range(len(text)):
        c = text[i: i + n]
        a.append(c)
        if i + n == len(text):
            break
    return a

a = 'foo bar hoge foo bar hoge foo bar hoge foo bar hoge'

print text2ngrams(a, 2)
print text2ngrams(a, 2, False)
