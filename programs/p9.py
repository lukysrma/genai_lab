#Take the Institution name as input. Use Pydantic to define the schema for the
#desired output and create a custom output parser. Invoke the Chain and Fetch
#Results. Extract the below Institution related details from Wikipedia: The
#founder of the Institution. When it was founded. The current branches in the
#institution . How many employees are working in it. A brief 4-line summary of
#the institution.

from pydantic import BaseModel
import wikipediaapi
# Define the Pydantic schema
class InstitutionDetails(BaseModel):
name: str
founder: str
founded_year: str
branches: str
employees: str
summary: str
# Wikipedia extraction function
def fetch_institution_details(institution_name: str) -> InstitutionDetails:
wiki_wiki = wikipediaapi.Wikipedia(user_agent="MyWikipediaScraper/1.0
(contact: myemail@example.com)", language="en")
page = wiki_wiki.page(institution_name)
if not page.exists():
raise ValueError("Institution page does not exist on Wikipedia")
# Extract information (this part needs actual content parsing)
summary = " ".join(page.summary.split(".")[:4]) + "."

VTUSYNC.IN

# Placeholder extraction logic
founder = "Not Available"
founded_year = "Not Available"
branches = "Not Available"
employees = "Not Available"
for section in page.sections:
if "founder" in section.title.lower():
founder = section.text.split(". ")[0]
if "founded" in section.title.lower():
founded_year = section.text.split(". ")[0]
if "branches" in section.title.lower():
branches = section.text.split(". ")[0]
if "employees" in section.title.lower():
employees = section.text.split(". ")[0]
return InstitutionDetails(
name=institution_name,
founder=founder,
founded_year=founded_year,
branches=branches,
employees=employees,
summary=summary
)
# Example invocation
institution_name = input("Enter Institution Name: ")
try:
details = fetch_institution_details(institution_name)
print(details.model_dump_json(indent=4))
except ValueError as e:
print(str(e))


#OUTPUT
#Enter Institution Name: Harvard University
#{
#"name": "Harvard University",
#"founder": "Not Available",
#"founded_year": "Not Available",
#"branches": "Not Available",
#"employees": "Not Available",
#"summary": "Harvard University is a private Ivy League research university in
#Cambridge, Massachusetts, United States Founded October 28, 1636, and named for
#its first benefactor, the Puritan clergyman John Harvard, it is the oldest institution of
#higher learning in the United States Its influence, wealth, and rankings have made it
#one of the most prestigious universities in the world \nHarvard was founded and
#
#authorized by the Massachusetts General Court, the governing legislature of colonial-
#era Massachusetts Bay Colony."}