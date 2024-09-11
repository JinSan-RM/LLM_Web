from PDF.PDF_2_TEXT import PDF2TEXT
from PDF.PDF_base_GPT import PDF_Menu_Create_G, truncate_text_to_token_limit
from PDF.PDF_base_CLOVA import PDF_Menu_Create_C
from fastapi import FastAPI
import requests
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
        
        text = PDF2TEXT(pdf_list)
        text = truncate_text_to_token_limit(text)
        G_data = PDF_Menu_Create_G(text)
        # C_data = PDF_Menu_Create_C(text)
        return {"message": "PDF 다운로드 및 처리 성공", "GPT": G_data} # "Clova":C_data
    else:
        return {"message": "PDF 다운로드 실패"}