
num1 = 0
ans=""
user_year=int(input("Enter your year: "))
print  (user_year)
def findleap():
    """Tells if a year is leap or not"""
    if user_year%100==0:
        if user_year%400==0:
            return "Leap Year with 100"
        else:
            return "Not leap year"

    if user_year%4==0:
        return "Leap Year with 4"
    else:
        return "Not leap year"

ans=findleap()
print(ans)