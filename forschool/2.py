import math

inp = open('INPUT.TXT', 'r')
outp = open('OUTPUT.TXT', 'w')
data = inp.readlines()

n = int(data[0])
times = math.ceil(math.log(n, 2))

a = [1]

for i in range(times):
    length = len(a)
    for j in range(length):
        if a[j] == 0:
            a.append(1)
        else:
            a.append(0)

result = str(a[n - 1]) + ' ' + str(times)
outp.write(result)

inp.close()
outp.close()