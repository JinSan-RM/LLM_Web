from PDF.PDF_2_TEXT import PDF2TEXT
from PDF.PDF_base_GPT import PDF_Menu_Create_G, truncate_input_text_to_token_limit, count_output_token
from PDF.PDF_base_CLOVA import PDF_Menu_Create_C
from fastapi import FastAPI
import requests, json
from io import BytesIO

app = FastAPI()

@app.get('/PDFAI')
def main(path: str, path2: str='', path3: str=''):
    pdf_list = []
    response = requests.get(path)

    if response.status_code == 200:
        pdf_data = BytesIO(response.content)
        pdf_list.append(pdf_data)
        
        if path2 != ''  :
        # print("path2 : ", path2)
            response2 = requests.get(path2)
            pdf_data2 = BytesIO(response2.content)
            pdf_list.append(pdf_data2)
        if path3 != '' :
        # print("path3 : ", path3)
            response3 = requests.get(path3)
            pdf_data3 = BytesIO(response3.content)
            pdf_list.append(pdf_data3)
        
        all_text = PDF2TEXT(pdf_list)

        truncated_text = truncate_input_text_to_token_limit(all_text)
        
        G_data = PDF_Menu_Create_G(truncated_text)
         
        
        G_output_token_num = count_output_token(G_data)
        
        # C_data = PDF_Menu_Create_C(text)
        return {"message": "PDF 다운로드 및 처리 성공", "G_output_token_num" : G_output_token_num, "GPT": G_data} # "Clova":C_data / 
    else:
        return {"message": "PDF 다운로드 실패"}
    
    

def save_to_local(G_data, file_name="output.json"):
    # G_data와 C_data의 내용을 텍스트 형태로 추출
    gpt_content = G_data.choices[0].message.content if hasattr(G_data, 'choices') else str(G_data)
    
    # 결합할 데이터를 딕셔너리로 구성
    data = {
        "GPT": gpt_content,
    }
    
    # 경로를 지정하지 않으면 현재 작업 디렉토리에 저장됩니다.
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    
    print(f"데이터가 {file_name}에 성공적으로 저장되었습니다.")


# def save_to_local(G_data, C_data, file_name="output.json"):
#     # G_data와 C_data의 내용을 텍스트 형태로 추출
#     gpt_content = G_data.choices[0].message.content if hasattr(G_data, 'choices') else str(G_data)
#     clova_content = C_data.choices[0].message.content if hasattr(C_data, 'choices') else str(C_data)
    
#     # 결합할 데이터를 딕셔너리로 구성
#     data = {
#         "GPT": gpt_content,
#         "Clova": clova_content
#     }
    
#     # 경로를 지정하지 않으면 현재 작업 디렉토리에 저장됩니다.
#     with open(file_name, 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
    
#     print(f"데이터가 {file_name}에 성공적으로 저장되었습니다.")