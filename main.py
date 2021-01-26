"""
Тестовый код
на Python

"""
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
s=r'C:\megahucker\new.txt'
print(s)
s = 'te' 'st'
print(s)
s1 = 'hello,'
s2 = 'world'
s3 = s1+s2
print(s3)
name = 'root'
id = str(0)
print('My name' + name + ' my id '+id)
print('hi '*5)
s = 'Hello world!'
print(s[0])
print(s[-1])
print(str((time.time_ns() - x1) / 1000000), "ms")
