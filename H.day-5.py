
'''
**Designe a calculator which will correctkly slove all the problem except the follwoing ones:
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

