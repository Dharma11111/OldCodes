import nltk
from nltk.tokenize import sent_tokenize

i=0
while i < 1:
    
    sentences = input()

    number_of_sentences = sent_tokenize(sentences)

    print(len(number_of_sentences))
