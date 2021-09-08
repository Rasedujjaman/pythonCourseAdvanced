# lambda function / sometimes called lambda expression

# Syntax:
# lambda arguments : expression 


# problem statement: Form a given list we will filter out the even numbers by using lambda
# and filter function
num_list = [1, 4, 7, 2, 5, 90, 12, 54, 23, 87, 30]

num_even = list(filter(lambda a: a%2==0, num_list))
print(num_even)


# The above code can be rewritten without using lambda

def isEven(n):
    if(n%2 ==0):
        return n

num = list(filter(isEven, num_list))
print(num)

# Comment:
# From the above two style of coding we see that both gives the same result
# But using lambda is much more concise and elegent and cleaner style of coding