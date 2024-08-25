import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    LLM_API_KEY = os.environ.get('LLM_API_KEY')
    LLM_API_URL = os.environ.get('LLM_API_URL') or 'https://api.openai.com/v1/engines/davinci-codex/completions'
