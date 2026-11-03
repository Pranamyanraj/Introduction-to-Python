sentence = input("Enter a sentence: ")
words = sentence.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print("The number of words in the sentence is:", len(words))
print("The longest word is:", longest)