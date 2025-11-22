# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()




# Exercise 1: Vowel or Consonant
#
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

def check_letter():
   user_input = input("Enter a letter (a-z or A-Z): ") 
   letter = user_input.lower()
   vowels = "aeiou"

   if letter in vowels:
      print(f"The letter {user_input} is a vowel.")
   else:
      print(f"The letter {user_input} is a constant.")

# Call the function
check_letter()


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

def check_voting_eligibility():
 voting_age=21             
 age=input("Please enter your age:") 
 new_age=int(age)         

 if new_age>=voting_age:  
    print("you can vote")   # 
 else:                     
   print ("you cannot vote") 

check_voting_eligibility()   



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

def calculate_dog_years():
    age_input = input("Input a dog's age: ")
    dog_age = int(age_input)
    
    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        years_after_two = dog_age - 2
        dog_years = 20 + (years_after_two * 7)
    
    print(f"The dog's age in dog years is {dog_years}.")


# Call the function
calculate_dog_years()




def weather_advice():

    cold_input = input("Is it cold? (yes/no): ")
    is_cold = cold_input.lower() == "yes"
    rain_input = input("Is it raining? (yes/no): ")
    is_raining = rain_input.lower() == "yes"  
    if is_cold and is_raining:
        
        print("Wear a waterproof coat.")
    
    elif is_cold and not is_raining:
        
        print("Wear a warm coat.")

    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    else:
      
        print("Wear light clothing.")

# Call the function
weather_advice()



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

def determine_season():
    month_input = input("Enter the month of the year (Jan - Dec): ")
    month = month_input.title()
    day_input = input("Enter the day of the month: ")
    day = int(day_input)

    if day < 1 or day > 31:
        print("Invalid day. Please enter a day between 1 and 31.")

    winter = ["Dec", "Jan", "Feb"]
    spring = ["Mar", "Apr", "May"]
    summer = ["Jun", "Jul", "Aug"]
    fall= ["Sep", "Oct", "Nov"]

    if month in winter:
        if month == "Dec" and day >= 21:
            season = "Winter"
        elif month == "Jan" or month == "Feb":
            season = "Winter"
        elif month == "Mar" and day <= 19:
            season = "Winter"
       

    elif month in spring:
        if month == "Mar" and day >= 20:
            season = "Spring"
        elif month == "Apr" or month == "May":
            season = "Spring"
        elif month == "Jun" and day <= 20:
            season = "Spring"
        else:
            season = None
    

    elif month in summer:
        if month == "Jun" and day >= 21:
            season = "Summer"
        elif month == "Jul" or month == "Aug":
            season = "Summer"
        elif month == "Sep" and day <= 21:
            season = "Summer"
        else:
            season = None

    elif month in fall:
        if month == "Sep" and day >= 22:
            season = "Fall"
        elif month == "Oct" or month == "Nov":

            season = "Fall"
        elif month == "Dec" and day <= 20:
            season = "Fall"
        else:
            season = None

    else:
        print(f"Invalid month: {month}")
        return
    if season:
        print(f"{month} {day:2d} is in {season}.")

    else:
        print("Unable to determine season for this date.")


# Call the function
determine_season()
