#Exercise 1:
#===================================

#
# arr = {
#     "key1":"value1",
#     "key2":"value2",
#     "key3":"value3",
#     "key4":"value4",
# }
# print(arr)
# arr["key5"] = "value5"
# print(arr)
# print(arr["key3"])

#Exercise 2:
#=======================================================
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }
# def rank1(val1):
#     if val1>90:
#         print("outstanding")
#     elif (val1<=90 and val1>80):
#         print("OKish")
#     else:
#         print("fail")
# print(student_scores)
# print(f"harry got", rank1(student_scores['Harry']))
# print(f"ron got", rank1(student_scores['Ron']))
#
# Excercise 3:
# ======================================================================

nam_bid = {
    'name': 0
}

def add_options():
    nam=""
    bids=0
    nam=str(input("enter your name:"))
    bids=int(input("enter your value:"))
    nam_bid[nam]=bids
    print(nam_bid)
    print(len(nam_bid))
    check_again()

def compare_bid():
    defa =[]
    maxm=0
    winner=""
    for i in nam_bid:
        # print(nam_bid[i])
        if maxm < nam_bid[i]:
            maxm=nam_bid[i]
            winner=i
    print("this is maxm",maxm,"by",winner)


def check_again():
    last_yes=input("Are you the last user?")
    if (last_yes)=="No":
        add_options()
    else:
        print("Thanks")
        compare_bid()



add_options()
# check_again()
