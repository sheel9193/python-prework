# question 1
# Write a function to print "hello_USERNAME!" USERNAMEA is the input of the function. 

def hello_name(user_name):
    """Writing a function to print user_name"""
    for users in user_name:
        msg = "Hello, " + users + "!"
        print(msg)

names = ['sheel9193', 'codingtemple93']
hello_name(names)

# question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
   """A function that prints odds numbers and returns nothing"""
   x = 0
   while x < 100:
       x += 1
       if x % 2 == 1:
           print (x)
       else:
           continue
print(first_odds())

# question 3
# Please write a python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Return the max number in a given list"""
    max = 0
    for num in a_list:
        if num > max:
            max = num
    return max
print(max_num_in_list([1,2,3,4,5,6,7,8,9,0]))

# question 4
# Write a function to return if the given year is a leap year.

def is_leap_year(a_year):
    """To determine if a given year is a leap year"""

    if (a_year % 4 == 0 and a_year % 100 != 0):
       return True
    elif (a_year % 4 == 0 and a_year % 400 == 0):
       return True
    else:
       return False
        

print(is_leap_year(2016))
print(is_leap_year(2017))

# question 5
# Write a function to check to see if all numbers in a list are consecutive numbers

def is_consecutive(a_list):
    """To confirm if numbers in a list are in order"""

    range_list = list(range(min(a_list),max(a_list)+1))

    return sorted(a_list) == range_list

first_list = [20,21,22,23,24,25,26]
second_list = [4,3,6,8,2]

print(is_consecutive(first_list))
print(is_consecutive(second_list))