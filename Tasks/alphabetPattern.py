'''
Right-angled Alphabet Triangle
A
A B
A B C
A B C D
A B C D E
65 66 67 68 69
'''
'''
ASCII - American Standard Code for Information Interchange
unique integer value for each characters(letters, symbols, alphabet, digits/numbers)
A-Z : 65-90
a-z : 97-122
0-9 : 48-57 
chr() - 'character'
returns character for particular ascii value
ord() - 'ordinal'
returns ascii value for particular character
'''

# Right-angled Alphabet Triangle
# A
# A B
# A B C
# A B C D
# A B C D E
# 65 66 67 68 69


value = 71
print(chr(value))

char="L"
print(ord(char))

n=5
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
print()

# Right-angled Triangle of Same Alphabets
# A
# B B
# C C C
# D D D D
# E E E E E

n=5
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()
print()



