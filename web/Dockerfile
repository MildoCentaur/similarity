FROM python:3.7
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# RUN pip3 install --upgrade pip
COPY . .
RUN pip3 install ./es_core_news_sm-2.3.1.tar.gz
RUN ls
CMD ["python3", "app.py"]