import re

def check_for_prompt_injection(user_input, llm_response):
    # Basic check: Does the response include anything that suggests it was influenced by malicious input?
    if re.search(r'\b(system|bash|command)\b', llm_response, re.IGNORECASE):
        return "Potential prompt injection detected."
    return "No prompt injection detected."
