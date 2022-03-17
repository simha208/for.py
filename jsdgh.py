#1
# num=int(input("enter num"))
# if num <50:
#     print("little")
# elif num >50:
#     print("big")

# num1=int(input("enter number"))
# num2=int(input("enter number"))
# num3=int(input("enter number"))
# if num1> num2 and num1>num3:
#     print(num1)
# elif num2 >num3 and num2>num1:
#     print(num2)
# elif num3>num1 and num3>num2:
#     print(num3)
#
# if num1< num2 and num1<num3:
#     print(num1)
# elif num2 <num3 and num2<num1:
#     print(num2)
# elif num3<num1 and num3<num2:
#     print(num3)

#3
# num=int(input("enter number"))
# if num %2==0:
#     print(num)
#4
# num=int(input("enter number :"))
# if num < 40 and num %2==0:
#     print(num)

#5
# num=int(input("enter number"))
# if num>100:
#     print(num*5)
# elif num< 100 :
#     print(num*10)
# elif num ==100 :
#       print(num+10)

#6
# num=int(input("enter number"))
# if num % 2 !=0:
#     print("odd ")
# elif num %2==0 and num //5 and num> 30:
#     print("even")
#7
# num=int(input("enter age:"))
# num1=int(input("enter height:"))
# num2=input("enter name:")
# if num > 18:
#     if num1 < 154:
#          if num2[0]=='a' or num2[0]=='b':
#
#                print("Was accepted")
#          else:print("No match")
#     else :
#         print("No match")
# else:
#     print("No match")

#8
# num=52
# while num> 23:
#     print(num)
#     num -=10

#2
# number=100
# while number < 250:
#      if number % 2 != 0:
#           print(number)
#      number +=1
#
#
# num1=int(input("enter number:"))
# num2=int(input("enter number:"))
# num3=int(input("enter number:"))
# num4=int(input("enter number:"))
# num5=int(input("enter number:"))
# num6=int(input("enter number:"))
#
# if num1> num2 and num1>num3 and num1>num4 and num1>num5 and num6:
#     print(num1)
# elif num2> num1 and num2>num3 and num2>num4 and num2>num5 and num2>num6:
#     print(num2)
# elif num3>num1 and num3>num2 and num3>num4 and num3>num5 and num3>num6:
#     print(num3)
# elif num4>num1 and num4>num2 and num4>num3 and num4>num5 and num4>num6:
#     print(num4)
# elif num5>num1 and num5>num2 and num5 > num3 and num5> num4 and num5>num6:
#     print(num5)
# elif num6>num1 and num6>num2 and num6>num3 and num6>num4 and num6>num5:
#     print(num6)
#
# if num1<num2 and num1<num3 and num1<num4 and num1<num5 and num6:
#     print(num1)
# elif num2< num1 and num2<num3 and num2<num4 and num2<num5 and num2<num6:
#     print(num2)
# elif num3<num1 and num3<num2 and num3<num4 and num3<num5 and num3<num6:
#     print(num3)
# elif num4<num1 and num4<num2 and num4<num3 and num4<num5 and num4<num6:
#     print(num4)
# elif num5<num1 and num5<num2 and num5< num3 and num5<num4 and num5<num6:
#     print(num5)
# elif num6<num1 and num6<num2 and num6<num3 and num6<num4 and num6<num5:
#     print(num6)
#
max=0
min=1000000
countEven=6
countBig=6
for i in range(6):
    num=int(input("please enter number"))
    if num>max:
        max=num
    if num<min:
        min=num
    if num>5:
        countBig+=1
    if num%2==0:
        countEven+=1

print(max)
print(min)