t_inp=4
n_inp=[2,4,6,4]
s_inp=["00","0011","101010","1001"]

t = int(input())
# t=t_inp

textMapping={'00':'A','01':'T','10':'C','11':'G'}

while t > 0:
    n = int(input())
    # n=n_inp[t_inp-t]
    s = input()
    # s=s_inp[t_inp-t]
    # Your code goes here
    t -= 1
    # print(n,s)
    for i in range(0,n,2):
        print(textMapping[s[i:i+2]],end="")
    print("")