RAG Based Customer Support Assistant
AI Engineer Intern – Take Home Assignment

This project is a simple Retrieval-Augmented Generation (RAG) based customer support assistant designed for an Indian e-commerce company.
It answers customer questions by retrieving information from company policy documents and generating grounded, safe, and structured responses.

The main focus of this project is prompt engineering, hallucination control, retrieval quality, and evaluation, as required in the assignment.

What This Project Does

Loads company policy documents (refund, shipping, cancellation, etc.)

Converts them into embeddings and stores them in a vector database

Retrieves the most relevant information for a user query

Generates a clear, structured answer strictly from retrieved context

Safely refuses and escalates when information is not available

How It Works (High Level)
User Question  
   ↓  
Chroma Vector Search  
   ↓  
Relevant Policy Chunks  
   ↓  
Structured Prompt  
   ↓  
Mistral 7B LLM  
   ↓  
Final Answer / Safe Refusal

Setup Instructions

Clone the repository and create a virtual environment:

git clone <your_repo_link>
cd RAG_assignment
python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Add your HuggingFace token in a .env file:

HUGGINGFACEHUB_API_TOKEN=your_token_here


Run the system:

python main.py

Prompt Engineering

Two prompt versions were designed and tested:

Prompt V1 (Initial)
A basic prompt that instructed the model to answer only from the context.

Prompt V2 (Improved)
The final prompt adds:

Strict hallucination prevention

Structured answer format

Professional refusal and escalation template

Clear bullet-point based answers

This significantly improved clarity and prevented incorrect or made-up responses.

Evaluation

An evaluation set of 7 questions was created, containing:

Fully answerable questions

Partially answerable questions

Out-of-scope questions

Question Type	Model Behavior
Answerable	Returned accurate, grounded answers
Partially Answerable	Gave acceptable responses using available context
Out of Scope	Properly refused without hallucinating

No hallucinations were observed during evaluation.

Edge Case Handling

If no relevant documents are found, the system returns a safe refusal message

If the question is outside the policy knowledge base, it escalates to the grievance officer

This ensures reliability and safety in real customer scenarios.

Tech Stack

Python

LangChain

ChromaDB

HuggingFace Mistral 7B

Sentence-Transformers

What I’m Most Proud Of

Designing a clean and simple RAG pipeline with strict hallucination control and clear evaluation evidence.

What I Would Improve Next

Given more time, I would add:

Reranking for better retrieval accuracy

JSON schema validation

Automated evaluation scoring

Basic logging and tracing
