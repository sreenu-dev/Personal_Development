inp="MCMXCIV"
dicto={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
inprev=inp[::-1]
outi=0
for x in range(0,len(inprev)):
    if(x>0 and dicto[inprev[x-1]]>dicto[inprev[x]]):
        outi-=dicto[inprev[x]]
    else:
        outi+=dicto[inprev[x]]
print(outi)