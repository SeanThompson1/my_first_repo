#Should have been Read.me

#Input Username
userName = input("Hi Whats your name? ")
passwordAttempt = input("Please enter your password. ")

#Correct password
password = "password"

if passwordAttempt == password:
    print("Hi " + userName)
    input("What " + "is " + "your " + "age? ")
   
    number_one = input("Try entering a number. ")
    number_two = input("Enter another number. ")
    number_one = int(number_one)
    number_two = int(number_two)

    total = number_one + number_two

    print("The sum of these 2 numbers is: " + str(total))

    if total == 69 or 420:
        while True:
            print("Nice Meme")

#Incorrect Password      
elif passwordAttempt != password:
    print("Please try that again. ")
