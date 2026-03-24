
import gensim.downloader as api  
from scipy.spatial.distance import cosine  


print("Loading Word2Vec model...")
model = api.load("word2vec-google-news-300")
print("Model loaded successfully.\n")


vector = model['king']
print("First 10 dimensions of 'king' vector:")
print(vector[:10], "\n")


print("Top 10 words most similar to 'king':")
for word, similarity in model.most_similar('king'):
    print(f"{word}: {similarity:.4f}")
print()


result = model.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print("Analogy - 'king' - 'man' + 'woman' ≈ ?")
print(f"Result: {result[0][0]} (Similarity: {result[0][1]:.4f})\n")


print("Analogy - 'paris' + 'italy' - 'france' ≈ ?")
for word, similarity in model.most_similar(positive=['paris', 'italy'], negative=['france']):
    print(f"{word}: {similarity:.4f}")
print()


print("Analogy - 'walking' + 'swimming' - 'walk' ≈ ?")
for word, similarity in model.most_similar(positive=['walking', 'swimming'], negative=['walk']):
    print(f"{word}: {similarity:.4f}")
print()


similarity = 1 - cosine(model['king'], model['queen'])
print(f"Cosine similarity between 'king' and 'queen': {similarity:.4f}")
