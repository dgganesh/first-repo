val=""
def check_prime(nom):
    prim = 0
    for i in range (1,nom-1):
        #print(i)
        if nom%i==0:
            prim=prim+1

    if prim>1:
      print("Not a prime number")
    else:
        print("Prime number")


print("ENTer the number less than 50 to check for prime")
eng=int(input())
check_prime(eng)
