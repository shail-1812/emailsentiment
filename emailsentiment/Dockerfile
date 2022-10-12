FROM jupyter/scipy-notebook

RUN pip install keras_preprocessing  
RUN pip install spacy
RUN pip install nlppreprocess
RUN pip install nltk
RUN pip install keras
RUN pip install tensorflow
RUN pip install flask
RUN pip install flask-wtf
RUN pip install tk
RUN python -m spacy download en

COPY finalized_model.sav ./finalized_model.sav
COPY tokenizer.pickle ./tokenizer.pickle
COPY templates/getemail.html ./getemail.html

COPY sentiment_functions.py ./sentiment_functions.py

