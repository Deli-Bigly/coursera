"""
Collatz Conjecture states that this function will always reach 1 at SOME number of iterations

The longest progression for any initial starting number

less than 10 is 9, which has 19 steps,
less than 100 is 97, which has 118 steps,
less than 1,000 is 871, which has 178 steps,
less than 10,000 is 6,171, which has 261 steps,
less than 100,000 is 77,031, which has 350 steps,
less than 1 million is 837,799, which has 524 steps,
less than 10 million is 8,400,511, which has 685 steps,
less than 100 million is 63,728,127, which has 949 steps,
less than 1 billion is 670,617,279, which has 986 steps,
less than 10 billion is 9,780,657,630, which has 1132 steps,[11][12] and
less than 100 billion is 75,128,138,247, which has 1228 steps.

"""


#Collatz_conjecture
def f(n):
        nMod = n%2
        if nMod == 0:
                n = (n//2)
        else:
                n = (n*3)+1
        return n

#starting value for Callatz_conjecture (n=9 takes 19 iterations to get to 1)
n = 9
#number of times to run the function
x = 19
while(x>0):
        n = f(n)
        x=x-1
        print (n)


