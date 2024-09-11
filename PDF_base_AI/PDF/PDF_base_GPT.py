from openai import OpenAI
import os


OpenAI.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()



menu_structure = """- You can use this kind of structure when build two_depth menu. start with 'number' is first_depth menu. start with '-' is second_depth menu.
                    1. Home
                    2. Company Introduction   
                            - Company History   
                            - Company Vision   
                            - CEO Message
                    3. Business Overview   
                            - Business Areas
                            - Business Achievements
                            - Future Goals
                    4. Team   
                            - Team Members   
                    5. Representative Contents   
                            - Education Methodology   
                            - Sejong Institute Content   
                    6. Contact Us   
                            - Location   
                            - Phone   
                            - Fax
                    7. FAQs"""

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
    # truncated_text = truncate_text_to_token_limit(text)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """- You are the organizer of the company introduction website. 
             - Data is a company introduction letter or product introduction letter. 
             - The result values will be printed in two ways.
             - One is to write two_depth menu refer to menu_structure in assistant. The total number of second_depth menus must be 10. Don't need to write extra explaination about second_depth. the length of menus should be less than 15 letters.
             - The other is pick 3 keywords in the contents.
             - Write in Korean."""}, # 
            {"role": "user", "content": text},
            {"role": "assistant", "content": f"{menu_structure}"} # {content_structure}
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