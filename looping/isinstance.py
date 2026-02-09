##isinstance() function  it is basically used for tyoe checking ,like tyoe(x)
#flattening of list

lst=[[20,30],8,9,[56,10]]

flattened_list=[]

for i in lst:
    if(isinstance(i,list)):
        for j in i:
            flattened_list.append(j)
    else:
        flattened_list.append(i)
print(flattened_list) 

lst2=[10,30,[20,78],(20,89,15),16,81]

flattened_list2=[]
for i in lst2:
    if(isinstance(i,list)):
        for j in i:
            flattened_list2.append(j)
    elif(isinstance(i,tuple)):
        for j in i:
            flattened_list2.append(j)
    else:
        flattened_list2.append(i)
print(flattened_list2)

