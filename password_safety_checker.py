from getpass import getpass

special_characters = ["!", "\" "" #", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\", ""]", "^", "_", "`", "{", "|", "}", "~", ]

print("This tool utilizes the annual Hive Systems Password Table \n This information provided should only be used as a guide and not as a means of ensuring security")
password = getpass("Please enter your password? ")
spec_Char = any(i in password for i in special_characters)

def main():
    if len(password) >= 19:
        print("This password is too long for the data utilized in this program!")
    elif password.isdigit() == True:
        digit()
    elif password.islower() == True:
        lowercase()
    elif password.isalpha() == True and password.islower() == False:
        bothcase()
    else:
        alphanum()

def digit():
    if len(password) <= 11:
        print("This password would be cracked instantly")
    if len(password) == 12:
        print("This password would be cracked in 1 second")
    if len(password) == 13:
        print("This password would be cracked in 5 seconds")
    if len(password) == 14:
        print("This password would be cracked in about 52 seconds")
    if len(password) == 15:
        print("This password would take about 9 minutes to crack")
    if len(password) == 16:
        print("This password would take about 1 hour to crack")
    if len(password) == 17:
        print("This password would take about 14 hours to crack")
    if len(password) == 18:
        print("This password would take about 6 days to crack")

def lowercase():
    if len(password) <= 8:
        print("This password would be cracked instantly")
    if len(password) == 9:
        print("This password would be cracked in about 3 seconds")
    if len(password) == 10:
        print("This password would be cracked in about 1 minute")
    if len(password) == 11:
        print("This password would take about 32 minutes to crack")
    if len(password) == 12: 
        print("This password would take about 14 hours to crack")
    if len(password) == 13:
        print("This password would take about 2 weeks to crack")
    if len(password) == 14:
        print("This password would take about 1 year to crack")
    if len(password) == 15:
        print("This password would take about 27 years to crack")
    if len(password) == 16:
        print("This password would take about 713 years to crack")
    if len(password) == 17:
        print("This password would take about 18k years to crack")
    if len(password) == 18:
        print("This password would take about 481k years to crack")

def bothcase():
    if len(password) <= 6:
        print("This password would be cracked instantly")
    if len(password) == 7:
        print("This password would be cracked in 1 second")
    if len(password) == 8:
        print("This password would be cracked in 28 seconds")
    if len(password) == 9:
        print("This password would be cracked in about 24 minutes")
    if len(password) == 10:
        print("This password would be cracked in about 21 hours")
    if len(password) == 11:
        print("This password would be cracked in about 1 month")
    if len(password) == 12:
        print("This password would take about 6 years to crack")
    if len(password) == 13:
        print("This password would take about 332 years to crack")
    if len(password) == 14:
        print("This password would take about 17k years to crack")
    if len(password) == 15:
        print("This password would take about 898k years to crack")
    if len(password) == 16:
        print("This passwo!@#$%^rd would take roughly 46 million years to crack")
    if len(password) == 17:
        print("This password would take roughly 2 billion years to crack")
    if len(password) == 18:
        print("Congratulations! This password would take roughly 126 billion years to crack!")

def alphanum():
    if spec_Char == True:
        if len(password) <= 6:
            print("This password would be cracked instantly")
        if len(password) == 7:
            print("This password would be cracked in about 4 seconds")
        if len(password) == 8:
            print("This password would be cracked in about 5 minutes")
        if len(password) == 9:
            print("This password would be cracked in about 6 hours")
        if len(password) == 10:
            print("This password would be cracked in about 2 weeks")
        if len(password) == 11:
            print("This password would take about 3 years to crack")
        if len(password) == 12:
            print("This password would take about 226 years to crack")
        if len(password) == 13:
            print("This password would take about 15k years to crack")
        if len(password) == 14:
            print("This password would take about 1 million years to crack")
        if len(password) == 15:
            print("This password would take about 77 million years to crack")
        if len(password) == 16:
            print("This password would take about 5 billion years to crack")
        if len(password) == 17:
            print("Congratulations! This password would take 380 billion years to crack!")
        if len(password) == 18:
            print("Congratulations! This password would take about 26 trillion years to crack!")
    else:
        if len(password) <= 6:
            print("This password would be cracked instantly!")
        if len(password) == 7:
            print("This password would be cracked in about 2 seconds")
        if len(password) == 8:
            print("This password would be cracked in about 2 minutes")
        if len(password) == 9:
            print("This password would be cracked in about 2 hours")
        if len(password) == 10:
            print("This password would be cracked in about 5 days")
        if len(password) == 11:
            print("This password would be cracked in about 10 months")
        if len(password) == 12:
            print("This password would take about 53 years to crack")
        if len(password) == 13:
            print("This password would take about 3k years to crack")
        if len(password) == 14:
            print("This password would take about 202k years to crack")
        if len(password) == 15:
            print("This password would take roughyl 12 million years to crack")
        if len(password) == 16:
            print("This password would take roughly 779 million years to crack")
        if len(password) == 17:
            print("Congratulations! This password would take roughly 48 billion years to crack!")
        if len(password) == 18:
            print("Congratulations! This password would take roughly 2 trillion years to crack!")
       
main()