
# 1.  From a list of numbers, filter out only the even numbers.

# 2.  From a list of numbers, filter out only the odd numbers.  do it

# 3.  Given a list of words, filter out words whose length is greater than 5.

# 4.  From a list of integers, filter numbers divisible by 3.
num_list =[1, 2, 3, 4, 5, 6, 7, 8, 9]

ans_list=list(filter(lambda n : n%3==0, num_list))
print(ans_list)

# 5.  From a list of names, filter names starting with the letter 'A'.
words=["anjali","ayushi","vaish","vini"]
ans_list=list(filter(lambda n : n[0]=='a', words))
print(ans_list)

# 6.  From a list of strings, filter out palindromes.
def ispalindrome(n):
    i=0
    j=len(n)-1
    while i<=j:
        if n[i] != n[j]:
            return False
        i+=1
        j-=1
    return True

words=["aiia","poop","tokt","vao"]
ans_list=list(filter(lambda n : ispalindrome(n), words))
# ans_list = list(filter(lambda n: n == n[::-1], words))
print(ans_list)

# 7.  From a list of ages, filter out ages greater than or equal to 18 (adults).
num_list =[1, 22, 33, 4, 65, 6, 27, 8, 9]
ans_list=list(filter(lambda n : n>=18, num_list))
print(ans_list)

# 8.  From a list of numbers, filter prime numbers only.
def isPrime(n):
    if n<2 :return False
    for i in range(2,n):
        if((n%i==0)):
            return False
    return True
num_list =[1, 2, 3, 4, 5, 6, 7, 8, 9]
ans_list=list(filter(lambda n : isPrime(n), num_list))
