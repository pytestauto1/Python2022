#Write a function that finds the sum of the first n natural numbers. Make your function recursive.
#sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15################################

def sum_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_numbers(n-1)




print(sum_numbers(5))    
