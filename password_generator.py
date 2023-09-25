import random
import string

def generatePassword(passwordLength, hasUppercase, hasLowercase, hasNumbers, hasSpecialChars):
    hasUppercaseCondition = True
    hasLowercaseCondition = True
    hasNumbersCondition = True
    hasSpecialCharsCondition = True
    
    password = ""
    charactersBank = ""
    if hasUppercase:
        charactersBank += string.ascii_uppercase
        hasUppercaseCondition = False
    if hasLowercase:
        charactersBank += string.ascii_lowercase
        hasLowercaseCondition = False
    if hasNumbers:
        charactersBank += string.digits
        hasNumbersCondition = False
    if hasSpecialChars:
        charactersBank += string.punctuation
        hasSpecialCharsCondition = False

    if passwordLength < 8:
        passwordLength = 8
    
    while not (hasSpecialCharsCondition and hasNumbersCondition and hasLowercaseCondition and hasUppercaseCondition):
        password = ""
        for i in range(passwordLength):
            password += (random.choice(charactersBank))
        
        for char in password:
            if hasUppercase and char.isupper() and hasUppercaseCondition == False:
                hasUppercaseCondition = True
            if hasLowercase and char.islower() and hasLowercaseCondition == False:
                hasLowercaseCondition = True
            if hasNumbers and char.isdigit() and hasNumbersCondition == False:
                hasNumbersCondition = True
            if hasSpecialChars and (char in string.punctuation) and hasSpecialCharsCondition == False:
                hasSpecialCharsCondition = True 

    return password


if __name__ == "__main__":
    print("*** Password Generator ***")
    choice = input("To generate a password type '1', to customize password parameters press ENTER: ")
    if choice == '1':
        print("*** Generating Password... ***")
        print("Password: ", generatePassword(25, True, True, True, True))
    else:
        passwordLength = input("How long should the password be? (minimum length is 8 characters): ")
        hasUppercase = input("Should the password have uppercase letters? (yes/no): ").lower() == "yes"
        hasLowercase = input("Should the password have lowercase letters? (yes/no): ").lower() == "yes"
        hasNumbers = input("Should the password have numbers? (yes/no): ").lower() == "yes"
        hasSpecialChars = input("Should the password have special characters? (yes/no): ").lower() == "yes"
        print("*** Generating Password... ***")
        print("Password: ", generatePassword(int(passwordLength), hasUppercase, hasLowercase, hasNumbers, hasSpecialChars))
