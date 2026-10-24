word = input("Word: ")
count = 0
for letter in word:
    if letter in "aeiou":
        count += 1
        print(f"{count} vowels")
