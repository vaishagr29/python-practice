'''
#count method
data= (24,23,34,55,34,79,45,76,40)
cnt = data.count(34)
print(cnt)

#index method
data= (24,23,34,55,34,79,45,76,40)
i = data.index(34)
print(i)
i1= data.index(34,3)
print(i1)
'''

# data= (24,23,34,55,34,79,45,76,40)
# *first,*sec,*third,*forth =data


info = ("disha",25,45,26,17,"pune","maharashtra")
Name,*Age,City,State=info
print("Name =",Name)
print("Age =",Age)
print("City =",City)
print("State =",State)



