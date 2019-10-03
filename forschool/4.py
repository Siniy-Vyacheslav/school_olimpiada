inp = open('INPUT.TXT', 'r')
outp = open('OUTPUT.TXT', 'w')
n = int(inp.readline())
a = []
for i in range(n):
    a.append([0] * n)
mark = 1

for i in range(n):
    for j in range(i, n - i):
        a[i][j] = mark
        a[j][i] = mark
        a[n - i - 1][j] = mark
        a[j][n - i - 1] = mark
    
    mark += 1

for i in range(len(a)):
    string = ''
    for j in range(len(a)):
        string += str(a[i][j]) + ' '
    outp.write(string + '\n')