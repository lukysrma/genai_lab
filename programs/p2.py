
import gensim.downloader as api
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model = api.load("word2vec-google-news-300")


words = ['computer', 'internet', 'software', 'hardware', 'keyboard', 'mouse', 'server', 'network', 'programming', 'database']
vectors = [model[word] for word in words]


pca = PCA(n_components=2)
reduced = pca.fit_transform(vectors)


input_word = 'computer'
similar_words = model.most_similar(input_word, topn=5)


print(f"Top 5 words similar to '{input_word}':")
for word, score in similar_words:
    print(f"{word}: {score:.4f}")


plt.figure(figsize=(8, 6))
for i, word in enumerate(words):
    plt.scatter(reduced[i, 0], reduced[i, 1])
    plt.annotate(word, (reduced[i, 0], reduced[i, 1]))
plt.title("PCA Visualization of Technology Word Embeddings")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(True)


plt.show()
