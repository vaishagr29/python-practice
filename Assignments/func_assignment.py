# =========================================
# PART 1: CODING QUESTIONS (1–30)
# =========================================

# 1. Non-parameterized function
def hello():
    print("Hello World")

# 2. Parameterized function (sum)
def add(a, b):
    print(a + b)

# 3. Return square
def square(n):
    return n * n

# 4. Print product (no return)
def product(a, b):
    print(a * b)

# 5. Lambda to double
double = lambda x: x * 2

# 6. Lambda add
add_lambda = lambda a, b: a + b

# 7. Higher-order function
def apply_func(func, lst):
    return [func(x) for x in lst]

# 8. Enumerate
for i, val in enumerate(['a', 'b', 'c']):
    print(i, val)

# 9. Zip
z = list(zip([1,2,3], ['x','y','z']))

# 10. Eval
result = eval("2+3*4")

# 11. Local & Global
x = 10
def scope():
    x = 5
    print("Local:", x)
scope()
print("Global:", x)

# 12. Factorial recursion
def fact(n):
    return 1 if n == 0 else n * fact(n-1)

# 13. Fibonacci recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# 14. Decorator
def start_decorator(func):
    def wrapper():
        print("Function started")
        func()
    return wrapper

# 15. Generator even numbers
def even_gen(n):
    for i in range(2, n+1, 2):
        yield i

# 16. Iterator
class MyIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            val = self.lst[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

# 17. Prime check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 18. List of squares
def squares(lst):
    return [x*x for x in lst]

# 19. Variable arguments
def sum_all(*args):
    return sum(args)

# 20. Reverse string recursion
def reverse(s):
    return s if len(s) == 0 else reverse(s[1:]) + s[0]

# 21. GCD
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

# 22. Multiple return
def sum_product(a, b):
    return a+b, a*b

# 23. Palindrome
def is_palindrome(s):
    return s == s[::-1]

# 24. Lambda max
max_val = lambda a, b: a if a > b else b

# 25. Filter odd
def filter_even(lst):
    return list(filter(lambda x: x % 2 == 0, lst))

# 26. Enumerate comprehension
enum_list = [(i, val) for i, val in enumerate(['a','b','c'])]

# 27. Zip dict comprehension
d = {k:v for k,v in zip(['a','b'], [1,2])}

# 28. Eval user input
# expr = input("Enter expression: ")
# print(eval(expr))

# 29. Time decorator
import time
def time_decorator(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time:", end-start)
    return wrapper

# 30. Generator squares
def square_gen():
    for i in range(1, 11):
        yield i*i


# =========================================
# PART 2: INTERVIEW (2-LINE ANSWERS)
# =========================================

def interview_answers():

    # 1. Parameterized functions take inputs, non-parameterized do not.
    #    They differ based on whether arguments are passed or not.
    pass

    # 2. Return functions give back a value, non-return only perform action.
    #    Return is used when result is needed later.
    pass

    # 3. Lambda functions are small anonymous functions.
    #    Example: lambda x: x*2
    pass

    # 4. Higher-order functions take functions as arguments.
    #    Example: map(), filter()
    pass

    # 5. enumerate gives index + value, zip combines lists.
    #    eval executes string as Python expression.
    pass

    # 6. Local variables inside function, global outside.
    #    nonlocal used in nested functions.
    pass

    # 7. Recursion is function calling itself.
    #    Example: factorial
    pass

    # 8. Decorator modifies function behavior.
    #    Used with @ syntax.
    pass

    # 9. Generator uses yield, iterator uses __next__().
    #    Generators are memory efficient.
    pass

    # 10. Multiple values returned using tuple.
    #     Example: return a, b
    pass


# =========================================
# PART 3: OUTPUTS
# =========================================

# 1.
# Output:
# Hi

# 2.
# Output:
# No output (function defined, not called)

# 3.
# Output:
# <function> (lambda defined, not executed)

# 4.
# Output:
# [0, 1, 4]

# 5.
# Output:
# [2, 3, 4]

# 6.
# Output:
# [(0, 'apple'), (1, 'banana')]

# 7.
# Output:
# [(1, 3), (2, 4)]

# 8.
# Output:
# 13

# 9.
# Output:
# No output (function defined, not called)

# 10.
# Output:
# No output (decorator defined, not used)