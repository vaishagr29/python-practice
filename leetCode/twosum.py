#Two sum

#target and numbers array find two index whose sum = target

target=int(input("enter a num target"))
num=[1,2,3,4,5]

mp={}

for i in range(len(num)):
    if (target-num[i]) in mp:
        print(mp[target-num[i]],i)
        break
    else:
        mp[num[i]]=i

