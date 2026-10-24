grade = float(input("Grade/20: "))
if grade <0 or grade >20:
    print("Invalid grade")
elif grade >= 16:
    print("Very Good!")
elif grade >= 14:
    print("Good!")
elif grade >= 12:
    print("Fairly Good!")
elif grade >= 10:
    print("Pass.")
else:
    print("Fail.")