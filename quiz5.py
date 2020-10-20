from nltk.tokenize import sent_tokenize,word_tokenize

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#task2
example_sent="I am studying Information Retrieval course at my university."
print("sent tokenization")
print(sent_tokenize(example_sent))
print("word tokenization")
print(word_tokenize(example_sent))

stop_words=set(stopwords.words('english'))

word_tokens=word_tokenize(example_sent)

word_tokens=[w for w in word_tokens if not w in stop_words]

print(word_tokens)

filtered_sentence=[]

for w in word_tokens:
    filtered_sentence.append(w)

print(filtered_sentence)

ps=PorterStemmer()

for a in filtered_sentence:
    print(a,":",ps.stem(a))