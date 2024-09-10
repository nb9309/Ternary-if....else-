word = input('enter value: ')
if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
    res = 'vowel word'
else:
    res = 'not a vowel word'

print('{} is a {}'.format(word,res))