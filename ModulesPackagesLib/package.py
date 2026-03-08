'''
package -  collection of modules, and it contains __init__.py file,
which tells that this folder is package.

calculate/ -> package
___init___.py
  add.py -> module
  sub.py -> module
  div.py -> module

shopping_app -> normal folder
   login/ -> package
   __init__.py
   login_page.py -> module
   payment/ -> package
   __init__.py
   payment_process.py -> module


'''

from calculator import addition, substraction

addition.add(10,20)
substraction.sub(60,40)

