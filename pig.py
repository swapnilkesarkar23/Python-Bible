# if starts with vowel, just add "yay"
# otherwise, move the first consonant cluster to end, and add "yay"

# get sentence from user
orignal = input("Please enter a sentence: ").strip().lower()

# split sentence into words
words = orignal.split()

# loop through words and convert to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "yay"
        new_words.append(new_word)

# stick words back together
output = " ".join(new_words)

# output the final string
print(output)
