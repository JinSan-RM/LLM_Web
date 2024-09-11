import fitz
import tiktoken

def PDF2TEXT(pdf_list):
    total_text = ""
    
    for pdf_file in pdf_list:
        doc = fitz.open(stream=pdf_file, filetype="pdf")  # PDF 파일 객체로 열기

        num_pages = doc.page_count
        print(f"총 페이지 수: {num_pages}")

        extracted_text = ""

        # 모든 페이지 텍스트 추출
        for page_num in range(num_pages):
            page = doc[page_num]
            text = page.get_text()
            extracted_text += f"페이지 {page_num + 1}의 텍스트:\n{text}\n"
        
        total_text += extracted_text
        # 페이지에서 이미지 추출
        # image_list = page.get_images(full=True)
        # if image_list:
        #     for img in image_list:
        #         xref = img[0]
        #         base_image = doc.extract_image(xref)
        #         image_bytes = base_image["image"]
        #         image_ext = base_image["ext"]
                
                # 이미지 파일로 저장 (필요 시 활성화)
                # with open(f"image_{xref}.{image_ext}", "wb") as img_file:
                #     img_file.write(image_bytes)

    return total_text

def truncate_text_to_token_limit(text, max_tokens=9800):
    # tiktoken을 사용해 텍스트의 토큰 수를 계산하고 자르기
    gpt4_tokenizer = tiktoken.get_encoding("cl100k_base") # GPT4 tokenizer = cl100k_base
    gpt4_tokens = gpt4_tokenizer.encode(text)
    print("Gpt4_tokens = ", len(gpt4_tokens))

    gpt4o_tokenizer = tiktoken.get_encoding("o200k_base") # GPT4o tokenizer = o200k_base 
    gpt4o_tokens = gpt4o_tokenizer.encode(text)
    print("Gpt4o_tokens = ", len(gpt4o_tokens))
    print("[INFO] We use Gpt4o_tokens")
    if len(gpt4o_tokens) > max_tokens:
        gpt4o_tokens = gpt4o_tokens[:max_tokens]
    
    truncated_text = gpt4o_tokenizer.decode(gpt4o_tokens)
    return truncated_text