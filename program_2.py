# Program #2: Larger than n
# In a program, write a function (with NO output) that accepts two arguments: number n, and a list.
# Assume that the list contains numbers.
# The function shell has been written out on line 30, (def display_larger_than_n_list)
# and should display all of the numbers in the list that are greater than then number n.

def main():
    # Declare local variables
    number = 5
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Display the number.
    print('Number:', number)

    # Display the list of numbers.
    print('List of numbers:')
    print(f'{number_list}')
    
    # Display the list of numbers that are larger
    # than the number.
    print(f'List of numbers that are larger than {number}:')
    
    # Call the display_larger_than_n_list function,
    # passing a number and number list as arguments.
    display_larger_than_n_list(number, number_list)

# The display_larger_than_n_list function accepts two arguments:
# a list, and a number. The function displays all the numbers
# in the list that are greater than the number.
def display_larger_than_n_list(n, n_list):
    list1 = list(n_list)
    larger_than_n_list = []
    for number in list1:
        if number <= n:
            continue
        elif number > n:
            larger_than_n_list.append(number)
    print(larger_than_n_list)

        
# Call the main function.
main()

#This program was written on 10/17/25 by Logan Gibson
#Its name is "Greater Than Some Number"