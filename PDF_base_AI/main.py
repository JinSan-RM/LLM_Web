from PDF.PDF_2_TEXT import PDF2TEXT
from PDF.PDF_base_GPT import PDF_Menu_Create_G, truncate_text_to_token_limit
from PDF.PDF_base_CLOVA import PDF_Menu_Create_C
from fastapi import FastAPI
import requests
from io import BytesIO

app = FastAPI()

@app.get('/PDFAI')
def main(path: str):
    response = requests.get(path)
    if response.status_code == 200:
        pdf_data = BytesIO(response.content)
        
        text = PDF2TEXT(pdf_data)
        text = truncate_text_to_token_limit(text)
        G_data = PDF_Menu_Create_G(text)
        C_data = PDF_Menu_Create_C(text)
        return {"message": "PDF 다운로드 및 처리 성공", "GPT": G_data, "Clova":C_data}
    else:
        return {"message": "PDF 다운로드 실패"}