inp = open('INPUT.TXT', 'r')
outp = open('OUTPUT.TXT', 'w')
data = inp.readlines()

for i in range(1, len(data)):
    isSimilar = True
    data[i] = data[i].rstrip('\n').split()
    a = [0] * 10
    b = [0] * 10

    for j in range(len(data[i][0])):
        el = int(data[i][0][j])
        if a[el] == 0:
            a[el] += el % el + 1

    for j in range(len(data[i][1])):
        el = int(data[i][1][j])
        if b[el] == 0:
            b[el] += 1

    for j in range(10):
        if a[j] != b[j]:
            isSimilar = False
    
    if isSimilar:
        outp.write('YES' + '\n')
    else:
        outp.write('NO' + '\n')

inp.close()
outp.close()