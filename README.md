RAG CUSTOMER SUPPORT ASSISTANT

This RAG system is designed for an Indian e-commerce environment, focusing on high-precision retrieval from company policies to provide grounded, hallucination-free responses.

---

KEY FEATURES

* Context-Aware: Uses ChromaDB to fetch relevant policy sections.
* Hallucination Control: Strict prompting ensures answers stay within document scope.
* Safe Escalation: Directs out-of-scope queries to a grievance officer.
* Structured Outputs: Responses are formatted for professional support standards.

---

SYSTEM ARCHITECTURE

1. Ingestion: Documents split into chunks via sentence-transformers.
2. Storage: Embeddings stored in ChromaDB vector store.
3. Retrieval: Semantic search fetches top-k relevant policy chunks.
4. Generation: Mistral-7B generates the final grounded response.

---

# Setup & Installation

1. Clone the repository
   `git clone https://github.com/ASufiyan7/RAG_assignment`

2. Open the project folder
   `cd RAG_assignment`

3. Create a virtual environment
   `python -m venv venv`

4. Activate the environment

   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`

5. Install dependencies
   `pip install -r requirements.txt`

6. Create a `.env` file and add your HuggingFace token
   `HUGGINGFACEHUB_API_TOKEN=your_token_here`

7. Run the project
   `python main.py`

---

EVALUATION RESULTS

* Fully Answerable: Accurate & Grounded (Pass)
* Partially Answerable: High Relevance (Pass)
* Out of Scope: Safe Refusal/Escalation (Pass)

---

TECH STACK

* LLM: Mistral-7B (HuggingFace)
* Orchestration: LangChain
* Vector DB: ChromaDB
* Embeddings: Sentence-Transformers
* Language: Python

---

FUTURE IMPROVEMENTS

* Implementation of Cross-Encoder Reranking.
* JSON schema validation for structured data.
* Basic logging and tracing for better observability.

