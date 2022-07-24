# Ask user for name
name = input("Hello there, What is your name?: ").strip().capitalize()

print("Hello {}, I'm James Darko. I want us to play a game. You give me a sentence, then I turn it into jibberish. I hope this is fun.".format(name))

# Get sentence from users
original = input("Let's start {}, kindly give me any sentence of your choice.: ".format(name)).strip().capitalize()

# split sentence into words
words = original.split()
print(words)

# loop through words and convert into Pig latin

new_words = []

# If it starts with a vowel, simply add "ay"

for word in words:
        if word[0]in "aeiou":
          new_word = word + "yay"
          new_words.append(new_word)
        else:
          vowel_pos = 0
          for letter in word:
             if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
             else:
                break

# If it starts with a consonant or consonant cluster, move the consonant to the end 
          cons = word[:vowel_pos]
          the_rest = word[vowel_pos:]
          new_word = the_rest + cons + "ay"
          new_words.append(new_word)  
          
print(new_words)

# stick words back together
output = " ".join(new_words)

# output the final string
print(output)

print("{}, is this not fun? Have a blissful day.".format(name))
