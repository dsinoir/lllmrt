import re

def check_for_sensitive_information(llm_response):
    # Example: Check for patterns resembling sensitive data like credit card numbers, SSNs, etc.
    sensitive_patterns = [
        r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
        r'\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b',  # Credit card number
    ]
    
    for pattern in sensitive_patterns:
        if re.search(pattern, llm_response):
            return "Sensitive information detected."
    
    return "No sensitive information detected."
