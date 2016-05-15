# -*- coding: utf-8 -*-


a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

b = a.split(" ")

print b
c = []

for i in b:
    i = i.replace(',', '')
    i = i.replace('.', '')
    print i
    print len(i)
    c.append(len(i))


print c
