#Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.
""" Return a boolean value (True or False).
Return True if the amount of x's and o's are the same.
Return False if they aren't the same amount.
The string can contain any character.
When "x" and "o" are not in the string, return True. """

def XO(txt):
    x = txt.count('x')
    o = txt.count('o')
    if x == o:
        return True
    else:
        if x & o ==0:
            return True
        else:
            return False


print (XO("xooxx"))