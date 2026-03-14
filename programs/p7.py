#7. Summarize long texts using a pre-trained summarization model using Hugging face model. Load the summarization pipeline. Take a passage as input and obtain the summarized text.

# Required libraries (install before running this script):
# pip install transformers torch

from transformers import pipeline  # Import the summarization pipeline from Hugging Face Transformers

# Load a smaller and faster pre-trained model for summarization
# 't5-small' is lightweight and quick, ideal for small/medium passages
summarizer = pipeline("summarization", model="t5-small")

# Input text to be summarized
text = """
The Industrial Revolution, which took place from the 18th to the 19th centuries, was a period during which predominantly agrarian, rural societies in Europe and America became industrial and urban. Prior to the Industrial Revolution, manufacturing was often done in people's homes, using hand tools or basic machines. Industrialization marked a shift to powered, special-purpose machinery, factories and mass production. The iron and textile industries, along with the development of the steam engine, played central roles in the Industrial Revolution, which also saw improved systems of transportation, communication and banking. While industrialization brought about an increased volume and variety of manufactured goods and an improved standard of living for some, it also resulted in often grim employment and living conditions for the poor and working classes.
"""

# Generate the summary of the input text
summary = summarizer(text, max_length=60, min_length=30, do_sample=False)

# Print the summarized output
print(summary[0]['summary_text'])