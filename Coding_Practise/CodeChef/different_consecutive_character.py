testCases=int(input())
# testCases=3
testCasesInputs=[
    [2,"11"],
    [4,"0101"],
    [5,"00100"]
]

while testCases>0:
    n=int(input())
    s=input()
    # n=testCasesInputs[3-testCases][0]
    # s=testCasesInputs[3-testCases][1]
    # Your code goes here
    testCases -= 1
    # s=s.split("")
    ordered_s=[]
    operations_Count=0
    while len(s)>0:
        if(len(ordered_s)==0):
            ordered_s.append(s[0])
            s=s[1:]
        elif s[0]==ordered_s[-1]:
            ordered_s.append("0" if s[0]=="1" else "1")
            operations_Count+=1
        else:
            ordered_s.append(s[0])
            s=s[1:]
    print(operations_Count)