# lambda function / sometimes called lambda expression

# Syntax:
# lambda arguments : expression 


# problem statement: Form a given list we will double the numbers by using lambda
# and map function
num_list = [1, 4, 7, 2, 5, 90, 12, 54, 23, 87, 30]

num_double = list(map(lambda a: a*2, num_list))
print(num_double)


# The above code can be rewritten without using lambda

def update(n):
    return 2*n
    

num = list(map(update, num_list))
print(num)

# Comment:
# From the above two style of coding we see that both gives the same result
# But using lambda is much more concise and elegent and cleaner style of coding