# Star pattern

# 1. Butterfly Pattern

# *       *
# **     **
# ***   ***
# **** ****
# *********
# **** ****
# ***   ***
# **     **
# *       *

n=5
for i in range(1,n):
    print("*"*i,end="")
    print(" "*(2*(n-i)-1),end="")
    print("*"*i,end="")
    print()
print("*"*(2*n - 1))
for i in range(n-1,0,-1):
    print("*"*i,end="")
    print(" "*(2*(n-i)-1),end="")
    print("*"*i,end="")
    print()


print()



# 2. Hollow Right Triangle

# *
# * *
# *   *
# *     *
# * * * * *
n=5
for i in range(1,n+1):
    if(i==1):
        print("*")
    elif(i==5):
        print("* "*n)
    else:
        print("*"+" "*(2*i-3)+"*")



# 3. Hollow Pyramid
#     *.      #0 spaces
#    * *.     #3 spaces
#   *   *     #7 spaces
#  *     *.   #6 spaces
# * * * * *
n=5

for i in range(1,n+1):
        print(" "*(n-i),end="")
        if(i==1):
            print("*")
        elif(i==5):
            print("* "*n)
        else:
           print("*", end="")
           print(" "*(2*i-3), end="")
           print("*")


# 4. Hollow diamond - 

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

n=5

for i in range(1,n+1):
        print(" "*(n-i),end="")
        if(i==1):
            print("*")
        else:
           print("*", end="")
           print(" "*(2*i-3), end="")
           print("*")

for i in range(n-1,0,-1):
        print(" "*(n-i),end="")
        if(i==1):
            print("*")
        else:
           print("*", end="")
           print(" "*(2*i-3), end="")
           print("*")


# 5. Mirror Right Pascal’s Triangle
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

n = 5

for i in range(1,n+1):
    print("  "*(n-i),end="")
    print("* " * i)

for i in range(n-1,0,-1):
    print("  "*(n-i),end="")
    print("* "*i)

# Number Pattern


# 1. Mirror Right Number Triangle

#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

n=5
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
         print(j,end=" ")
    print()
print()

# 2. Odd Number Pyramid

#     1
#    3 3
#   5 5 5
#  7 7 7 7
# 9 9 9 9 9

n=5
num=1
for i in range(1,n+1):
    print(" "*(n-i),end="")
    j=1
    while j <i+1:
         if(num%2!=0):
                print(num,end=" ")
                j+=1
         else:
                num+=1
    num+=1
    print()
print()


# 3. Inverted Continuous Numbers

# 1 2 3 4 5
# 6 7 8 9
# 10 11 12
# 13 14
# 15

num=1
n=5
for i in range(n,0,-1):
     for j in range(1,i+1):
            print(num,end=" ")
            num+=1
     print()
print()

# 4. Centered Number Pyramid

#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

n=5
num=1
for i in range(1,n+1):
    print(" "*(n-i),end="")
    j=1
    while j <i+1:
        print(i,end=" ")
        j+=1
    print()
print()



# 5. Reverse Number Triangle

# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1


n=5
for i in range(n,0,-1):
     for j in range(n,i-1,-1):
            print(j,end=" ")
     print()
print()


# Alphabet Pattern

# 1. Continuous Alphabets

# A
# B C
# D E F
# G H I J
# K L M N O

n=5
num=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num+=1
    print()
print()
     

# 2. Inverted Alphabet Right Triangle

# A B C D E
# A B C D
# A B C
# A B
# A

n=5
for i in range(1,n+1):
    for j in range(65,70-i+1):
        print(chr(j),end=" ")
    print()
print()

# 3. Alphabet Pyramid with Repeated Letters

#     A
#    B B
#   C C C
#  D D D D
# E E E E E

n=5
num=65
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(num),end=" ")
    num+=1
    print()
print()
