str = input("Enter string")

words = str.split()

for word in words:
    print(word, "=", len(word))