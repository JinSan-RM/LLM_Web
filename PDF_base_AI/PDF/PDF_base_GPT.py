from openai import OpenAI
import os
import tiktoken

OpenAI.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()


tree_structure = """- You can use this kind of structure when build a tree structure.
                    C:.
                    ├─Main
                    ├─About Us
                    │  ├─CEO's Message
                    │  ├─Organization Chart
                    │  └─Directions
                    │
                    ├─Business Overview
                    │   ├─Business Areas
                    │   ├─Business Achievements
                    │   └─Product Introduction
                    │
                    └─Customer Service
                        ├─Notices
                        ├─Customer Inquiries
                        └─FAQ"""

content_structure = """ - You can use this when make contents of menues
                    1. Main
                    Content: A brief introduction to the company's vision and mission.

                    2. About Us
                        2-1. CEO's Message
                            Content: Basic company information, goals, and vision.
                        2-2. Organization Chart
                            Content: Introduction to the company's organizational structure and key personnel.
                        2-3. History
                            Content: The company's growth process over the years.
                    
                    3. Services
                        3-1. Business Areas
                            Content: The company's business items and areas of operation.
                        3-2. Business Achievements
                            Content: The company's business accomplishments.
                        3-3. Product Introduction
                            Content: Description of the company's products and services.
                    
                    4. Customer Service
                        4-1. Notices
                            Content: The company's latest news and events.
                        4-2. Customer Inquiries
                            Content: Contact information, email, social media links, etc.
                        4-3. FAQ
                            Content: Frequently asked questions and answers. """

class CompletionGPT:
    def __init__(self, host, text):
        self._host = host
        self._text = text

def PDF_Menu_Create_G(text):
    truncated_text = truncate_text_to_token_limit(text)
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "- You are the organizer of the company introduction website. \n- Data is a company introduction letter or product introduction letter. \n- The result values will be printed in two ways. One is to draw 10 submenus in a tree structure. The other is to write down what goes into each menu"},
            {"role": "user", "content": truncated_text},
            {"role": "assistant", "content": f"{tree_structure}, {content_structure}"}
            # ,{
            # "role": "system",
            # "content": "You will perform two tasks: 1) Extract the main keywords from the text. 2) Write a brief introduction based on the text."
            # },
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