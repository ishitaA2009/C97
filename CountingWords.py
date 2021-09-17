introstr = input("Enter String: ")
characterCount = 0
wordCount = 1

for i in introstr:
    characterCount = characterCount+1
    if(i == " "):
        wordCount = wordCount+1


print("no. of words in the string: ")
print(wordCount)
print("Number of characters in the string: ")
print(characterCount)
