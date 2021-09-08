# lambda function / sometimes called lambda expression

# Syntax:
# lambda arguments : expression 


f = lambda a: a*a  # we assign the lambda expression to a variable

num = int(input("Give a number: "))
num_sqr = f(num) # evaluate the lambda expression

print(f"The square of {num} is {num_sqr}")