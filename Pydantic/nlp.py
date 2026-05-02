import nltk 
nltk.download('punkt')

from nltk import word_tokenize, sent_tokenize

corpus = "Hello there. How are you doing today? This is a sample text for tokenization."

print("Word Tokenization:", word_tokenize(corpus))