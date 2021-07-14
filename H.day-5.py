#if and elif:

'''
var1=65
var2=int(input("Enter a number: "))
if var1>var2:
    print("lesser")
elif var2==65:
    print("equal")
else:
    print("grater")
'''
'''
a=5
age=int(input("Enter your age: "))

if age<18:
   # if age<18:
        print("you are eigible")
elif age==18:
    print("not decied yet")
else:
    print("you are not eligible for typeing")
'''
"""
list=[2,3,4,5]
print(5 in list)
print(15 not in list)
if 5 in list:
    print("yes 5 in the list")
else:
    print(" not in a list")
"""
'''
**Designe a calculator which will correctkly slove all the problem
except the follwoing ones:
45*3=555, 56+9=77,56/6=4
'''
inp1 = input("operator")
print("Enter 1st number: ")
val1= int(input())
print("Enter 2nd number: ")
val2= int(input())
val3=val1+val2
val4=val1*val2
val5=val1-val2
val6=val1/val2

if inp1 =="+":

    if val1+ val2==56+9:
        print("the result is: ")
        print(77)
    else:
        print("The result is: ")
        print(val3)
elif inp1 =="*":

    if val1 * val2==45*3:
        print("The result is: ")
        print(555)
    else:
        print("The result is: ")
        print(val4)

elif inp1=="-":

    if val1-val2==5-5:
        print("The Result is: ")
        print(1)
    else:
        print("The Result is: ")
        print(val5)
elif inp1=="/":

    if val1/val2==56/5:
        print("The Result is: ")
        print(4)
    else:
        print("The result is: ")
        print(val6)
else:
    print("invalid choice")

