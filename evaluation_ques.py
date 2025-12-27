from main import prepare_data, create_vector_store, rag_system

evaluation_questions = [
    "What is your refund policy?",
    "How long does shipping take?",
    "What happens if my product is damaged?",
    "Can I cancel an order after delivery?",
    "Do you sell laptops?",
    "Is cryptocurrency accepted as payment?",
    "Do you offer student discounts?"
]

chunks = prepare_data("policy_documents")
vector_store = create_vector_store(chunks)

for idx, question in enumerate(evaluation_questions, 1):
    print(f"{question}\n")
    answer = rag_system(question, vector_store)

    print("Response:\n")
    print(answer)
