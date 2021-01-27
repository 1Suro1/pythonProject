"""
Тестовый код
на Python

"""
from builtins import id

import builtins

import s, time

x1 = time.time_ns()


def print_hi():
    print(__name__)
    s.lol()
    print(2 + 3)
    print(2 - 3)
    print(2 * 3)
    print(1.0 / 5.0)
    print(1 // 5.0)
    print(6 % 2)
    print(- 5 - 3)
    print(5 ** 2)
    print(144 ** 0.5)
    print((2 + 3) * 4)
    print(.5 + 2)
    print(0.1 + 0.2)


print_hi()
test = None
print(test)
print(type(test))
if test is None or test is not None:
    test = 1
    print(test)
x, y = (1, 5)
print(x, y)
# None, '', 0 = False
print(bool("false"))
# Экранированная последовательность
words = "Test \n \\ \"ss\" 'words'"
print(words)
test = '''\
sdsd
'lol'\
'''
print(test)
s = r'C:\megahucker\new.txt'
print(s)
s = 'te' 'st'
print(s)
s1 = 'hello,'
s2 = 'world'
s3 = s1 + s2  # Конкатенация
print(s3)
name = 'root'
id = 0
print('My name' + name + ' my id ' + str(id))
print('hi ' * 5)
s = 'Hello World!'
print(s[0])
print(s[-1])  # len-1
# s[0] = 'D' не изменяемая
# [X:Y:Z] - x-начало y-конец z-шаг среза
print(s[0:12])
print(s[0:12:2])
print(s[::-1])
print(len(s))  # Количество символов в строке
print(s.capitalize())  # Первый символ в вверхном остальные в нижнем регистре,не изменяет строку
print(s.center(20))
print(s.count("o", 0, 5))
print(s.index('o'))
print(s.replace('l', 't'))
print(s.split()[0])
print(s.isdigit())  # цифры
print(s.isalpha())  # символы
print(s.isalnum())  # и символы и цифры
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': id})
print('Test %s id:%d' % ('test', id))
print('%.1f' % (40.55))
print('Test {0} {0} {1} '.format("test", 40.1))
print('graph {x} {y}'.format(x=1, y=2))
print(f'Test {name} {id + 5}')
i = 1
while i <= 10:
    print(i, end=" ", sep="!")
    i += 1
print()
for i in range(11):
    print(i, end=" ")
else:
    print()
    print("done")
s = [1, 1, 1, 1, 2, 'hello', [1, 1, 1], True]
print(s)
s1 = list('hello')
print(s1)
s2 = list((1, 2, 3))
print(s2)
s3 = [i for i in 'hello']
print(s3)
s4 = [i for i in 'hello world' if i not in ['a', 'e', 'i', 'o', 'u', ' ']]
print(s4)
s5 = list(range(3, 5, 1)) and list(range(10))
print(s5)
for i in range(1,10):
    for j in range(1,10):
        print(f'{i}*{j}={i*j}\t', end=" ")
    print(end="\n")
s5 = [1, 2, 3, 'hello', ['test', 1], 'world', True]
s5[0] = 5
print(s5)
print(s5[0:3])
s5[0:3] = [10, 15, 'lol']
print(s5[0:3])
s5.append('lol')
print(s5)
s6 = [1, 2, 3]
s5.extend(s6)
print(s5)
s5 += s6
print(s5)
s5.insert(0,'test1')
print(s5)
s5.remove(1)
print(s5)
k = s5.pop()
print(k, s5)
x = 20
print(x, builtins.id(x))
x = 10
print(x, builtins.id(x))
t = [1, 2, 3]
print(t, builtins.id(t))
t.append(5)
print(t, builtins.id(t))
x = 10
y = x
print(x, builtins.id(x))
print(y, builtins.id(y))
x = 15
print(x, builtins.id(x))
print(y, builtins.id(y))
del x, y, t, k, s2, s5, s4, s3, s, id, test, words

print()
print(str((time.time_ns() - x1) / 1000000), "ms")
