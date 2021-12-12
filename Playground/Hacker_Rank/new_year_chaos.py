q=[1,2,5,3,7,8,6,4]
default=[1,2,3,4,5,6,7,8]
count=0

def swap(q,a,b,a_index):
    # q[a_index]=b
    bribes=0
    for k in range(a_index,len(q)):
        bribes+=1
        if(q[k]==b):
            # q[a_index]=b
            # q[k]=a
            del q[k]
            q.insert(a_index,b)
            break
        
    return [q,bribes-1]

def createArray(lenght):
    c=[]
    for i in range(lenght):
        c.append(i+1)
    return c

def checkIntegrity(default,q):
    for i in range(len(q)):
        if(default[i]!=q[i]):
            data=swap(default,default[i],q[i],i)
            default=data[0]
            global count
            if(data[1]>2):
                print("Too chaotic")
                return "no"
            count+=data[1]
            return default
    return "ok"

def minimumBribes(q):
    global count
    default=createArray(len(q))
    n=-1
    for i in range(len(q)):
        default=checkIntegrity(default,q)
        if(default=="ok"):
            # print("Done")
            print(count)
            break
        elif(default=="no"):
            break
minimumBribes(q)
