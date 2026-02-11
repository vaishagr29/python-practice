
# # 1. Print all elements in a nested list
# # Given nested_list = [[1, 2], [3, 4]], print each element.

# l=[[1, 2], [3, 4]]
# for i in l:
#     for j in i:
#         print(j,end=" ")
# print()

# # 2. Print key-value pairs from dictionary
# # Given d = {'A': 1, 'B': 2}, print each key and value.

# d={'A': 1, 'B': 2}
# for key, value in d.items():
#     print(f"{key}:{value}")
# print()

# # 3. Print the multiplication table of 3 up to 5.
# for i in range(1,6):
#     print(f"3x{i}={3*i}")
# print()

# # 4. Print all characters of words in a list
# # Given words = ["hi", "ok"], print all characters.

# l = ["hi", "ok"]
# for w in l:
#     for c in w:
#         print(c,end=" ")
# print()

# # 5. Print all Armstrong numbers between 100 and 999.
# # (An Armstrong number is a number equal to the sum of the cubes of its digits, e.g., 153 → 1³+5³+3³=153)

# for i in range(100, 1000):
#     n = i
#     sum = 0
#     while n > 0:
#         digit = n % 10
#         sum += digit ** 3
#         n //= 10
#     if sum == i:
#         print(i,end=" ")

# print("\n")

# # 6. Print all prime numbers between 10 and 50.
# # (A prime number is divisible only by 1 and itself)

# for i in range(10,51):
#     if i>1:
#         flag=True
#         for j in range(2,i):
#             if i % j == 0:
#                 flag=False
#                 break
#         if flag:    
#             print(f"{i} is a prime number")
# print()
            


# # 7. Print all Fibonacci numbers less than 50.
# # (Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13… each number is the sum of the previous two)

# prev=0
# next=1
# sum=1
# print(0,end=" ")
# print(1,end=" ")

# while(sum<50):
#     print(sum,end=" ")
#     sum=prev+next
#     prev=next
#     next=sum
# print()

n=5
if n%3:
    print("odd")
else:
    print("even")
