import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Load and chunk policy docs
def prepare_data(directory_path):
    loader = DirectoryLoader(directory_path, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=100)
    return splitter.split_documents(documents)

# Create vector database
def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return Chroma.from_documents(documents=chunks, embedding=embeddings)


# Prompt V1 (Basic)
prompt_v1 = ChatPromptTemplate.from_template("""
You are a customer support assistant.
Answer ONLY from the context.

Context:
{context}

Question:
{question}

Answer:
""")

# Prompt V2 (Improved & structured)
prompt_v2 = ChatPromptTemplate.from_template("""
You are a professional Indian E-commerce Customer Support AI.

Rules:
- Use ONLY the given context
- Do NOT hallucinate
- If answer is missing, respond using the Not Available format

Context:
{context}

Question:
{question}

Response:

If answer exists:

Answer:
- Use bullet points

Source: Company Policy Documents

If answer does NOT exist:

Not Available
This information is not present in our policy records.
Please contact:
- grievance@company.com
""")


# RAG Pipeline
def rag_system(query, vector_store):
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    # Edge case: No relevant documents found
    if not docs:
        return "No relevant policy found. Please contact grievance@company.com"

    context = "\n".join(doc.page_content for doc in docs)

    prompt = prompt_v2.format(context=context, question=query)

    client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

    response = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=[
            {"role": "system", "content": "You are a customer support assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,
        max_tokens=400
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    chunks = prepare_data("policy_documents")
    vector_store = create_vector_store(chunks)

    test_query = "What is your refund policy?"
    print("\nResponse:\n")
    print(rag_system(test_query, vector_store))
