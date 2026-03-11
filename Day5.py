# yday code practice
# str1 = ["one","two","three"]
# print (str1)
# str1.append("four")
# print (str1)
# str1.append(str(input("Enter details to be in the list")))
# print(str1)
# if str1[4]=="five":
#     print("Correct name added")
# else:
#     print("String not correct")

# For loop
str1 =["one","two","three","four","five","six","seven","eight"]

for strer in str1:
    print(strer)
    print("HEllo", strer,"How are you")

print(str1)

str2 = ""

for one1 in str1:
    str2=str2+" "+one1
    print(one1)
    print(str2)

num2=0
list1 = [123,123,532,345,582,234,834,670,234,999]
num3=sum(list1)
print(num3 )
for num1 in list1:
    if num1>num2:
        num2=num1
        print(num2)
#
# print("highest number in the list is ", num2)

num11=0
for strr1 in range(1,11):
    num11+=strr1
    print(strr1)
    print(num11)
num12=0
for sum1 in range(1,25,2):
    print(sum1)
    num12+=sum1
    print(num12)


for num in range(1,100):
    if ((num%3==0) and (num%5==0)):
        print("BuzzWizz")
    elif(num%5==0):
        print("wizz")
    elif (num%3==0):
        print("Buzz")
    else:
        print(num)



