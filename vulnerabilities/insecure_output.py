def check_for_insecure_output(llm_response):
    # Check if the response contains any risky output that could be insecure
    if '<script>' in llm_response or '</script>' in llm_response:
        return "Potentially insecure output detected."
    return "No insecure output detected."
