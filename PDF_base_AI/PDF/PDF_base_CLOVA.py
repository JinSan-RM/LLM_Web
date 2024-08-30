# -*- coding: utf-8 -*-
import os
import requests

NCP_API_KEY = os.environ.get('NCP_API_KEY')
NCP_API_KEY_primary_val = os.environ.get('NCP_API_KEY_primary_val')
tree_structure = """- 트리구조는 이렇게 제시하면 돼. C:.
                                                    ├─메인
                                                    ├─회사소개
                                                    │  ├─CEO 인사말
                                                    │  ├─조직도
                                                    │  └─오시는 길
                                                    │
                                                    ├─사업소개
                                                    │   ├─사업분야
                                                    │   ├─사업성과
                                                    │   └─제품소개
                                                    │
                                                    └─고객센터
                                                        ├─공지사항
                                                        ├─고객문의
                                                        └─FAQ"""

content_structure = """ 1. 메인
                        내용 : 회사의 비전과 미션을 간략히 소개.
                        2. 회사 소개 (About Us)
                            2-1. CEO 인사말 
                            내용 : 회사의 기본 정보, 목표, 비전.
                            2-2. 조직도
                            내용 : 회사의 조직 구조 및 주요 인물 소개.
                            2-3. 연혁
                            내용 : 연도에 따른 회사 성장 과정.
                        3. 사업 소개 (Services)
                            3-1. 사업분야
                            내용 : 회사의 사업 아이템, 사업 분야.
                            3-2. 사업성과
                            내용 : 회사의 사업 성과
                            3-3. 제품소개
                            내용 : 회사 제품 및 서비스에 대한 설명
                        4. 고객센터
                            4-1. 공지사항
                            내용 : 회사의 최신 소식 및 이벤트.
                            4-2. 고객문의
                            내용 : 연락처 정보, 이메일, 소셜 미디어 링크 등.
                            4-3. FAQ
                            내용 : 자주 묻고 답하는 질문 및 답변.
                         """


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

        response = requests.post(self._host + '/testapp/v1/chat-completions/HCX-003',
                                headers=headers, json=completion_request, stream=False)
        response_text = response.text
        print(response_text)
        return response_text  # 이 부분에서 response_text를 반환

def PDF_Menu_Create_C(text):
        completion_executor = CompletionClova(
        host='https://clovastudio.stream.ntruss.com',
        api_key=NCP_API_KEY,
        api_key_primary_val=NCP_API_KEY_primary_val,
        request_id='e3f29a8a-b492-4f19-83df-2e7e83663fbd'
        )
        preset_text = [{"role":"system","content":"- 너는 기업소개 웹 사이트 기획자야. \n- 데이터는 회사소개서 혹은 제품소개서야. \n- 결과값은 2가지로 출력할거야. 하나는 이중 구조로 10개의 서브메뉴를 트리구조로 그리는 것. 다른 하나는 각 메뉴에 들어갈 내용을 적어줘"},
                   {"role":"user","content": text},
                   {"role":"assistant","content":f"{tree_structure}, {content_structure}"}]

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