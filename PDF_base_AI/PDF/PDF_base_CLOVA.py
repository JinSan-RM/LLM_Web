# -*- coding: utf-8 -*-
import os
import requests

NCP_API_KEY = os.environ.get('NCP_API_KEY')
NCP_API_KEY_primary_val = os.environ.get('NCP_API_KEY_primary_val')

class CompletionClova:
    def __init__(self, host, api_key, api_key_primary_val, request_id):
        self._host = host
        self._api_key = api_key
        self._api_key_primary_val = api_key_primary_val
        self._request_id = request_id

    def execute(self, completion_request):
        headers = {
            'X-NCP-CLOVASTUDIO-API-KEY': self._api_key,
            'X-NCP-APIGW-API-KEY': self._api_key_primary_val,
            'X-NCP-CLOVASTUDIO-REQUEST-ID': self._request_id,
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'text/event-stream'
        }

        with requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                           headers=headers, json=completion_request, stream=False) as r:
            for line in r.iter_lines():
                if line:
                    print(line.decode("utf-8"))

def PDF_Menu_Create_C(text):
        completion_executor = CompletionClova(
        host='https://clovastudio.stream.ntruss.com',
        api_key=NCP_API_KEY,
        api_key_primary_val=NCP_API_KEY_primary_val,
        request_id='e3f29a8a-b492-4f19-83df-2e7e83663fbd'
        )
        preset_text = [{"role":"system","content":"- 너는 기업소개 웹 사이트 기획자야. \n- 데이터는 회사소개서 혹은 제품소개서야. \n- 결과값은 2가지로 출력할거야. 하나는 이중 구조로 10개의 서브메뉴를 트리구조로 그리는 것. 다른 하나는 각 메뉴에 들어갈 내용을 적어줘"},
                   {"role":"user","content": text},
                   {"role":"assistant","content":"소셜 미디어는 사람들의 도파민을 풍성하게 해줘"}]

        request_data = {
            'messages': preset_text,
            'topP': 0.6,
            'topK': 0,
            'maxTokens': 256,
            'temperature': 0.2,
            'repeatPenalty': 1.2,
            'stopBefore': [],
            'includeAiFilters': True,
            'seed': 0
        }
        
        return completion_executor.execute(request_data)
    