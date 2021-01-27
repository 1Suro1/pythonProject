s = [1, 2, 3]
print([i * 2 for i in s])
s = [1, 2, 3]
d = 0
for i in range(len(s)):
    d += s[i]**2
print(d)
s = [3, 6.7, 11.8]
for i in range(len(s)):
    s[i] //=2
print(s)
s = 'Hello world'
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()
print(s)