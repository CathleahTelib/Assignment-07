sentence = input("Enter any sentence you want:")
string= sentence.lower()
vowels = 0
consonants = 0
words = 1

for i in range(len(string)):
    if(sentence[i] == ' ' or sentence == '\n' or sentence == '\t'):
        words = words + 1
for c in string:
    if c in 'aeiou':
        vowels= vowels+1
    else:
        if c in 'bcdfghjklmnpqrstvwxyz':
            consonants = consonants+1
    
print('words:',words)
print('vowels:',vowels)
print('consonants:',consonants)
