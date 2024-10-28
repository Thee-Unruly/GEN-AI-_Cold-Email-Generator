from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key='your groq api key',
    model_name = "llama-3.1-70b-versatile",
    temperature=0
)

#response = llm.invoke('')
#print (response)

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://jobs.nike.com/job/R-40807?from=job%20search%20funnel")

page_data = loader.load().pop().page_content
#print(page_data)

from langchain_core.prompts import PromptTemplate

prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
)

chain_extract = prompt_extract | llm 
res = chain_extract.invoke(input={'page_data':page_data})
res.content

from langchain_core.output_parsers import JsonOutputParser

json_parser = JsonOutputParser()

json_res = json_parser.parse(res.content)
