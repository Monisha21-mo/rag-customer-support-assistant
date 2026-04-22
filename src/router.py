def route_query(query):
    query = query.lower()

    if "price" in query or "cost" in query:
        return "pricing"
    elif "help" in query or "support" in query:
        return "support"
    else:
        return "general"
