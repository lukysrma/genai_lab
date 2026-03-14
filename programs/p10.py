#Build a chatbot for the Indian Penal Code. We'll start by downloading the
#official Indian Penal Code document, and then we'll create a chatbot that can
#interact with it. Users will be able to ask questions about the Indian Penal
#Code and have a conversation with it.
#Step 1: Download the IPC PDF File
#Before running the chatbot, you must download the Indian Penal Code (IPC)
#PDF. Use the following Python script to download it:

import requests
def download_ipc_pdf(url, save_path="ipc.pdf"):
try:
response = requests.get(url)
response.raise_for_status()
with open(save_path, 'wb') as f:
f.write(response.content)
print(f"Downloaded IPC PDF to: {save_path}")
except requests.exceptions.RequestException as e:
print(f"Request error: {e}")
except Exception as e:
print(f"Unexpected error: {e}")
if __name__ == "__main__":

VTUSYNC.IN

ipc_pdf_url ="https://www.indiacode.nic.in/bitstream/123456789/4219/1/THE-
INDIAN-PENAL-CODE-1860.pdf"

download_ipc_pdf(ipc_pdf_url)
Instructions:
1. Save this script as a .py file (e.g., download_ipc.py).
2. Run the script to download the IPC PDF to your local system. By default, the file
will be saved as ipc.pdf.
3. Ensure the file is saved in the directory where you intend to run the chatbot
application, or provide the appropriate path.
Step 2: Run the Chatbot
Once the IPC PDF is downloaded, you can proceed with running the chatbot. The
chatbot will read from the ipc.pdf file to provide responses based on the Indian
Penal Code.
import PyPDF2
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def extract_text_from_pdf(pdf_path):
text = ""
try:
with open(pdf_path, 'rb') as file:
reader = PyPDF2.PdfReader(file)
for page in reader.pages:
text += page.extract_text() or ""
return text
except FileNotFoundError:
print(f"Error: File not found at {pdf_path}")
return ""
except Exception as e:
print(f"Error extracting text from PDF: {e}")
return ""
def preprocess_text(text):
if not text:
return []
text = text.lower()

VTUSYNC.IN

text = text.translate(str.maketrans('', '', string.punctuation))
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]
return tokens
def create_index(text):
index = {}
try:
section_pattern =
r"((?:CHAPTER|SECTION)\s+\w+\.?\s+.*?)(?:(?:CHAPTER|SECTION)\s+\w+\.?\s+|$
)"
matches = re.findall(section_pattern, text, re.DOTALL | re.IGNORECASE)
for match in matches:
title_match = re.search(r"^(?:CHAPTER|SECTION)\s+\w+\.?\s+(.*?)(?=\n)",
match, re.DOTALL | re.IGNORECASE)
if title_match:
title = title_match.group(1).strip()
content = match[title_match.end():].strip()
index[title] = content
return index
except Exception as e:
print(f"Error creating index: {e}")
return {}
def get_most_relevant_section(query, index):
try:
if not index:
return None
sections = list(index.values())
section_titles = list(index.keys())
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sections + [query])
query_vector = tfidf_matrix[-1]
similarities = cosine_similarity(query_vector, tfidf_matrix[:-1]).flatten()
if not similarities.any():
return None
most_relevant_index = similarities.argmax()
return section_titles[most_relevant_index]
except Exception as e:
print(f"Error finding relevant section: {e}")
return None

VTUSYNC.IN

def get_section_text(section_title, index):
try:
return index.get(section_title)
except Exception as e:
print(f"Error getting section text: {e}")
return None
def generate_response(query, index):
if not index:
return "I'm sorry, I cannot process the IPC without the index. Please ensure the
IPC content is loaded."
relevant_section_title = get_most_relevant_section(query, index)
if not relevant_section_title:
return "I'm sorry, I couldn't find relevant information in the IPC for your query."
section_text = get_section_text(relevant_section_title, index)
if not section_text:
return "I found the relevant section, but I'm unable to retrieve the details."
cleaned_text = re.sub(r'\n\s*\n+', '\n\n', section_text.strip())
cleaned_text = re.sub(r'[ \t]+\n', '\n', cleaned_text)
cleaned_text = re.sub(r'\n+', '\n', cleaned_text)
response = f"Here's what I found in the Indian Penal Code,
**{relevant_section_title}**:\n\n{cleaned_text}"
return response
def chatbot(index):
print("Welcome to the Indian Penal Code Chatbot! Ask me anything about the IPC.
Type 'exit' to quit.")
while True:
query = input("You: ")
if query.lower() == "exit":
break
response = generate_response(query, index)
print(f"Chatbot: {response}\n")
if __name__ == "__main__":
pdf_path = "ipc.pdf" # Path to your local IPC PDF
ipc_text = extract_text_from_pdf(pdf_path)
if ipc_text:
ipc_index = create_index(ipc_text)
if ipc_index:
chatbot(ipc_index)
else:
print("Failed to create index. Chatbot cannot start.")
VTUSYNC.IN

else:
print("Failed to extract text from PDF. Chatbot cannot start.")