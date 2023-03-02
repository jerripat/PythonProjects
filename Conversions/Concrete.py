

import webbrowser


ans = input("Would you like to open the concreate calculator? (y/n) :")
url = 'https://www.concretenetwork.com/concrete/howmuch/calculator.htm#slab-calc'

if ans == "y":
   webbrowser.open(url)
else:
   print("OK...Good-bye")
   exit()