import nltk
from nltk.corpus import gutenberg
from pprint import pprint

alice = gutenberg.raw(fileids='carroll-alice.txt')
sample_text = 'We will discuss briefly about the basic syntax, structure and design philosophies. ' \
              'There is a defined hierarchical syntax for Python code which you should remember when writing code! ' \
              'Python is a really powerful programming langauge!'

# TOTAL CHARACTERS IN aLICE IN wONDERLAND:
print(len(alice))

# Sentence tokenization:
default_st = nltk.sent_tokenize

# Determin sentence structures in text:
alice_sentences = default_st(text=alice)
sample_sentences = default_st(text=sample_text)

print('Number of sentences in Alice Text: ' + str(len(alice_sentences)))
print('Number of sentences in sample text: ' + str(len(sample_sentences)))

pprint(sample_sentences)

print('First 5 sentences of alice: ')
pprint(alice_sentences[0:5])