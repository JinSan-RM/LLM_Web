from openai import OpenAI
import os
import tiktoken

OpenAI.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()

class CompletionGPT:
    def __init__(self, host, text):
        self._host = host
        self._text = text

def PDF_Menu_Create(text):
    truncated_text = truncate_text_to_token_limit(text)
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "- You are the organizer of the company introduction website. \n- Data is a company introduction letter or product introduction letter. \n- The result values will be printed in two ways. One is to draw 10 submenus in a tree structure. The other is to write down what goes into each menu"},
            {"role": "user", "content": truncated_text},
            {"role": "assistant", "content": "Understood. I will help you create a structured web header menu based on the contents you provide. I will ensure that the submenus are logically related to the main menus, and the entire structure will be clear and organized, with a maximum of 10 items in a tree format."},
            # {"role": "user", "content": }
        ],
        temperature=0.1,
        max_tokens=300,
        top_p=1
    )
    
    return completion

def truncate_text_to_token_limit(text, max_tokens=7700):
    # tiktoken을 사용해 텍스트의 토큰 수를 계산하고 자르기
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
    
    truncated_text = tokenizer.decode(tokens)
    return truncated_text