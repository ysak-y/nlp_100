# -*- coding: utf-8 -*-


a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a = a.split(' ')

b = [1, 5, 6, 7, 8, 9, 15, 16, 19]

c = {}


for idx, s in enumerate(a):

    print s
    print idx
    if idx + 1 in b:
        
        c[s[0]] = idx + 1

    else:

        c[s[0:2]] = idx + 1


print c 
