# Write a program that accepts a sentence as input, reverses each word, and then reverses the entire sentence.
sentence=input("Enter the sentence")
for word in sentence.split():
    word=word[:-1]

reversed_sentence = sentence[::-1]
print(reversed_sentence)    
