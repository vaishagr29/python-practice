'''
generator - it yeilds one value at a time,
also called lazy execution used when we want to 
fetch large dataset
it fetch by using yeild keyword
'''

def generator_function():
    for i in range(1,11):
        yield i

gen = generator_function()

for j in gen:
    print(j)


#next func- generates value as needed

print(next(gen))
print(next(gen))

#iterator - it iterates over an object like a loop, one element at a time.
#to control the iteration

lst =[10,20,30,40,50]

i = iter(lst)
print(next(i))
print(next(i))
