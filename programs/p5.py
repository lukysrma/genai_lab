import gensim.downloader as api  
from gensim.models import KeyedVectors 
import random  

model = api.load("glove-wiki-gigaword-100")

def generate_similar_words(seed_word, topn=10):
    if seed_word in model:
       
        return [word for word, _ in model.most_similar(seed_word, topn=topn)]
    else:
        
        return []
def create_paragraph(seed_word):
    similar_words = generate_similar_words(seed_word, topn=10)
    if not similar_words:
        return f"No similar words found for '{seed_word}'."

    random.shuffle(similar_words)

    paragraph = f"In a world defined by {seed_word}, "
    paragraph += f"people found themselves surrounded by concepts like {', '.join(selected_words[:-1])}, and {selected_words[-1]}. "
    paragraph += f"These ideas shaped the way they thought, acted, and dreamed. Every step forward in their journey reflected the essence of '{seed_word}', "
    paragraph += f"bringing them closer to understanding the true meaning of {selected_words[0]}."

    return paragraph

seed = "freedom"  
print(create_paragraph(seed))
