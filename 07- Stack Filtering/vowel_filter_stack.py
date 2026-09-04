stack = []
words = ["sky", "apple", "try", "bow", "fly", "orange", "arjun", "edtvds"]

for word in words:
    if not any(vowel in word.lower() for vowel in "aeiou"):
        stack.append(word)

print("Stack with words without vowels:", stack)

while stack:
    print("Popped word:", stack.pop())

if not stack:
    print("Stack is now empty :)")
