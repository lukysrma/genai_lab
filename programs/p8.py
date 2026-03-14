#Install langchain, cohere (for key), langchain-community. Get the api key( By
#logging into Cohere and obtaining the cohere key). Load a text document from
#your google drive . Create a prompt template to display the output in a
#particular manner


from langchain.prompts import PromptTemplate
from langchain_community.llms import Cohere
# Set your Cohere API key
COHERE_API_KEY = "YOUR_COHERE_API" # Replace with your actual API key
# Read the text file
file_path = "Artificial_Intelligence.txt" # Replace with your file name
with open(file_path, "r", encoding="utf-8") as file:
document_text = file.read()
print("File loaded successfully!")
Output 1:- File loaded successfully!
# Create a simple prompt template
prompt_template = PromptTemplate(
input_variables=["text"],
template="Summarize the following text in a simple way:\n\n{text}"
)
# Initialize the Cohere model
llm = Cohere(cohere_api_key=COHERE_API_KEY)
# Run the text through Cohere
output = llm.invoke(prompt_template.format(text=document_text))
# Display the result
print("Summary:\n", output)

