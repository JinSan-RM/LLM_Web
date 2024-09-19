from openai import OpenAI
import os
import tiktoken


OpenAI.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()


title_structure = """- You can use this example to write down title.
                    [Title]
                    The example of title
                    """

keywords_structure = """- You can use this example to write down keywords.
                    [Keywords]
                    1. A
                    2. B
                    3. C
                    """

menu_structure = """- You can use this kind of structure when build two_depth menu. start with 'number' is first_depth menu. start with '-' is second_depth menu.
                    [Two_depth Menu]
                    1. Home
                    2. Company Introduction   
                            - Company History   
                            - Company Vision   
                            - CEO Message                    
                    3. Business Overview   
                            - Business Areas
                            - Business Achievements
                            - Future Goals 
                    4. Contact Us
                            - Location   
                            - Phone   
                            - FAQs
                            - Team members"""

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


# NOTE : Keywords와 Title을 미리 뽑고, 그 이후에 메뉴 뽑기. 그래야 메뉴로 인해서 뒤가 짤리는 현상 방지 가능

def PDF_Menu_Create_G(text):
    # truncated_text = truncate_text_to_token_limit(text)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """- You are the organizer of the company introduction website. 
             - Data is a company profile or company introduction. 
             - The result values will be printed in three ways.
             - First is the title of website.
             - Second is pick 3 keywords in the contents.
             - Third is to write two_depth menu refer to menu_structure in assistant. The first_depth must be 3~5. The second_depth must be 0~4. Don't need to write extra explaination about second_depth. the length of menus should be less than 15 letters.
             - Write in Korean."""}, # 
            {"role": "user", "content": text},
            {"role": "assistant", "content": f"{title_structure}, {keywords_structure}, {menu_structure}"} # {content_structure}
            # ,{
            # "role": "system",
            # "content": "You will perform two tasks: 1) Extract the main keywords from the text. 2) Write a brief introduction based on the text."
            # },
            # {"role": "user", "content": }
        ],
        temperature=0.2,
        max_tokens=200,
        top_p=1
    )
    
    
    return completion

def truncate_input_text_to_token_limit(text, max_tokens=9800):
    # tiktoken을 사용해 텍스트의 토큰 수를 계산하고 자르기
    gpt4_tokenizer = tiktoken.get_encoding("cl100k_base") # GPT4 tokenizer = cl100k_base
    gpt4_tokens = gpt4_tokenizer.encode(text)
    print("Input_Gpt4_tokens = ", len(gpt4_tokens))

    gpt4o_tokenizer = tiktoken.get_encoding("o200k_base") # GPT4o tokenizer = o200k_base 
    gpt4o_tokens = gpt4o_tokenizer.encode(text)
    print("Input_Gpt4o_tokens = ", len(gpt4o_tokens))
    print("[INFO] We use Gpt4o_tokens")
    if len(gpt4o_tokens) > max_tokens:
        gpt4o_tokens = gpt4o_tokens[:max_tokens]
    
    truncated_text = gpt4o_tokenizer.decode(gpt4o_tokens)
    return truncated_text

def count_output_token(output_data):
    
    # print("================= test ================")
    # print(type(output_data))
    # print(output_data)
    
    real_content = output_data.choices[0].message.content
    
    gpt4o_tokenizer = tiktoken.get_encoding("o200k_base") # GPT4o tokenizer = o200k_base 
    gpt4o_tokens = gpt4o_tokenizer.encode(real_content)
    
    num_of_output_token = len(gpt4o_tokens)
    print("Output_Gpt4o_tokens = ", num_of_output_token)
    
    return num_of_output_token