# import random
#
# letts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# splcha = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']
# #
# sum2=int(input("How many digits pass you want?"))
# sum1= int(input("how many alphabets pass you want?"))
# # sum3=int("How manu numbers")
#
# passd = ""
#
# count1= int(len(letts))
# count2= int(len(numbs))
# count3= int(len(splcha))
#
# passnew=""
#
# for i in range(0,sum1):
#     passd+=letts[random.randint(0,len(letts)-1)]
# passnew+=passd
# passd=""
# print("first", passnew)
# for a in range(0,sum2):
#     passd+=numbs[random.randint(0,len(numbs)-1)]
# passnew+=passd
# print("second", passnew)
# passd=""
#
# for b in range(0,(13-(sum1+sum2))):
#     passd+=splcha[random.randint(0,len(splcha)-1)]
# print("third", passnew)
# passnew+=passd
#
# print(passnew)
# print(len(passnew))
#
#
#
#
