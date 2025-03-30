word = input("Enter a word: ")
print("First 3 characters:", word[:3])
print("Last 3 characters:", word[-3:])
if word.lower().startswith("py"):
    print("The word starts with 'Py'")
else:
    print("The word does not start with 'Py'")