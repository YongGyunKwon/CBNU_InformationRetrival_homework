from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity


query=[1,1]
doc1=[1,0]
doc2=[1,0]
doc3=[1,0]
doc4=[1,1]

result1=cosine_similarity([query],[doc1])
result2=cosine_similarity([query],[doc2])
result3=cosine_similarity([query],[doc3])
result4=cosine_similarity([query],[doc4])

print(result1)
print(result2)
print(result3)
print(result4)