testCaseCount=int(input())
# testCaseCount=3
test_inputs=[
    ["ABCDE","EDCBA"],
    ["ROUND","RINGS"],
    ["START","STUNT"]
]

while testCaseCount > 0:
    s=input()
    # s=test_inputs[3-testCaseCount][0]
    t=input()
    # t=test_inputs[3-testCaseCount][1]
    # Your code goes here
    # print(s,t)
    testCaseCount -= 1
    for i in range(len(s)):
        if s[i]!=t[i]:
            print("B",end="")
        else:
            print("G",end="")
    print("")

