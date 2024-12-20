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

# def check_voting_eligibility(input):
#     # Your control flow logic goes here
#     try:
#         age = int(input)
#         voting_age = 18
#         if age < 1:
#             print("Error, please enter a valid age.")
#         elif age < voting_age:
#             print("You can't vote.")
#         elif age >= voting_age:
#             print("You can vote!")
#     except ValueError:
#         print("Please enter a number.")

# # Call the function
# check_voting_eligibility(input("Please enter your age: "))

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years(input):
#     # Your control flow logic goes here
#     try:
#         age = int(input)
#         if age > 2:
#             first_two = age - 2
#             final_age = first_two * 7 + 20
#             print(f"The dog's age in dog years is {final_age}.")
#         elif age == 1:
#             print("The dog's age in dog years is 10.")
#         elif age == 2:
#             print("The dog's age in dog years is 20.")
#         elif age <= 0:
#             print("Please input a valid dog age.")
#     except ValueError:
#         print("Please input a valid dog age.")

# # Call the function
# calculate_dog_years(input("Input a dog's age: "))

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice(cold, rain):
#     # Your control flow logic goes here
#     try:
#         if cold.lower() == "yes" and rain.lower() == "yes":
#             print("Wear a waterproof coat.")
#         elif cold.lower() == "no" and rain.lower() == "yes":
#             print("Carry an umbrella.")
#         elif cold.lower() == "yes" and rain.lower() == "no":
#             print("Wear a warm coat.")
#         elif cold.lower() == "no" and rain.lower() == "no":
#             print("Wear light clothing.")
#         else:
#             print("Please answer with yes or no.")
#     except ValueError:
#         print("Please answer with yes or no.")

# # Call the function
# weather_advice(input("Is it cold? (yes/no): "), input("Is it raining? (yes/no): "))

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season(month, day):
    # Your control flow logic goes here
    try:
        lc_month = month.lower()
        int_day = int(day)
        if int_day > 31:
            print("Please enter a valid month and day.")
        elif lc_month == "jan" or lc_month == "feb" and int_day < 29 or lc_month == "dec" and int_day > 20 or lc_month == "mar" and int_day < 20:
            print(f"{month} {day} is in winter.")
        elif lc_month == "apr" or lc_month == "may" or lc_month == "mar" and int_day > 19 or lc_month == "jun" and int_day < 21:
            print(f"{month} {day} is in spring.")
        elif lc_month == "jul" or lc_month == "aug" or lc_month == "jun" and int_day > 20 and int_day < 31 or lc_month == "sep" and int_day < 22:
            print(f"{month} {day} is in summer.")
        elif lc_month == "oct" or lc_month == "nov" or lc_month == "sep" and int_day > 21 and int_day < 31 or lc_month == "dec" and int_day < 21:
            print(f"{month} {day} is in fall.")
        else:
            print("Please enter a valid month and day.")
    except ValueError:
        print("Please enter a valid month and day.")

# Call the function
determine_season(input("Enter the month of the year (Jan - Dec): "), input("Enter the day of the month: "))