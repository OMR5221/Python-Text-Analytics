from nltk.corpus import brown
print('Total Categories: ', len(brown.categories()))

print(brown.categories())

# tokenized sentences
print(brown.sents(categories='mystery'))

# parts of sentence tagged sentences:
print(brown.tagged_sents(categories='mystery'))

# Get sentences in natural form:
sentences = brown.sents(categories='mystery')

print(sentences)

sentences = [' '.join(sentence_token) for sentence_token in sentences]

print(sentences[0:5])