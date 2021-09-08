# lambda function / sometimes called lambda expression

# Syntax:
# lambda arguments : expression 


# problem statement: Form a given list we will reduce the numbers by using lambda
# and reduce function

from functools import reduce
num_list = [1, 4, 7, 2, 5, 90, 12, 54, 23, 87, 30]

num =  reduce(lambda a,b: a+b, num_list)
print(num)


# The above code can be rewritten without using lambda

def update(a,b):
    return a+b
    

num = reduce(update, num_list)
print(num)

# Comment:
# From the above two style of coding we see that both gives the same result
# But using lambda is much more concise and elegent and cleaner style of coding

# num_list = [1, 4, 7, 2, 5, 90, 12, 54, 23, 87, 30]
# num = 1+4 = 5 + 7 = 12 + 2 = 14 + 4 = 19 + 90 = 109 + 12 = 121 + 54 = 175 + 23 = 198 + 87 = 285+30 = 315
