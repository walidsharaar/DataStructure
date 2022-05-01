# function declaration for order of N
def get_squared_numbers(numbers):
    squared_numbers=[]
    for n in numbers:
        squared_numbers.append(n*n)
    return squared_numbers

numbers=[2,5,4,7,8]


# call the function
# returns [4,25,16,49,64]
print(get_squared_numbers(numbers))
