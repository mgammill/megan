meg_fav_foods = ["pasta", "burrito", "chocolate", "bread", "banana"]
# print(meg_fav_foods[1])

# I encountered this error code: "NameError: name 'pasta' is not defined"
# The entries in my list originally did not have quotations around them.
# To fix this error, I went back to add quotations around each item.

# print(meg_fav_foods[-1])
meg_fav_foods.append("cheeseburger")
# print(meg_fav_foods)
meg_fav_foods.insert(0, "apple")
# print(meg_fav_foods)
del(meg_fav_foods[2])
# print(meg_fav_foods)
# print(len(meg_fav_foods))
for food in meg_fav_foods:
    print(food.upper())
new_list = []
new_list.append(meg_fav_foods[::5])
# print(new_list)
if "potato" in meg_fav_foods:
    print("A potato!")
else: 
    print("No potato!")
numbers = []
for i in range(0,21):
    numbers.append(i)
def get_first_15(numbers):
    return(numbers[:16])
step1 = get_first_15(numbers)
# I encountered this error code for line 28: 
# "SyntaxError: invalid syntax"
# In line 28, I didn't specify which list I wanted to print entries of
# I wrote: return(:16) rather than return(numbers[:16])
def get_every_5th(step1):
    return(step1[::5])
step2 = get_every_5th(step1)
def reverse_and_stride(step2):
    working_list = step2[::-1]
    return(working_list[2::3]) # Start on entry "2" (3rd entry) so that we get every third entry
step3 = reverse_and_stride(step2)

# I encountered this error: "NameError: name 'reverse_and_stride' is not defined
# did you mean: 'reverse_and_string'?
# In my function on line 37, I had a typo in the name of my function.
# I have fixed this my editing the function to be named "reverse_and_stride"

# I encountered another error: "TypeError: 'function' object is not subscriptale"
# I realized that on line 38, "get_every_5th" is not the full name of my function,
# To fix the error I need to add "()" to the end of this name.
# I have since edited this to be "setp2" rather than "get_every_5th(step1)"

# print(numbers)
# print(step1)
# print(step2)
# print(step3)

numbers1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(numbers[2]) # This prints the thrid row
# print(numbers[1][1]) # This prints the second item in the second row
numbers1.append([10,11,12])
# print(numbers)
def sum_nested(list):
    sum = 0
    for sublist in list:
        for i in range(len(sublist)):
            sum += (sublist[i])
    return(sum)
# print(sum_nested(numbers1))

# I enountered this error message: "TypeErroe: sum_nested() takes 0 positional
# aruments but 1 was given"
# When writing the name of my function, I should hae indicated that it
# inputs argument: list ("numbers") rather than leaving it blank with "()"
# To fix this, I changed the function name to: "sum_nested(list)"
#
# I encountered another error for line 67: "TypeError: 'list' object cannot be 
# interpreted as an integer"
# I wrote "range(sublist)" where I should have written "range(len(sulist))"
# This error has been resolved by making the above edit

def make_nxn(n):
    nested = []
    bank = []
    for i in range(n*n):
        bank.append(i+1)
    for i in range(n):
        nested.append(bank[i*5:(i+1)*5])
    return(nested)
nested5x5 = make_nxn(5)
# print(nested5x5)
def multiples_of_3(list):
    for sublist in list:
        for i in sublist:
            if (i % 3) == 0:
                index = sublist.index(i)
                del(sublist[index])
                sublist.insert(index, "?")
    return(list)
nested5x5mod3 = multiples_of_3(nested5x5)
# print(nested5x5mod3)
# I encountered this error: "SyntaxError: invalid synax" for line 95.
# On line 95, I wanted index to hold the index for sublist item i 
# I originally had index = enumerate(i).
# The correct way to find the index is to use the command list.index("item")
# To resolve the error, I edited my code to use the correct indexing command.
def sum_rest(list):
    sum = 0
    for sublist in list:
        for i in sublist:
            if i != "?":
                sum += i
    return(sum)
sum = sum_rest(nested5x5mod3)
# print(sum)
ages = {
    "Katie": 30,
    "Miriam": 42,
    "Safia": 25,
    "Mira": 48
}
# print(ages["Katie"])
ages["Mira"] = 100
# print(ages)
ages["Milana"] = 52
# print(ages)
del(ages["Milana"])
# print(ages)
for key in ages:
    print(f"{key} is {ages[key]} years old")

list5x5mod3 = multiples_of_3(make_nxn(5))
# This runs functions from 3.4.1 to make a 5x5 list
# with number 1 through 25, replacing all multiples of 3
# with a question mark "?"
print(list5x5mod3)