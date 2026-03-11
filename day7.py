# def printname():
#     name1=input("Enter your name")
#     print(name1)
#     print(int(len(name1)))
#
# printname()

str2=[]
str3=""
def wordtoarray():
    str1 = input("You are the major user, select a word for hangman for user 2")
    print(str1)
    for i in range(0,int(len(str1))):
        str2.append(str1[i])
    print(str2)
    print(int(len(str2)))

str4=[]

def addblanks():
    str3=""

    for i in range(0,int(len(str2))):
        if i%2==0:
            str4.append(str2[i])
            # str3=str3+str2[i]
        else:
            str4.append('_')
            # str3 = str3+"_"
    print(str4)
    for i in str4:
        str3+=i

    print(str3)

def takecharinput():
    print(str2)
    chr1=""
    chr1=str(input("Guess a letter"))
    # print(chr1)
    for i in range(0,int(len(str2))):
        if i%2==1:
            # print("letter is",(str2[i]))
            if(str(chr1)==str(str2[i])):
                # print("inside",str2[i])
                str4.insert(i,str(chr1))
                str4.pop(i+1)
        else:
            "Your selction is wrong"

    # print("you are correct")
    str5=""
    for i in range(0,len(str4)):
       str5=str5+(str(str4[i]))
    print("changed word is",str5)


wordtoarray()
addblanks()

while (any('_' in s for s in str4)):
    takecharinput()


