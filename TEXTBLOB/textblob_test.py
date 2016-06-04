from textblob import TextBlob
from textblob import Word

wiki = TextBlob("Python is a high-level, general-purpose programming language.")
print("Python is a high-level, general-purpose programming language.")
#Speech tagging
print("Speech Tags : ")
a = wiki.tags #a list is returned
for x in a:
    print(x)

#noun_phrases extraction
print("Noun Phrases : ")
for x in wiki.noun_phrases:
    print(x)
print()

#sentiment analysis
testimonial = TextBlob("Textblob is amazingly simple to use. What great fun!")
print("Textblob is amazingly simple to use. What great fun!")
a = testimonial.sentiment
print(a) #returns polarity[-1(for worst) to 1(for best)] and subjectivity
print()

#word inflection
sentence = TextBlob('Use 4 spaces per indentation level.')
print(sentence.words[2].singularize()) #similarly you can use pluralize
print()

#word lemmatization
w = Word("octopi")
print("octopi -> ",w.lemmatize())
w = Word("went")
print("went -> ",w.lemmatize("v"))
print()

#definition
print("Octopus : ",Word("octopus").definitions)
print()

#translation and language detection
en_blob = TextBlob(u'Simple is better than complex.')
print('Simple is better than complex.')
print("SPANISH : ",en_blob.translate(to='es'))
en_blob = TextBlob(u'Comment allez vous?')
print('Comment allez vous?')
print("language : ",en_blob.detect_language())
print()

#spell-check
w = Word("banama")
print("banama")
print("correction : ",w.correct())
print("suggestions : ",w.spellcheck())
print()
