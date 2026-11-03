full = input("Enter your full name: ")
initials = ''
for word in full.split():
    initials += word[0].upper()+'.'
print("Your initials are:", initials)