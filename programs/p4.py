from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import gensim.downloader as api

# Load embeddings
emb_model = api.load("glove-wiki-gigaword-100")
def get_similar_words(word, top_n=2):
    try:
        return [w[0] for w in emb_model.most_similar(word, topn=top_n)]
    except:
        return []
def enrich_prompt(prompt):
    words = prompt.split()
    enriched = []

    for word in words:
        enriched.extend(get_similar_words(word))

    return prompt + " " + " ".join(enriched)
  # Load FLAN-T5 model and tokenizer directly
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
# Prompts
original_prompt = "Explain benefits of exercise"
enriched_prompt = enrich_prompt(original_prompt)

# Generate
def generate_response(prompt, max_length=100):
    inputs = tokenizer(prompt, return_tensors="pt").input_ids
    outputs = model.generate(inputs, max_length=max_length)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

original_output = generate_response(original_prompt)
enriched_output = generate_response(enriched_prompt)

print("Original:", original_output)
print("\nEnriched:", enriched_output)
def detail_score(text):
    return len(text.split())

print("Original Detail:", detail_score(original_output))
print("Enriched Detail:", detail_score(enriched_output))


from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
def diversity_score(text):
    words = text.split()
    return len(set(words)) / len(words)

print("Original Diversity:", diversity_score(original_output))
print("Enriched Diversity:", diversity_score(enriched_output))
def relevance_score(prompt, output):
    emb1 = model.encode(prompt, convert_to_tensor=True)
    emb2 = model.encode(output, convert_to_tensor=True)
    return util.cos_sim(emb1, emb2).item()

print("Original Relevance:", relevance_score(original_prompt, original_output))
print("Enriched Relevance:", relevance_score(original_prompt, enriched_output))

