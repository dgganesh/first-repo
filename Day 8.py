# first exercise
# ========================
# def greet():
#     print("")
#     print("How are you doing")
#     print(" I am good thanks")
#
# greet()
#
# def greet_name(name):
#     print(name)
#     print("How are you doing {name}")
#     print("Hope you are doing well",name)
#
# greet_name("ganesh")
from operator import indexOf

# Second exercise:
#=======================
# def weeks_left(num):
#     nmr = 0
#     weeks=0
#     nmr=num
#     weeks=(90-num)*52
#     print("You have",weeks, " left with you ")
#
# s=int(input("Enter your age"))
# weeks_left(s)
#
# def two_param(nam,loca):
#     print(f"Hello there, {nam}")
#     print(f"I see you are from, {loca}, thats a great place to be in")
#
#
# two_param(loca="chennai",nam="Ganesh")
#

# # THird exercise
# # ========================
# def count_love(nam1,nam3):
#     j=0
#     n=0
#     k=0
#     l=0
#     m=0
#
#     nam5=str(nam1)+str(nam3)
#     print(f"combination is {nam5}")
#     nam2="true"
#     nam4="love"
#     for i in range(0,len(nam5)):
#        for j in range(0,len(nam2)):
#            if nam5[i]==nam2[j]:
#                n+=1
#                print(f"i is {nam5[i]} and j is {nam2[j]}")
#                print(n)
#
#     for k in range(0,len(nam5)):
#        for l in range(0,len(nam4)):
#            if nam5[k]==nam4[l]:
#                m+=1
#                print(f"k is {nam5[k]} and l is {nam4[l]}")
#                print(m)
#     print(f"total love scope for {nam1} and {nam3} is", str(n)+str(m))
#
#
# count_love("Ganesh guru ","Raksha lava")
#
# Fourth project
#===================
let= [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'], ['t'], ['u'], ['v'], ['w'], ['x'], ['y'], ['z']]
num1= int(input("Enter the number for encoding"))
# word= str(input("Enter the word to encode"))
orig_let= [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n'], ['o'], ['p'], ['q'], ['r'], ['s'], ['t'], ['u'], ['v'], ['w'], ['x'], ['y'], ['z']]

ar_ind = 0

let.reverse()
for i in range (num1):
    let.append(let[i])
    print(let[i])

for j in range (num1):
    let.pop(0)

let.reverse()
print(f"changed array is {let}")
print(f"original array is {orig_let}")

def gen_has():
    old_word=str(input("Enter the word to change"))
    new_word = ""
    for g in range (len(old_word)):
        # j=str(orig_let.index(les[g]))
        # orig_let.
        j = str((old_word[g]))
        print(f"letter are{g},{j}")
        ar_ind=orig_let.index([j])
        print(ar_ind)
        print("new array letters are")
        print((let[ar_ind])[0])
        new_word=new_word+str(let[ar_ind][0])
        print(new_word)

gen_has()