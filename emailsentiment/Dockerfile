FROM python:3.9.14

WORKDIR /app
COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN pip install spacy-download
RUN python -m spacy download en

COPY app.py /app
COPY test.json /app
COPY tokenizer.pickle /app
COPY finalized_model.sav /app

CMD ["python", "./app.py"]

