# #תרגילי list arrays

# ##1
# a = ['I love python']
# print(a*5)
#
# #2
# a = []
# for i in range(1,11):
#     a.append(i)
# print(a)
#
# #3
a=[]
for i in range(10):
    num=int(input('enter 10 number: '))
    a.append(num)
print(a)
x=sorted(a)
print(x)
#
# #4.א
# a=[]
# sum=0
# count=0
# count1=0
# count3=0
# max=0
# for i in range(4):
#     x = int(input('enter 11 numbers: '))
#     if x > 0:
#      a.append(x)
#      sum=sum+x
#     else:
#         break
# print(a, sum)
# for j in (a):
#     print(j/11)
# for d in(a):
#     if d > 10:
#         count=count+1
# print('count big 10=',count)
# for f in(a):
#     if f < 10:
#         count1+=1
# print('count small 10=',count1)
# for m in(a):
#     if (m>max):
#         max=m
# print('the max number is=',max)
# print('the even number is=' ,end=' ')
# for s in(a):
#     if s%2==0:
#         print(s,end= '')
# print('the number/3is=',end= ' ')
# for t in(a):
#     if t%3==0:
#         count3=count3+1
#         print(count3, )
#
# #5
# lst = [1, 2, 2, 4, 5, 5, 6]
# for i in range(len(lst)):
#     if lst[i]==lst[i-1]:
#         print(lst[i])
# y=3
# lst.insert(0,3)
# print(lst)
# x=int(input('enter number'))
# lst.insert(1,x)
# j=x+y
# lst.insert(2,x+y)
# print(lst)
# lst.insert(3,x*y*j)
# print(lst)
#
# #6
# dani=[]
# yemi=[]
# for i in range(2):
#     dani.append(int(input('enter score dani:')))
#     yemi.append(int(input('enter score yemi:')))
# for i in range(len(dani)):
#     for j in range(len(yemi)):
#         if dani[i]==yemi[j]:
#             print(dani[i], 'same score')
#
# #7
#
# ste=(input('even or odd string length: '))
# if len(ste)%2==0:
#     print('even',len(ste),ste)
# else:
#     print('odd',len(ste),ste)
#
# #8
# a=[]
# sum=0
# for i in range(3):
#     name = input('enter name of the trail: ')
#     length = int(input('enter length of the trail: '))
#     sum=sum+length
#     if length>10:
#         a.append(length)
# print(a)
# print(sum)
#
# #9
# ארגז שתייה=35
# פחות מ4 ארגזים דמימשלוח=10
#
#
# count=0
# bottle=35
# for i in range(2):
#     name=input('Enter your name: ')
#     order=int(input('Insert a number of bottle crates: '))
#     if order < 4:
#         print(bottle*order+10)
#     elif order >4:
#         print(bottle*order)
#     if order >20:
#         count=count+1
#         print(count)
#
# #10
# count=0
# sum=0
# for i in range(2):
#     lastname=input('enter last name:' )
#     numkids=int(input('enter numbers of kids: '))
#     if numkids > 3:
#         print('discount')
#         sum=sum+numkids
#         print(sum)
#
#11
# סוגי דם A O AB B
# מבצע תרומה  איש 25
count=0
for i in range(25):
    name = input('enter name:')
    type_bloode = input('enter blood type:A/O/AB/B')
    years = int(input('enter your years:  '))
    if type_bloode=='o':
        count=count+1

    print(name,type_bloode,years)
print('Number of blood types o=',count)
