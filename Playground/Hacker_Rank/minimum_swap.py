arr=[7,1,3,2,4,5,6]

def nextCommon(arr):
    t=arr[0]
    for i in range(len(arr)):
        if(t!=arr[0]):
            return t
        t+=1


def swap(arr,a,b,a_index):
    b_index=arr.index(a)
    arr[a_index]=a
    arr[b_index]=b
    return arr

def minimumSwaps(arr):
    # default=CreateDefault(arr)
    n=-1
    count=0
    i=1
    while(i<=len(arr)):
        n+=1
        if(i!=arr[n]):
            count+=1
            arr=swap(arr,i,arr[n],n)
            i+=1
            # n=i-2
            continue
        i+=1
    return count


print(minimumSwaps(arr))
