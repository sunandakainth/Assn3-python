#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kaint
#
# Created:     17-05-2025
# Copyright:   (c) Kaint 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
fact_num=int(input("enter the number"))
print("the factorial is:", fact( fact_num))
