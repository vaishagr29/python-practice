def solve(l):
    mp={}
    for i in l:
        if i not in mp:
            mp[i]=1
        else:
            mp[i]+=1
    return [i for i,j in mp.items() if j==1]

n=int(input("enter n"))
num=list(map(int,input().split()))
print(*(solve(num)))