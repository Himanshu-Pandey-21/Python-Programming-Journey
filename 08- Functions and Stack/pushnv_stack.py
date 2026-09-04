def PushNV(N):
    NoVowel = []
    vowels = "aeiouAEIOU"

    for word in N:
        if not any(ch in vowels for ch in word):
            NoVowel.append(word)

    return NoVowel


All = []
for i in range(5):
    word = input("Enter word: ")
    All.append(word)

print("All words:", All)

NoVowel = PushNV(All)
print("Pushed stack (No-Vowel words):", NoVowel)

while len(NoVowel) > 0:
    print("Popped word:", NoVowel.pop())

print("Empty Stack")
