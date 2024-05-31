
'''uses pip install jupyterlab python-dotenv langchain openai
Author: Gera Jahja
IGNORE THIS FILE, IT IS FOR TESTING CONCEPTS , NOT PART OF BACKEND FUNCTIONALITY
'''
import os
from dotenv import load_dotenv
import openai
import langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
import re
import codecs, json

#load api key from env file
load_dotenv()
my_key=os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0,openai_api_key=my_key)

def get_response(prompt_question):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful research and programming assistant"},
                  {"role": "user", "content": prompt_question}]
    )

    return response.choices[0].message.content

template ="""
You are an expert quiz maker for technical fields. Let's think step by step and create a quiz with {num_questions} {quiz_type} questions about the following concept/content: {quiz_context}.Only provide JSON code as a response, no other response.

The format of the quiz could be stored in JSON format as follows:

- For Multiple-choice questions:
{{
  "quizType": "Multiple-choice",
  "quizContext": "{{quiz_context}}",
  "questions": [
    {{
      "question": "Question1 text here",
      "options": {{
        "a": "Answer 1",
        "b": "Answer 2",
        "c": "Answer 3",
        "d": "Answer 4"
      }},
      "correctAnswer": "a|b|c|d"
    }},
    {{
      "question": "Question2 text here",
      "options": {{
        "a": "Answer 1",
        "b": "Answer 2",
        "c": "Answer 3",
        "d": "Answer 4"
      }},
      "correctAnswer": "a|b|c|d"
    }}
  ]
}}
- For True/false questions:

{{
  "quizType": "True-False",
  "quizContext": "{{quiz_context}}",
  "questions": [
    {{
      "question": "Question1 text here",
      "correctAnswer": "True|False"
    }},
    {{
      "question": "Question2 text here",
      "correctAnswer": "True|False"
    }}
  ]
}}
- For Open-ended questions:

{{
  "quizType": "Open-ended",
  "quizContext": "{{quiz_context}}",
  "questions": [
    {{
      "question": "Question1 text here",
      "answer": "Detailed answer here"
    }},
    {{
      "question": "Question2 text here",
      "answer": "Detailed answer here"
    }}
  ]
}}
- Example for Multiple-choice:

{{
  "quizType": "Multiple-choice",
  "quizContext": "Binary search tree complexities",
  "questions": [
    {{
      "question": "What is the time complexity of a binary search tree?",
      "options": {{
        "a": "O(n)",
        "b": "O(log n)",
        "c": "O(n^2)",
        "d": "O(1)"
      }},
      "correctAnswer": "b"
    }}
  ]
}}
"""
prompt = PromptTemplate.from_template(template)
prompt.format(num_questions=3, quiz_type="multiple-choice", quiz_context="Data Structures in Python Programming")

chain = LLMChain(llm=ChatOpenAI(temperature=0.0),prompt=prompt)

quiz_response = chain.run(num_questions=5, quiz_type="multiple-choice", quiz_context="Data Structures in Python Programming",)
'''
quiz_response = chain.run(num_questions=3, quiz_type="True-false", quiz_context="Marketing", verbose=True)

quiz_response = chain.run(num_questions=5, quiz_type="Open-ended", quiz_context="Finance")
'''
# Write JSON file
filename = 'quiz_data.json'

try:
    json_data = json.loads(quiz_response)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)
    json_data = None

with open(filename, 'w') as file:
    json.dump(json_data, file, indent=4)

'''
# Load, chunk and index the contents of the blog.
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
rag_chain.invoke("What is Task Decomposition?")
# cleanup
vectorstore.delete_collection()
'''