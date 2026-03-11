import random
print("random number between 2,10",random.randint(2,10))

int1=random.random()

if int1>0.5:
    print("heads")
else:
    print("tails")

later = ["one","two","three"]
print(later[random.randint(0,2)])
print(later)

later.append("four")
later.append("five")
print(later[random.randint(0,4)])
onne=["one","two","three"]
twwo=["four","five","six","seven","eight","nine"]
thhree=[onne,twwo]

print(onne)
print(twwo)
print(thhree)

list1=[1,2,3,4,5,6]
list2=[1,2,3,4,5,6]
if list1[random.randint(0,5)]>list2[random.randint(0,5)]:
    print("person1 wins")
elif list1[random.randint(0,5)]==list2[random.randint(0,5)]:
    print("Its draw between both of you")
else:
    print("Person2 wins")

