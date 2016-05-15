# -*- coding: utf-8 -*-


def template(x, y, z):
    s = str(x) + 'の時の' + str(y) + 'は' + str(z)
    return s
    
a = template(12, '気温', 22.4)
print a
