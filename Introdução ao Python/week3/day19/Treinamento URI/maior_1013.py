a, b, c = input().split()
a = int(a); b = int(b); c = int(c)

valores = [a, b, c]
if c > a:
    a = c

print('{} eh o maior'.format(int((a+b+abs(a-b))/2)))