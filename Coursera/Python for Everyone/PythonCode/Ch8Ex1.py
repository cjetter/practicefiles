'''Ch8Ex1: Write a function called chop that takes a list and modifies it, removing the first
and last elements, and returns None.

Then write a function called middle that takes a list and returns a new list 
that contains all but the first and last elements.
'''

def chop(t):
    x = len(t)-1
    del t[x]
    del t [0]
    print(t)
    ##How do you get it to return None?? The idea is that we are trying to show no new list was created but why complicate things?

def middle(t):
    x = len(t)-1
    t2 = t[1:x]
    print(t)
    print(t2)


test1 = '12321'
test = list(test1)
#chop(test)
middle(test)