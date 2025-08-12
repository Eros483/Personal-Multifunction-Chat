def web_search_prompt_template(query: str, information: str) -> str:
    """
    Sets prompt template for web search agent.
    Args:
        query (str): The user's query to answer.
        information (str): The information retrieved from web search.
    Returns:
        str: The formatted prompt template.
    """
    return f"""
    Based on the following information, please answer the user's query comprehensively and accurately, and in a concise manner.

    User Query: {query}

    Retrieved Information:
    {information}

    Please provide a clear, well-structured answer based on the information above to answer the user's query.
    If the information is not relevant to the query, return "No relevant information found."
    Do not include any additional information or context that is not present in the retrieved information.
    """