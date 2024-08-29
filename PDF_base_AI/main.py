from PDF.PDF_2_TEXT import PDF2TEXT
from PDF.PDF_base_GPT import PDF_Menu_Create
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
        print(text, "<=====text")
        data = PDF_Menu_Create(text)
        return {"message": "PDF 다운로드 및 처리 성공", "text": data}
    else:
        return {"message": "PDF 다운로드 실패"}