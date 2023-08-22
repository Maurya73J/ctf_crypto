import numpy as np
mr = {}
for i in range(16):
    j = format(i, '04b')
    mr[j] = chr(ord('f')+i)

file = open("inputs.txt","w+")
for i in range(8):
    for j in range(128):
        pr = np.binary_repr(j, width=8)
        es = 'ff'*i + mr[pr[:4]] + mr[pr[4:]] + 'ff'*(8-i-1)
        file.write(es)
        file.write(" ")
    file.write("\n")
file.close()
