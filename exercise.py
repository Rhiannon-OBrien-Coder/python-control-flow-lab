# Exercise 1: Vowel or Consonant
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter(input):
#     # Your control flow logic goes here
#     lowercase = input.lower()
#     uppercase = input.upper()
#     if lowercase != uppercase:
#         input_is_vowel = lowercase in "a, e, i, o, u"
#         if len(input) > 1:
#             print("Please enter a single letter.")
#         elif input_is_vowel == True:
#             print(f'The letter {input} is a vowel.')
#         elif input_is_vowel == False:
#             print(f'The letter {input} is a consonant.')
#     else:
#         print("Invalid entry, try a letter.")

    

# Call the function
# check_letter(input(""))

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility(input):
    # Your control flow logic goes here
    try:
        age = int(input)
        voting_age = 18
        if age < 1:
            print("Error, please enter a valid age.")
        elif age < voting_age:
            print("You can't vote.")
        elif age >= voting_age:
            print("You can vote!")
    except ValueError:
        print("Please enter a number.")

# Call the function
check_voting_eligibility(input("Please enter your age: "))

# Exercise 3

# Exercise 4

# Exercise 5