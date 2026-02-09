'''
1. Square Pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
2. Right-angled Triangle
*
* *
* * *
* * * *
* * * * *
3. nverted Right-angled Triangle
* * * * *
* * * *
* * *
* *
*
4. Pyramid
    *
   * *
  * * *
 * * * *
* * * * *
5. Inverted Pyramid
* * * * *
 * * * *
  * * *
   * *
    *
    
6. Right-aligned triangle
        *
      * *
    * * *
  * * * *
* * * * *
7. Inverted right-aligned triangle
* * * * * 
  * * * *
    * * *
      * *
        *
        
8. diamond pattern
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *

'''

'''# 1. Square Pattern
        * * * * *
        * * * * *
        * * * * *
        * * * * *
        * * * * *
'''
n=5
for i in range(1,n+1):
    print("* "*n)

print()

'''

    2. Right-angled Triangle
    *
    * *
    * * *
    * * * *
    * * * * *

'''

n=5
for i in range(1,n+1):
    print("* "*i)

print()

'''
        3. nverted Right-angled Triangle
        * * * * *
        * * * *
        * * *
        * *
        *
'''

n=5
for i in range(1,n+1):
    print("* "*(n+1-i))

print()

'''
        4. Pyramid
            *
           * *
          * * *
         * * * *
        * * * * *
'''

n=5

for i in range(1,n+1):
        
        print(" " * (n-i) + "* "*(i))
        # print("*"*(2*i-1))
print()
'''
            5. Inverted Pyramid
            * * * * *
             * * * *
              * * *
               * *
                *
'''

n=5

for i in range(1,n+1):
        
        print(" " * (i-1) + "* "*(n-i+1))
print()
'''
    6. Right-aligned triangle
            *
          * *
        * * *
      * * * *
    * * * * *
'''

n=5
for i in range(1,n+1):
    print( " " * ((n-i)*2)+"* "*(i) )
print()

'''
        7. Inverted right-aligned triangle
         * * * * * 
           * * * *
             * * *
               * *
                 *
'''

n=5
for i in range(1,n+1):
    print( " " * ((i-1)*2)+"* "*(n+1-i) )
print()

'''
8. diamond pattern
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *

'''

n=5

for i in range(1,n+1):
        
        print(" " * (n-i) + "* "*(i))

for i in range(1,n+1):
        
        print(" " * (i-1) + "* "*(n-i+1))

print()




