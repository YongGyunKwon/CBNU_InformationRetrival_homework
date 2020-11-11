from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# list of text documents
text = ["breakthrough drug for schizophrenia",
        "new schizophrenia drug",
        "new approach for treatment of schizophrenia",
        "new hopes for schizophrenia patients","schizophrenia drug","schizophrenia patient"]

# create the transform (Note: that values are normalized from 0 to 1)
vectorizer = TfidfVectorizer()

# tokenize and build vocab
vectorizer.fit(text)



# encode document
vector = vectorizer.transform(text)


# summarize encoded vector
print(vector.toarray())

# creating separate vectors
d1 = vector[0].toarray()
d2 = vector[1].toarray()
d3 = vector[2].toarray()
d4 = vector[3].toarray()

q1 = vector[4].toarray()
q2 = vector[5].toarray()

# calculate cosine similarity
similarity_d1q1 = cosine_similarity(d1, q1)
similarity_d2q1 = cosine_similarity(d1, q1)
similarity_d3q1 = cosine_similarity(d3, q1)
similarity_d4q1 = cosine_similarity(d4, q1)


similarity_d1q2 = cosine_similarity(d1, q2)
similarity_d2q2 = cosine_similarity(d2, q2)
similarity_d3q2 = cosine_similarity(d3, q2)
similarity_d4q2 = cosine_similarity(d4, q2)


print(similarity_d1q1)
print(similarity_d2q1)
print(similarity_d3q1)
print(similarity_d4q1)

print("----------------------")

print(similarity_d1q2)
print(similarity_d2q2)
print(similarity_d3q2)
print(similarity_d4q2)
