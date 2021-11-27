lowerCase, upperCase, specialChar, digit = 0, 0, 0, 0
passCheck= input("Enter your password:")
if (len(passCheck) >= 15):
    for i in passCheck:
        for p in passCheck.split():
            if(p[0].isupper()):
                upperCase += 1
        if(i.islower()):
            lowerCase += 1
        if(i.isdigit()):
            digit += 1
        if(i == '!' or i == '_' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or
         i == '&' or i == '*' or i == '(' or i ==')' or i == '_' or i == '+' or i == '?' or i == '/'):
            specialChar += 1
else:
    print("The password did not meet the number of characters desired.")
if (lowerCase >= 1 and upperCase >= 1 and specialChar >= 1 and digit >= 1):
    print("Valid Password")
else:
    print("Invalid Password")