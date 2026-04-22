from transformers import pipeline

qa_pipeline = pipeline("question-answering")

def rag_answer(query, retriever):
    docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in docs[:2]])

    result = qa_pipeline(
        question=query,
        context=context
    )

    return result['answer']
