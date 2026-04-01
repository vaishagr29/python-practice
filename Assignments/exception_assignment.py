# =========================================
# PART 1: CODING QUESTIONS (1–20)
# =========================================

# 1. Handle division by zero
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Handle ValueError
try:
    x = int("abc")
except ValueError:
    print("Invalid integer")

# 3. try-except-else
try:
    x = 10 / 2
except:
    print("Error")
else:
    print("No exception")

# 4. try-finally
try:
    x = 10 / 0
except:
    pass
finally:
    print("Execution finished")

# 5. Raise ValueError
x = -1
if x < 0:
    raise ValueError("Negative not allowed")

# 6. Multiple exceptions
try:
    lst = [1]
    print(lst[5])
    d = {}
    print(d['a'])
except (IndexError, KeyError):
    print("Error occurred")

# 7. ZeroDivisionError friendly message
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Please enter non-zero number")

# 8. FileNotFoundError
try:
    f = open("file.txt")
except FileNotFoundError:
    print("File not found")

# 9. TypeError
try:
    x = "abc" + 5
except TypeError:
    print("Cannot add string and number")

# 10. Raise custom exception
s = "abc"
if len(s) < 5:
    raise Exception("String too short")

# 11. Invalid float
try:
    x = float("abc")
except ValueError:
    print("Invalid float")

# 12. Invalid list index
try:
    lst = [1,2]
    print(lst[10])
except IndexError:
    print("Index error")

# 13. else executes only if no error
try:
    print(10/2)
except:
    print("Error")
else:
    print("Executed successfully")

# 14. finally always executes
try:
    x = 10/0
except:
    print("Error")
finally:
    print("Always runs")

# 15. Raise exception if number < 0
num = -5
if num < 0:
    raise Exception("Negative number")

# 16. File permission error
try:
    f = open("/root/file.txt", "w")
except PermissionError:
    print("No permission")

# 17. Valid integer input
try:
    num = int("abc")
except ValueError:
    print("Enter valid integer")

# 18. Handle KeyError
try:
    d = {'a':1}
    print(d['b'])
except KeyError:
    print("Key not found")

# 19. Raise if not string
val = 123
if not isinstance(val, str):
    raise TypeError("Not a string")

# 20. Multiple exceptions one block
try:
    x = int("abc")
    y = [1][5]
except (ValueError, IndexError):
    print("Multiple error handled")


# =========================================
# PART 2: REAL-TIME EXAMPLES
# =========================================

# 1. Calculator division
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. File reading
try:
    open("config.txt")
except FileNotFoundError:
    print("Config file missing")

# 3. Form validation
try:
    age = int("abc")
except ValueError:
    print("Invalid age")

# 4. Cleanup using finally
try:
    print("DB operation")
finally:
    print("Connection closed")

# 5. Banking withdrawal
balance = 100
withdraw = 200
if withdraw > balance:
    raise Exception("Insufficient balance")


# =========================================
# PART 3: INTERVIEW ANSWERS (2 LINES)
# =========================================

def interview_answers():

    # 1. try-except handles runtime errors and prevents program crash.
    #    It allows graceful handling of exceptions.
    pass

    # 2. else runs only if no exception occurs.
    #    It is used for code that should execute when try is successful.
    pass

    # 3. finally always executes whether exception occurs or not.
    #    It is used for cleanup tasks.
    pass

    # 4. Custom exception is raised using raise keyword.
    #    Example: raise ValueError("Error")
    pass

    # 5. Exception handling deals with runtime errors.
    #    Error handling is a broader concept including all types of errors.
    pass

    # 6. Multiple exceptions handled using tuple in except.
    #    Example: except (ValueError, TypeError):
    pass

    # 7. Yes, try can be used with finally without except.
    #    finally will always execute.
    pass

    # 8. raise manually throws exception, assert checks condition.
    #    assert is used for debugging.
    pass

    # 9. It prevents crashes and improves reliability.
    #    Helps in handling unexpected situations.
    pass

    # 10. Syntax errors occur before execution.
    #     Exceptions occur during runtime.
    pass


# =========================================
# PART 4: OUTPUTS
# =========================================

# 1.
# Output:
# Division by zero error

# 2.
# Output:
# Invalid integer

# 3.
# Output:
# Hello
# No Error

# 4.
# Output:
# Finished

# 5.
# Output:
# ValueError: Negative value not allowed

# 6.
# Output:
# Index error occurred

# 7.
# Output:
# Key not found

# 8.
# Output:
# Start
# End

# 9.
# Output:
# Type error occurred

# 10.
# Output:
# (depends on input; if invalid → "Invalid input")