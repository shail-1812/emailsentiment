FROM python:3.9.14-buster

COPY ./requirements.txt /app/requirements.txt
# RUN pip install keras_preprocessing  
# RUN pip install spacy
# RUN pip install nlppreprocess
# RUN pip install nltk
# RUN pip install keras
# RUN pip install tensorflow
# RUN pip install flask
WORKDIR /app

RUN pip install -r requirements.txt
# ENV SPACY_VERSION    0.98
# RUN apt-get update && apt-get install tk-dev && rm -r /var/lib/apt/lists/
# RUN \
#     pip3 install -U jieba \
#         ipython \
#         numpy \
#         pandas \
#         requests \
#         chardet \
#     && pip3 install -U spacy==${SPACY_VERSION} \
#     && python3 -m spacy download en \
#     && python3 -m spacy download xx
RUN pip install spacy-download
RUN python -m spacy download en

# COPY finalized_model.sav ./finalized_model.sav
# COPY tokenizer.pickle ./tokenizer.pickle
# COPY templates/getemail.html ./getemail.html

# COPY app.py ./app.py

COPY . /app
ENTRYPOINT [ "python" ]

CMD ["app.py" ]

