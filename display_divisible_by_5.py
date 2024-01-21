# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only 
# those numbers which are divisible by 5

# Pseudocode
# assign variable for list
# for loop the list
# if-else statement
#   if num%, print list

number_list = [10, 20, 33, 46, 55]
print("Given list:", number_list)
print('Divisible by 5:')
for number in number_list:
    if number % 5 == 0:
        print(number)