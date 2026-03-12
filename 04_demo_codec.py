s1 = '你好234kkkdd'

print(s1.encode())
print(s1.encode('utf-8'))

bys = b'\xe4\xbd\xa0\xe5\xa5\xbd234kkkdd'

s2 = bys.decode()

print(s2)