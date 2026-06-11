num = int(input("enter the num:"))
if (num % 2 == 0):
    print("even")
else:
    print("odd")

num1 = int(input("enter the num:"))
num2 = int(input("enter the num:"))
num3 = int(input("enter the num:"))

if (num1 > num2):
   # print("num1 is greater")
#
elif (num2 > num3):
    print("num2 is greater")
else:
    print("num3 is greater")  

num = int(input("enter the num:"))
c = num % 7
if (c == 0):
   # print("divisible by 7",num)
else:
    print("not divisible by 7",num ) 
   
       
list1 = [input("1st movie:"),input("2nd movie"),input("3nd movie")]


list1 =[1,2,3]
listcpy = list1.copy()
listcpy.reverse()
if (listcpy == list1):
    print("palindrome")    
else:    print("not palindrome")   
  
list = [A,B,C,A,A,B]
print(list.count("A"))