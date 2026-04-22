from src.router import route_query
from src.hitl import hitl_check
from src.generator import rag_answer

def run_graph(query, retriever):
    route = route_query(query)
    answer = rag_answer(query, retriever)

    if hitl_check(answer):
        return f"[{route.upper()}] ⚠️ Escalated to Human"

    return f"[{route.upper()}] {answer}"
