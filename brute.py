"""
    the idea for this is to eventually
    run the raspberry pi for a few
    days to collect potential passwords
    in lexicographical order.
"""
from string import ascii_lowercase
from datetime import *
def main():
    password = input("password to guess: ")
    p = ""
    now = datetime.utcnow()
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    for e in ascii_lowercase:
                        print(str(a+b+c+d+e) + '\n')
                        if (tryPass(a,b,c,d,e,password)): 
                            print("the password is: " +  str(a+b+c+d+e)+ '\n')
                            later = datetime.utcnow()
                            time = later - now
                            print("found in: " + str(time.total_seconds()) + " seconds.")
                            return 0 

def tryPass(a,b,c,d,e,p):
    if(str(a+b+c+d+e) == p):
        ans = True
    else:
        ans = False
    return ans

main()
