from funcc import blockbyte, exp, convfunc
from pyfinite import ffield

psw = "jgjllmgkjklqkqfkkgihkploitmijimq"

mr = {}
for i in range(16):
    j = format(i, '04b')
    mr[j] = chr(ord('f')+i)

m={}
for i in mr:
    j=mr[i]
    m[j]=list(i)

inputfile="inputs.txt"
outputfile="outputs.txt"


inputfi = open(inputfile, 'r')
outputfi = open(outputfile, 'r')
pex= [[] for i in range(8)]
pai=[[[] for i in range(8)] for j in range(8)]

fi = ffield.FField(7)
for k, (iline, oline) in enumerate(zip(inputfi.readlines(), outputfi.readlines())):
    instr = []
    outstr = []
    for inn in iline.strip().split(" "):
        instr.append(blockbyte(inn)[k])
    for outt in oline.strip().split(" "):
        outstr.append(blockbyte(outt)[k])
    for i in range(1, 127):
        for j in range(1, 128):
            f = True
            for iin, oout in zip(instr, outstr):
                if ord(oout) != exp(fi.Multiply(exp(fi.Multiply(exp(ord(iin), i), j), i), j), i):
                    f = False
                    break
            if f:
                pex[k].append(i)
                pai[k][k].append(j)
inputfi = open(inputfile, 'r')
outputfi = open(outputfile, 'r')
for k, (iline, oline) in enumerate(zip(inputfi.readlines(), outputfi.readlines())):
    if k <= 6 :
        instr= []
        outstr= []
        for inn in iline.strip().split(" "):
            instr.append(blockbyte(inn)[k])
        for outt in oline.strip().split(" "):
            outstr.append(blockbyte(outt)[k+1])
        for i in range(1, 128):
            for a, b in zip(pex[k+1], pai[k+1][k+1]):
                for r, s in zip(pex[k], pai[k][k]):
                    f = True
                    for iin, oout in zip(instr, outstr):
                        if ord(oout) != exp(int(fi.Multiply(exp(fi.Multiply(exp(ord(iin), r), s), r), i))^int(fi.Multiply(exp(fi.Multiply(exp(ord(iin), r), i), a),b)), a):
                            f = False
                            break
                    if f:
                        pex[k+1] = [a]
                        pai[k+1][k+1] = [b]
                        pex[k] = [r]
                        pai[k][k] = [s]
                        pai[k][k+1] = [i]
print(pex)
print(pai)

for numi in range(6):
    nuz = numi+ 2

    expm = [e[0] for e in pex]
    linmat = [[0 for i in range(8)] for j in range(8)]

    for i in range(8):
        for j in range(8):
            linmat[i][j] = 0 if len(pai[i][j]) == 0 else pai[i][j][0]
    inputfi = open(inputfile, 'r')
    outputfi = open(outputfile, 'r')
    for k, (iline, oline) in enumerate(zip(inputfi.readlines(), outputfi.readlines())):
        if k > (7-nuz):
            continue
        instr = []
        outstr = []
        for i in iline.strip().split(" "):
            instr.append(blockbyte(i))
        for i in oline.strip().split(" "):
            outstr.append(blockbyte(i))
        for i in range(1, 128):
            linmat[k][k+nuz] = i
            f = True
            for inps, outs in zip(instr, outstr):
                if convfunc(inps, linmat, expm)[k+nuz] != ord(outs[k+nuz]):
                    f = False
                    break
            if f:
                pai[k][k+nuz] = [i]
    inputfi.close();
    outputfi.close();

linmat = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        if(len(pai[i][j]) == 0):
             linmat[i][j] = 0
        else: linmat[i][j] = pai[i][j][0]

print(linmat)
print(expm)
def passout(password):
    pw = blockbyte(password)
    out = ""
    for k in range(8):
        for ans in range(128):
            an=format(ans,'08b')
            cs=mr[an[:4]]+mr[an[4:]]
            inn = out + cs+(16-len(out)-2)*'f'
            if ord(pw[k]) == convfunc(blockbyte(inn), linmat, expm)[k]:
                out += cs
                break
    return out
print((blockbyte(passout(psw[:16]))+blockbyte(passout(psw[16:]))))
