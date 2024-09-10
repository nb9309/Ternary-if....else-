#Program for accepting a Word and Decidide whether It is Vowel Or Not
#TernaryOpEx5.py
word=input("Enter any Word:")
res="Vowel Word" if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word else "Not Vowel Word"
print("{} is {}".format(word,res))