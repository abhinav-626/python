n = input()
l = len(n)
s= 0
i = 0
while i<l:
    s += int(n[i])**l
    i += 1
if int(n) == s:
    print('no. is armstrong')
else:
    print('no is not armstrong')
