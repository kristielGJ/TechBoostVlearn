
'''uses pip install jupyterlab python-dotenv langchain openai'''
import os
from dotenv import load_dotenv
import openai
import langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain import PromptTemplate
import re

#load api key from env file
load_dotenv()
my_key=os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0,openai_api_key=my_key)
text="What is AI?"
print(llm(text))


def get_response(prompt_question):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a helpful research and programming assistant"},
                  {"role": "user", "content": prompt_question}]
    )

    return response.choices[0].message.content

template = """
You are an expert quiz maker for technical fields. Let's think step by step and
create a quiz with {num_questions} {quiz_type} questions about the following concept/content: {quiz_context}.

The format of the quiz could be one of the following:
- Multiple-choice: 
- Questions:
    <Question1>: <a. Answer 1>, <b. Answer 2>, <c. Answer 3>, <d. Answer 4>
    <Question2>: <a. Answer 1>, <b. Answer 2>, <c. Answer 3>, <d. Answer 4>
    ....
- Answers:
    <Answer1>: <a|b|c|d>
    <Answer2>: <a|b|c|d>
    ....
    Example:
    - Questions:
    - 1. What is the time complexity of a binary search tree?
        a. O(n)
        b. O(log n)
        c. O(n^2)
        d. O(1)
    - Answers: 
        1. b
- True-false:
    - Questions:
        <Question1>: <True|False>
        <Question2>: <True|False>
        .....
    - Answers:
        <Answer1>: <True|False>
        <Answer2>: <True|False>
        .....
    Example:
    - Questions:
        - 1. What is a binary search tree?
        - 2. How are binary search trees implemented?
    - Answers:
        - 1. True
        - 2. False
- Open-ended:
- Questions:
    <Question1>: 
    <Question2>:
- Answers:    
    <Answer1>:
    <Answer2>:
Example:
    Questions:
    - 1. What is a binary search tree?
    - 2. How are binary search trees implemented?
    
    - Answers: 
        1. A binary search tree is a data structure that is used to store data in a sorted manner.
        2. Binary search trees are implemented using linked lists.
"""
prompt = PromptTemplate.from_template(template)
prompt.format(num_questions=3, quiz_type="multiple-choice", quiz_context="Data Structures in Python Programming")

chain = LLMChain(llm=ChatOpenAI(temperature=0.0),prompt=prompt)

quiz_response = chain.run(num_questions=3, quiz_type="multiple-choice", quiz_context="Data Structures in Python Programming",)

f = open("quiz_Python.txt", "a")
f.write(quiz_response)
f.close()


quiz_response = chain.run(num_questions=5, quiz_type="True-false", quiz_context="Marketing", verbose=True)
f = open("quiz_m.txt", "a")
f.write(quiz_response)
f.close()

quiz_response = chain.run(num_questions=3, quiz_type="Open-ended", quiz_context="Finance")
print(quiz_response)
f = open("quiz_fin.txt", "a")
f.write(quiz_response)
f.close()

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