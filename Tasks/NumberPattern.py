# 1. Right-angled Number Triangle
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
print()

# 2. Inverted Right-angled Number Triangle  
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

n=5
for r in range(1,n+1):
    for c in range(1,n+2-r):
        print(c,end=" ")
    print()
print()

# 3. Right-aligned Number Triangle
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

n=5
for row in range(1,n+1):
    print(" "*((n-row)*2),end="")
    for col in range(1,row+1):
        print(col,end=" ")
    print()

# 4. Pyramid of Same Numbers
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5

n=5
for row in range(1,n+1):
    print(" "*(n-row),end="")
    for col in range(1,row+1):
        print(row,end=" ")
    print()
print()


# 5. Floyd's Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n=5
num=0
for row in range(1,n+1):
    for col in range(1,row+1):
        num+=1
        print(num,end=" ")
    print()
print()

# 6. Left-aligned Descending Numbers
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

print("Left-aligned Descending Numbers")

for i in range(1,n+1):
    for col in range(n+1-i,0,-1):
        print(col,end=" ")
    print()
print()



# 7. Number Pyramid (Floyd's Triangle with alignment)
#     1
#    2 3
#   4 5 6
#  7 8 9 10
# 11 12 13 14 15
print("Number Pyramid (Floyd's Triangle with alignment")

n=5
num=1
for row in range(1,n+1):
    print(" "*(n-row),end="")
    for col in range(1,row+1):
        print(num,end=" ")
        num+=1
    print()
print()

# 8. Number Triangle with Reverse Row Order
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5

print("Number Triangle with Reverse Row Order")

n=5
for i in range(n,0,-1):
    for col in range(i,n+1):
        print(col,end=" ")
    print()
print()












