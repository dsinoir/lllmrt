from flask import Blueprint, render_template, request
from vulnerabilities import prompt_injection, insecure_output, sensitive_info_disclosure

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['prompt']
        # Call LLM API and get the response
        response = get_llm_response(user_input)
        
        # Analyze the response
        pi_result = prompt_injection.check_for_prompt_injection(user_input, response)
        io_result = insecure_output.check_for_insecure_output(response)
        si_result = sensitive_info_disclosure.check_for_sensitive_information(response)
        
        results = {
            "Prompt Injection": pi_result,
            "Insecure Output": io_result,
            "Sensitive Information Disclosure": si_result
        }
        
        return render_template('index.html', results=results, user_input=user_input, response=response)
    
    return render_template('index.html')

def get_llm_response(prompt):
    # This function should call your LLM API and return the response
    headers = {
        "Authorization": f"Bearer {current_app.config['LLM_API_KEY']}",
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150,
    }
    response = requests.post(current_app.config['LLM_API_URL'], headers=headers, json=data)
    return response.json().get('choices')[0].get('text').strip()
