inp = open('INPUT.TXT', 'r')
outp = open('OUTPUT.TXT', 'w')
data = inp.readlines()

n = int(data[0])
m = n
k = 0

while n >= 10:
    n //= 10
    k += 1

k = 10 ** k
new = m % 10 * k + m % k // 10 * 10 + m // k

outp.write(str(new * new))

inp.close()
outp.close()