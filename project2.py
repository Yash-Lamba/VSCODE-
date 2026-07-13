# a random password generator
# improrts needed 
import random
import string

# user perferecnces
# length of the password decided by the user: must be atleast 6
# does the user want to include special characters, numbers, and uppercase letters
def password_generator():
    print("Generate a password stronge enough to keep your accounts safe!")
    # user inputs
    while True:
        try:
            length = int(input("Enter the desired length of your password (minimum 6 characters/maximum 12 characters): "))
            if length < 6:
                print("Password length must be at least 6 characters. Please try again.")
                continue
            elif length > 12:
                print("password length must not be more than 12 characters. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() 
    numbers = input("Include numbers? (yes/no): ").strip().lower()
    special_characters = input("Include special characters? (yes/no): ").strip().lower() 

    # create a pool of characters based on user preferences
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if uppercase == "yes" else ""
    numbers = string.digits if numbers == "yes" else ""
    special_characters = string.punctuation if special_characters == "yes" else ""
    character_pool = lowercase + uppercase + numbers + special_characters 

    # selecting random characters from the pool to generate the password
    selected_characters = random.sample(character_pool,length)
    
    #generating the final password by joining the selected characters
    final_password = ''.join(selected_characters)
    print("Your generated password is: ", final_password)
    
password_generator()


