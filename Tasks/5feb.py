# 1. displaying hi 10 times
i = 1
while(i <= 10):
    print("hi")
    i += 1

# 2. displaying numbers from 1-10
i = 1
while(i <= 10):
    print(i)
    i += 1

# 3. displaying numbers from 25-50
i = 25
while(i <= 50):
    print(i)
    i += 1

# 4. displaying reverse numbers from 10-1
i = 10
while(i >= 1):
    print(i)
    i -= 1

# 5. display reverse from 50-25
i = 50
while(i >= 25):
    print(i)
    i -= 1

# 6. infinite loop with terminating condition
i = 1
while(True):
    print(i)
    i += 1
    if(i > 5):
        break

# 7. even numbers from 1 to 20
i = 1
while(i <= 20):
    if(i % 2 == 0):
        print(i)
    i += 1

# 8. sum of digits
n = int(input("enter number for sum of digits: "))
sum = 0
while(n > 0):
    sum += (n % 10)
    n //= 10
print(sum)

# 9. product of digits of number
n = int(input("enter number for product of digits: "))
prod = 1
while(n > 0):
    prod *= (n % 10)
    n //= 10
print(prod)

# 10. factors of a number using while loop
n = int(input("enter number for factors (while): "))
i = 1
while(i <= n):
    if(n % i == 0):
        print(i)
    i += 1

# 11. factors of number using for loop
n = int(input("enter number for factors (for): "))
for i in range(1, n+1):
    if(n % i == 0):
        print(i)

# 12. reverse of a number
n = int(input("enter number to reverse: "))
rev = 0
while(n > 0):
    rev = (rev * 10) + (n % 10)
    n //= 10
print(rev)

# 13. check palindrome
n = int(input("enter number to check palindrome: "))
temp = n
rev = 0
while(n > 0):
    rev = (rev * 10) + (n % 10)
    n //= 10
if(temp == rev):
    print("palindrome")
else:
    print("not palindrome")

# 14. Armstrong number
n = int(input("enter number to check armstrong: "))
temp = n
count = 0
while(temp > 0):
    count += 1
    temp //= 10

temp = n
sum = 0
while(temp > 0):
    digit = (temp % 10)
    sum += (digit ** count)
    temp //= 10

if(sum == n):
    print("armstrong")
else:
    print("not armstrong")

# 15. fibonacci series
a = 0
b = 1
i = 1
while(i <= 10):
    print(a)
    c = (a + b)
    a = b
    b = c
    i += 1

# 16. list of first 10 fibonacci series elements
fib = []
a = 0
b = 1
i = 1
while(i <= 10):
    fib.append(a)
    c = (a + b)
    a = b
    b = c
    i += 1
print(fib)

# 17. first fibonacci series till N
N = int(input("enter N for fibonacci: "))
a = 0
b = 1
while(a <= N):
    print(a)
    c = (a + b)
    a = b
    b = c

# 18. check prime number
n = int(input("enter number to check prime: "))
flag = True
if(n <= 1):
    flag = False
else:
    i = 2
    while(i < n):
        if(n % i == 0):
            flag = False
            break
        i += 1

if(flag):
    print("prime")
else:
    print("not prime")


# 1. Print numbers from 1 to 10, but stop when the number is 5 (use break).  
# 2. Print numbers from 1 to 10, but skip 5 (use continue).  
# 3. Traverse numbers from 1 to 20, stop when you find 13 (use break).  - do it
# 4. Traverse numbers from 1 to 20, skip multiples of 3 (use continue).  
# 5. Print characters of the string "python", but stop when you encounter 'h' (use break).