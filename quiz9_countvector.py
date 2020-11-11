from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# list of text documents
text = ["breakthrough drug for schizophrenia",
        "new schizophrenia drug",
        "new approach for treatment of schizophrenia",
        "new hopes for schizophrenia patients","schizophrenia patient"]

q1=["schizophrenia patient"]

# create the transform
vectorizer = CountVectorizer()

vectorizer_q1 = CountVectorizer()


# tokenize and build vocab
vectorizer.fit(text)

vectorizer_q1.fit(q1)

# summarize
print(vectorizer.vocabulary_)

# encode document
vector = vectorizer.transform(text)
vector_q1 = vectorizer.transform(q1)

# summarize encoded vector
print(vector.toarray())

print(vector_q1.toarray())

# creating separate vectors
v1 = vector[0].toarray()
v2 = vector[4].toarray()

q1=vector_q1[0].toarray()

# calculate cosine similarity
similarity = cosine_similarity(v1, v2)

print(similarity)

