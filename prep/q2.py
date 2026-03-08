# Problem Statement:
# You are given two strings str1 and str2.
# Your task is to remove all characters from str1 that are present in str2.
# Return the modified string after removing the common characters.
# If no characters from str1 are present in str2, return str1 as it is.
# Input Format:
# The first line contains a string str1.
# The second line contains a string str2.
# Output Format:
# Print the modified string after removing all characters from str1 that are present in str2.
# Constraints:
# 1 ≤ length of str1 ≤ 104
# 1 ≤ length of str2 ≤ 104
# Strings contain only lowercase English alphabets.
def solve(s1,s2):
    dummy=[]
    for i in s1:
        if i not in s2:
            dummy.append(i)
    return "".join(dummy)

str1=input("enter string")
str2=input("enter string")

ans=solve(str1,str2)
print(ans)


