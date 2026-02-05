# 1. Print the multiplication table of 5.

for i in range(1,11):
    print(f"5 x {i} = {5*i}")

# 2. Print the multiplication table of any number given by the user.

n= int(input("enter num"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# 3. Find the sum of the first 10 natural numbers.
sum=0
for i in range(1,11):
    sum+=i

print(sum)

# 4. Find the factorial of a given number.

#4!=1*2*3*4
ans=1
n= int(input("enter num for factorial"))
for i in range(1,n+1):
    ans*=i
print(ans)
      
# 5. Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i*i)
print()

# 6. Print cubes of numbers from 1 to 10.
for i in range(1,11):
    print(i*i*i)
print()

# 7. Calculate the sum of even numbers from 1 to 50.
sum=0
for i in range(2,51,2):
    sum+=i

print(sum)

# 8. Calculate the sum of odd numbers from 1 to 50.
sum=0
for i in range(1,51,2):
    sum+=i

print(sum)

# 9. Print the product of numbers from 1 to 5.
p=0
for i in range(1,6):
    p*=i

print(p)
# 10. Print numbers from 1 to 10 along with their double (e.g., 1 → 2, 2 → 4).
for i in range(1,11):
    print(f"{i} -> {i*i}")
print()

