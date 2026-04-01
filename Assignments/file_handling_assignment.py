# =========================================
# PART 1: CODING QUESTIONS (1–25)
# =========================================

# 1. Create file and write
with open("sample.txt", "w") as f:
    f.write("Hello World")

# 2. Read file
with open("sample.txt", "r") as f:
    print(f.read())

# 3. Append data
with open("sample.txt", "a") as f:
    f.write("\nPython is fun")

# 4. Read line by line
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# 5. Delete first line
with open("sample.txt", "r") as f:
    lines = f.readlines()
with open("sample.txt", "w") as f:
    f.writelines(lines[1:])

# 6. Insert line at beginning
with open("sample.txt", "r") as f:
    data = f.read()
with open("sample.txt", "w") as f:
    f.write("New First Line\n" + data)

# 7. Write numbers 1–10
with open("data.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")

# 8. Sum numbers
with open("data.txt", "r") as f:
    total = sum(int(x.strip()) for x in f)
print(total)

# 9. Function to write list
def write_list(lst, filename):
    with open(filename, "w") as f:
        for item in lst:
            f.write(item + "\n")

# 10. Count lines
def count_lines(filename):
    with open(filename, "r") as f:
        return len(f.readlines())


# =========================================
# REAL-TIME SCENARIOS (11–20)
# =========================================

# 11. Log file
import datetime
with open("app.log", "a") as f:
    f.write(str(datetime.datetime.now()) + "\n")

# 12. Read CSV
with open("file.csv", "r") as f:
    for row in f:
        print(row.strip())

# 13. Log errors
try:
    x = 10 / 0
except Exception as e:
    with open("error.log", "a") as f:
        f.write(str(e) + "\n")

# 14. Read large file in chunks
def read_chunks(file):
    with open(file, "r") as f:
        while True:
            chunk = f.read(10)
            if not chunk:
                break
            print(chunk)

# 15. Context manager
with open("safe.txt", "w") as f:
    f.write("Safe write")

# 16. Delete file
import os
if os.path.exists("temp.txt"):
    os.remove("temp.txt")

# 17. Copy file
with open("source.txt", "r") as s, open("dest.txt", "w") as d:
    d.write(s.read())

# 18. Rename file
os.rename("old.txt", "new.txt")

# 19. Word frequency
with open("sample.txt", "r") as f:
    words = f.read().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)

# 20. Replace word
with open("sample.txt", "r") as f:
    data = f.read()
data = data.replace("Hello", "Hi")
with open("sample.txt", "w") as f:
    f.write(data)


# =========================================
# ADDITIONAL OPERATIONS (21–25)
# =========================================

# 21. Check file exists
if os.path.exists("sample.txt"):
    print("File exists")

# 22. Binary file write
with open("bin.dat", "wb") as f:
    f.write(b"Hello")

# 23. Read binary
with open("bin.dat", "rb") as f:
    print(f.read().decode())

# 24. Append multiple lines
lines = ["Line1\n", "Line2\n"]
with open("sample.txt", "a") as f:
    f.writelines(lines)

# 25. Clear file
open("sample.txt", "w").close()


# =========================================
# PART 2: INTERVIEW QUESTIONS (2 LINES)
# =========================================

def interview_answers():

    # 1. Text files store data as readable characters.
    #    Binary files store data in byte format.
    pass

    # 2. with automatically closes file after use.
    #    It prevents memory leaks and errors.
    pass

    # 3. Large files read using chunks or line by line.
    #    This avoids loading entire file in memory.
    pass

    # 4. Use os.path.exists() to check file presence.
    #    Prevents FileNotFoundError.
    pass

    # 5. Use try-except while opening/reading files.
    #    Handles errors like missing files.
    pass

    # 6. read() reads entire file, readline() one line.
    #    readlines() returns list of lines.
    pass

    # 7. Use os.remove() to delete file.
    #    Check existence before deleting.
    pass

    # 8. Use 'a' mode to append data.
    #    It adds content without deleting old data.
    pass

    # 9. 'w' overwrites, 'a' appends, 'r+' reads and writes.
    #    Modes control file operations.
    pass

    # 10. Open source and destination files.
    #     Copy using read() and write().
    pass


# =========================================
# PART 3: OUTPUTS
# =========================================

# 1.
# Output:
# Hello

# 2.
# Output:
# 12345

# 3.
# Output:
# ['Python\\n', 'Java\\n', 'C++\\n']

# 4.
# Output:
# (No output, file updated)

# 5.
# Output:
# True/False (depends if file exists)

# 6.
# Output:
# Python

# 7.
# Output:
# File not found

# 8.
# Output:
# (No output, file contains 0,1,2)

# 9.
# Output:
# First 5 characters of file

# 10.
# Output:
# (No output, file contains 'abc')