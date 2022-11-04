FROM public.ecr.aws/lambda/python:3.9

# WORKDIR /app
# COPY requirements.txt ./

# RUN pip install -r requirements.txt
# RUN pip install spacy-download
# RUN python -m spacy download en

# COPY app.py /app
# COPY test.json /app
# COPY tokenizer.pickle /app
# COPY finalized_model.sav /app

# CMD ["python", "./app.py"]

WORKDIR /app
COPY app.py /app ${LAMBDA_TASK_ROOT}
COPY requirements.txt /app
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
COPY tokenizer.pickle /app
COPY finalized_model.sav /app
CMD ["app.handler"]


