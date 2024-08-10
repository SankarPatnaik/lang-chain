from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
#os.environ['OPENAI_API_KEY'] = openapi_key


llm = OpenAI(temperature=0.7)
#llm = GooglePalm(google_api_key=api_key, temperature=0.5)
def generate_Institute_name(course):
    # Chain 1: Institute Name
    prompt_template_name = PromptTemplate(
        input_variables=['course'],
        template="""I want to open a Training Institute for {course}. Suggest a good name."""
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="Institute_name")

    # Chain 2: Menu Items

    prompt_template_items = PromptTemplate(
        input_variables=['Institute_name'],
        template="""Suggest some Institute for {Institute_name}. Return it as a comma separated string"""
    )

    Institute_name_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="subject")

    chain = SequentialChain(
        chains=[name_chain, Institute_name_chain],
        input_variables=['course'],
        output_variables=['Institute_name', "subject"]
    )

    response = chain({'course': course})

    return response

if __name__ == "__main__":
    print(generate_Institute_name("Gen AI"))
