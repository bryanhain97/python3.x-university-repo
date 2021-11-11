# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 20:39:09 2021

@author: seher
"""

# calculations

# 2.2.1
x = -1.2
a = 3 **(4+x)
print("a=", a)

# 2.2.2
b = 931.8//a
print("b=", b)

# 2.2.3
c = (-2*x+b) % a
print("c=", c)


# logical expressions

# 2.2.4
if (a < b):
    print("Die Aussage ist wahr, a ist kleiner b.")
else:
    print("Die Aussage ist falsch, a ist kleiner b.")

# 2.2.5
print((True or False) and not (a > b) != (-3 > -1))

# Zusatzfrage

s = 3
t = 0

print(t != 0 and s/t > 0)


# Die Fehlermeldung zerodivisionerror erscheint,
# da t als null definiert wurde und
# somit nicht dividiert werden kann.
# Wenn t ungleich null definiert wird, ist die Aussage false,
# da t=0 ist und
# dies wird in der Konsole auch so ausgegeben.
# Das "and s/t>0" wird vom Programm nicht weiter untersucht.
