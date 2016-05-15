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


a = "paraparaparadise"
b = "paragraph"

a = text2ngrams(a, 2, False)
b = text2ngrams(b, 2, False)


print "a + b is ", a + b

def get_sum_of_sets(n_gram_a, n_gram_b):

    return set(n_gram_a + n_gram_b)

def get_difference_sets(n_gram_a, n_gram_b):

    return set(list(set(n_gram_a) - set(n_gram_b)) + list(set(n_gram_b) - set(n_gram_a)))

def get_product_sets(n_gram_a, n_gram_b):

    return get_sum_of_sets(n_gram_a, n_gram_b) - get_difference_sets(n_gram_a, n_gram_b)

def has_word(word, sentence):
    return word in sentence


print 'sum of sets is ', get_sum_of_sets(a, b)

print 'differense sets is ', get_difference_sets(a, b)

print 'product sets is', get_product_sets(a, b)

print has_word('se', a)
print has_word('se', b)
