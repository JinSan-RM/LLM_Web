# Python 3.9 이미지 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /code

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /code/PDF_base_AI/requirements.txt

# RUN apt-get install wget
# RUN apt-get update
# RUN apt-get install libgconf2-4 libnss3-1d libxss1
# RUN pip install selenium 
# # RUN apt-get install gdebi -y
# RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
# # RUN apt install google-chrome-stable_current_amd64.deb

RUN pip install --no-cache-dir --upgrade -r /code/PDF_base_AI/requirements.txt
# RUN git config --global http.postBuffer 524288000

# Set non-interactive and timezone
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Seoul

# # Install Tesseract and Leptonica
# RUN apt-get update \
#     && apt-get install -y \
#     tesseract-ocr \
#     libtesseract-dev \
#     libleptonica-dev \
#     tesseract-ocr-eng \
#     tesseract-ocr-kor

# # Install pytesseract
# RUN pip install pytesseract

# # Set the Tesseract path
# ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

# # Install dependencies
# RUN apt-get update \
#     && apt-get install -y \
#     software-properties-common \
#     wget \
#     git \
#     gcc \
#     g++ \
#     make \
#     autoconf \
#     automake \
#     libtool \
#     libleptonica-dev \
#     pkg-config

# # Install Leptonica from source
# RUN wget http://www.leptonica.org/source/leptonica-1.79.0.tar.gz \
#     && tar -zxvf leptonica-1.79.0.tar.gz \
#     && cd leptonica-1.79.0 \
#     && ./configure --prefix=/usr/local/leptonica-1.79.0 \
#     && make \
#     && make install

# # Install Tesseract from source
# RUN export PKG_CONFIG_PATH=/usr/local/leptonica-1.79.0/lib/pkgconfig \
#     && git clone https://github.com/tesseract-ocr/tesseract.git \
#     && cd tesseract \
#     && ./autogen.sh \
#     && ./configure --prefix=/usr/local/tesseract \
#     && make \
#     && make install

# # Copy the traineddata files
# COPY ./kor.traineddata /usr/local/tesseract/share/tessdata
# COPY ./eng.traineddata /usr/local/tesseract/share/tessdata

# # Set environment variables for tesseract
# ENV PATH=$PATH:/usr/local/tesseract/bin
# ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/tesseract/lib
# ENV TESSDATA_PREFIX=/usr/local/tesseract/share/tessdata


ENV PYTHONPATH="/code:/code/PDF_base_AI"


# RUN pip3 install selenium

# CMD ["python", "-m", "debugpy", "--wait-for-client", "--listen", "0.0.0.0:5678", "main.py"]
# COPY ./app /code/app
# 
CMD ["uvicorn", "PDF_base_AI.main:app", "--reload", "--forwarded-allow-ips", "*", "--host", "0.0.0.0", "--port", "80"]
